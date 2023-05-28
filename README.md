# book_agreegation (Manajemen Toko Buku)

Program ini adalah sebuah aplikasi sederhana untuk manajemen toko buku. Program ini menggunakan konsep Aggregation dengan dua kelas utama, yaitu `Buku` dan `TokoBuku`. Setiap objek `TokoBuku` memiliki beberapa objek `Buku` yang merupakan daftar buku yang tersedia di toko tersebut.

## Kelas Buku

Kelas `Buku` memiliki atribut-atribut berikut:
- `judul`: string yang menyimpan judul buku.
- `pengarang`: string yang menyimpan nama pengarang buku.
- `harga`: integer atau float yang menyimpan harga buku.

## Kelas TokoBuku

Kelas `TokoBuku` memiliki atribut-atribut berikut:
- `nama`: string yang menyimpan nama toko buku.
- `buku`: list yang menyimpan objek-objek `Buku` yang tersedia di toko.

Selain atribut, kelas `TokoBuku` juga memiliki metode-metode berikut:
- `tambah_buku(buku)`: metode ini digunakan untuk menambahkan buku baru ke dalam daftar buku toko. Parameter `buku` merupakan objek `Buku` yang akan ditambahkan.
- `tampilkan_buku()`: metode ini digunakan untuk menampilkan daftar buku yang tersedia beserta informasi detailnya, seperti judul, pengarang, dan harga.

## Contoh Penggunaan

Berikut adalah contoh penggunaan program untuk mengelola toko buku:
![image](https://github.com/wahyupamungkas1/book_agreegation_wahyupamungkas/assets/129237250/0dc387b5-6567-4de4-9905-8a2356834788)

Output yang dihasilkan:
![image](https://github.com/wahyupamungkas1/book_agreegation_wahyupamungkas/assets/129237250/7f7fb350-c977-4c11-a87f-0329ce44b10b)
