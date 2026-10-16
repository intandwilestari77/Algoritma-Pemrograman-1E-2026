suhu = float(input("Suhu reaktor (Celcius): "))
tekanan = float(input("Tekanan gas (Bar): "))
print(f"Suhu: {suhu} C | Tekanan: {tekanan} Bar")

if suhu > 1000:
    if tekanan > 50:
        pesan = "MELTDOWN! SEGERA EVAKUASI!"
    else:
        pesan = "Bahaya Suhu: Segera Turunkan Daya!"
elif suhu > 500:
    if tekanan > 30:
        pesan = "Tekanan Tidak Stabil"
    else:
        pesan = "Operasi Reaktor Normal"
else:
    pesan = "Reaktor Belum Cukup Panas"
print(pesan)

print("Pompa Maksimal" if suhu > 800 else "Pompa Normal")

