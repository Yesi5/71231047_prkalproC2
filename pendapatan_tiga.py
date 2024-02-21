def hitung_pendapatan(gaji_per_jam, jam_kerja_per_minggu):
    pendapatan_sebelum_pajak = gaji_per_jam * jam_kerja_per_minggu * 5
    pajak = 0.14 * pendapatan_sebelum_pajak
    pendapatan_setelah_pajak = pendapatan_sebelum_pajak - pajak
    belanja_pakaian_aksesoris = 0.10 * pendapatan_setelah_pajak
    belanja_alat_tulis = 0.01 * pendapatan_setelah_pajak
    sisa_uang = pendapatan_setelah_pajak - belanja_pakaian_aksesoris - belanja_alat_tulis
    sedekah = 0.25 * sisa_uang
    sedekah_anak_yatim = 0.30 * sedekah
    sedekah_dhuafa = sedekah - sedekah_anak_yatim
    
    return pendapatan_sebelum_pajak, pendapatan_setelah_pajak, belanja_pakaian_aksesoris, belanja_alat_tulis, sedekah, sedekah_anak_yatim, sedekah_dhuafa

gaji_per_jam = float(input("Masukkan gaji per jam yang Anda inginkan: "))
jam_kerja_per_minggu = int(input("Masukkan jumlah jam kerja per minggu: "))

pendapatan_sebelum_pajak, pendapatan_setelah_pajak, belanja_pakaian_aksesoris, belanja_alat_tulis, sedekah, sedekah_anak_yatim, sedekah_dhuafa = hitung_pendapatan(gaji_per_jam, jam_kerja_per_minggu)

print("1. Pendapatan Budi selama liburan musim panas sebelum pembayaran pajak: Rp.", pendapatan_sebelum_pajak)
print("2. Pendapatan Budi selama liburan musim panas setelah pembayaran pajak: Rp.", pendapatan_setelah_pajak)
print("3. Jumlah uang yang akan Budi habiskan untuk membeli pakaian dan aksesoris: Rp.", belanja_pakaian_aksesoris)
print("4. Jumlah uang yang akan Budi habiskan untuk membeli alat tulis: Rp.", belanja_alat_tulis)
print("5. Jumlah uang yang akan Budi sedekahkan: Rp.", sedekah)
print("6. Jumlah uang yang akan Budi terima anak yatim: Rp.", sedekah_anak_yatim)
print("7. Jumlah uang yang akan Budi terima kaum dhuafa: Rp.", sedekah_dhuafa)