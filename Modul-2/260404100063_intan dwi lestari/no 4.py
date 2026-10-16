pin = int(input("Masukkan PIN 3 digit: "))
jam = int(input("Jam kedatangan (0-23): "))

d1 = pin // 100
d2 = (pin // 10) % 10
d3 = pin % 10
print(f"Digit PIN: {d1}, {d2}, {d3}")

if pin % 5 == 0:
    if jam < 12:
        pesan = "Garasi Pagi Terbuka"
    else:
        pesan = "Garasi Malam Terbuka, Lampu Dinyalakan"
elif pin % 2 == 0:
    if d1 + d3 == d2:
        pesan = "Garasi VIP Terbuka Khusus Bos"
    else:
        pesan = "Kode Genap Ditolak, Alarm Berbunyi!"
else:
    pesan = "Akses Ditolak"
print(pesan)
#memakai ternary
print("Mode Malam Merekam" if jam > 18 else "Mode Siang Standby")


