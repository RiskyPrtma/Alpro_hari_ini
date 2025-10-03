# Tugas 2 
print("Program Menentukan Kode Produk")
print("Keterangan Kode : ")
print("Kode jenis produk --> b (baju), c (celana)")
print("Kode jenis produk --> m (merah), h (hitam)")

produk = input("Masukan kode produk : ")
warna_produk = input("Masukan kode warna : ")

pilihan_produk = ""
pilihan_warna_produk = ""


if produk == "b":
 pilihan_produk = "Baju"
elif produk == "c":
 pilihan_produk = "Celana"

if warna_produk == "m":
 pilihan_warna_produk = "Merah"
elif warna_produk == "h":
 pilihan_warna_produk = "Hitam"

if produk != "b" and produk != "c":
 print("Kode Produk yang anda masukan salah")
elif warna_produk != "m" and warna_produk != "h":
 print("kode Warna produk yang anda masukan salah")
else :
 print(pilihan_produk + " berwarna " + pilihan_warna_produk) 

