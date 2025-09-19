print ("soal 1 : marathon netflix series")

jumlah_episode = int(input("masukkan jumlah episode : "))
durasi_per_episode = int(input("masukkan durasi per episode (menit):"))

total_menit=jumlah_episode*durasi_per_episode
total_jam=total_menit/60

print("total waktu menonton =",total_menit, "menit =", total_jam, "jam")

print("="*100)

print("soal 2 : sisa uang beli cupang dan koi")

jumlah_uang = int(input("masukkan jumlah uang yang dibawa (Rp) : "))

harga_cupang = 10000
harga_koi = 20000

jumlah_cupang = int(input("masukkan jumlah ikan cupang yang dibeli : "))
jumlah_koi = int(input("masukkan jumlah ikan koi yang dibeli : "))

total_harga = (jumlah_cupang*harga_cupang) + (jumlah_koi*harga_koi)
sisa_uang = jumlah_uang - total_harga

print("total belanja ikan (Rp) =", total_harga)
print("sisa uang (Rp) =", sisa_uang, )

print("="*100)

print("soal no 3 : pergi liburan dengan sepeda motor ")

jarak=float(input("masukkan total jarak perjalanan (KM): "))
konsumsi = float(input("masukkan konsumsi BBM sepeda motor (KM per liter):"))
kapasitas_tangki = float(input("masukkan kapasitas tangki motor (liter): "))
harga_bensin = float(input("masukkan harga bensin per liter (Rp): "))

bensin_dibutuhkan = jarak/konsumsi

if bensin_dibutuhkan > 3 :     
    harga_diskon_bensin = harga_bensin - 500
else : 
    harga_diskon_bensin = harga_bensin

total_biaya = harga_diskon_bensin*bensin_dibutuhkan

jumlah_isi_bensin = bensin_dibutuhkan/kapasitas_tangki
import math
isi_bensin = math.ceil(bensin_dibutuhkan /kapasitas_tangki )

print (f"ntotal jarak perjalanan (KM) = {jarak}")
print(f"kapasitas tangki (Liter) = {kapasitas_tangki}")
print(f"bensin dibutuhkan (Liter) = {round(bensin_dibutuhkan,2)}")
print(f"harga bensin per liter = {harga_diskon_bensin}")
print(f"total biaya bensin (Rp) = {total_biaya}")
print(f"isi bensin sekitar = {isi_bensin} kali")