def hitung_berat(tinggi,bmi_harapan) :
    berat = bmi_harapan * (tinggi ** 2)
    return berat

def kategori_berat(bmi) :
    if bmi < 18.5 :
        return "Kurus"
    elif 18.5 <= bmi < 24.9:
        return "Normal"
    elif 24.9 <= bmi < 29.9 :
        return "Gemuk"
    else:
        return "Obesitas"
    
def bmi_hasil(berat, tinggi):
    bmi = berat_diperlukan / (tinggi ** 2) 
    return bmi

tinggi = float(input("Tinggi(dalam meter)): "))
bmi_harapan =float(input("BMI yang diharapan : "))


berat_diperlukan = hitung_berat(tinggi, bmi_harapan)
bmi = bmi_hasil(berat_diperlukan, tinggi)
kategori = kategori_berat(bmi_harapan)


print("Berat yang diperlukan :", berat_diperlukan, "kg")
print("BMI yyang sesuai:", bmi)
print("Kategori berat badan:", kategori)


