jarak_berangkat = 100
jarak_pulang = 100
konsumsi = 40
bensin_tersedia = 1.5
harga_bensin = 10000

total_jarak_pp = jarak_berangkat + jarak_pulang
total_bensin = total_jarak_pp / konsumsi
total_bensin_yang_dibeli = total_bensin - bensin_tersedia
total_biaya_yang_dikeluarkan = total_bensin_yang_dibeli * harga_bensin

print("total jarak pp=", total_jarak_pp, "km")
print("total bensin=", total_bensin, "liter")
print("bensin yang harus dibeli=", total_bensin_yang_dibeli, "liter")
print("biaya beli bensin=Rp", total_biaya_yang_dikeluarkan, "Rp")

