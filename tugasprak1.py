import tkinter as tk

def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

def handle_encrypt():
    text = text_entry.get()
    shift = int(shift_entry.get())
    encrypted_text = encrypt(text, shift)
    result_label.config(text="Encrypted: " + encrypted_text)

def handle_decrypt():
    text = text_entry.get()
    shift = int(shift_entry.get())
    decrypted_text = decrypt(text, shift)
    result_label.config(text="Decrypted: " + decrypted_text)

root = tk.Tk()
root.title("Caesar Cipher")

tk.Label(root, text="Text:").grid(row=0, column=0)
text_entry = tk.Entry(root, width=30)
text_entry.grid(row=0, column=1)

tk.Label(root, text="Shift:").grid(row=1, column=0)
shift_entry = tk.Entry(root, width=5)
shift_entry.grid(row=1, column=1)

encrypt_button = tk.Button(root, text="Encrypt", command=handle_encrypt)
encrypt_button.grid(row=2, column=0)

decrypt_button = tk.Button(root, text="Decrypt", command=handle_decrypt)
decrypt_button.grid(row=2, column=1)

result_label = tk.Label(root, text="Result will be shown here")
result_label.grid(row=3, column=0, columnspan=2)

root.mainloop()
