# DESKRIPSI TUGAS


Tugas ini terdiri dari tiga kodingan tentang algoritma Caesar Cipher, algoritma DES, dan algoritma Steganography. Berikut adalah rincian dari masing-masing file:

## 1. Caesar Cipher
   Kode tersebut(tugasprak1.py) adalah aplikasi GUI sederhana untuk Caesar Cipher, sebuah algoritma kriptografi klasik yang mengenkripsi atau mendekripsi teks dengan cara mengganti setiap huruf berdasarkan pergeseran (shift).
   Cara menjalakannya:
   1. Jalankan pada terminal python tugasprak1.py, maka akan muncul tampilan gui-nya.
   2. Masukkan teks yang ingin dienkripsi atau didekripsi di kotak "Text".
   3. Masukkan nilai pergeseran (1-25) di kotak "Shift".
   4. Klik tombol Encrypt untuk mengenkripsi teks atau Decrypt untuk mendekripsi.
   5. Hasilnya akan muncul di label di bawah tombol.
  
 ## 2. Data Encryption Standard(DES)
Kode tersebut(des.py) adalah implementasi aplikasi GUI menggunakan Python untuk enkripsi dan dekripsi dengan algoritma DES (Data Encryption Standard).
   Cara Menjalankannya:
   1. Instal pustaka pycryptodome (jika belum terinstal) dengan perintah pip install pycryptodome.
   2. Ketikkan pada terminal python des.py, lalu akan muncul tampilangui-nya.
   3. Masukkan teks di kotak Input Text.
   4. Masukkan kunci (8 karakter) di kotak Key (8 karakter).
   5. Klik tombol Encrypt untuk mengenkripsi teks. Hasilnya akan muncul di kotak Output Text.
   6. Untuk dekripsi:
      - Salin hasil terenkripsi ke kotak Input Text.
      - Masukkan kunci yang sama di kotak Key.
      - Klik tombol Decrypt untuk mendapatkan teks asli.
## 3. Steganography
Kode tersebut(stgn.py) adalah aplikasi GUI untuk steganografi, yaitu menyembunyikan atau mengungkap pesan dalam gambar menggunakan teknik Least Significant Bit (LSB).
Cara menjalankannya:
1. Install pustaka stegano(apabila belum terinstall), dengan cara mengetikkan pip install stegano pada 
2. Jalankan file melalui terminal atau IDE Python dengan cara mengetikkan python stgn.py
3. Menyembunyikan Pesan:
      - Klik tombol Sembunyikan Pesan.
      - Pilih gambar dengan tombol Browse.
      - Masukkan pesan rahasia dan tentukan lokasi untuk menyimpan gambar baru.
      - Klik tombol Sembunyikan.
4. Menampilkan Pesan:
      - Klik tombol Tampilkan Pesan.
      - Pilih gambar dengan tombol Browse.
      - Klik tombol Tampilkan Pesan untuk melihat pesan yang tersembunyi.
