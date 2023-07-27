
def kubus(sisi):
    volume = sisi**3
    return volume

def tabung(diameter,tinggi):
    r=diameter/2
    volume=(22/7*(r**2))*tinggi
    return volume

def balok(panjang,lebar,tinggi):
    volume=panjang*lebar*tinggi
    return volume

print("===============KALKULATOR CERDAS===============")
print('Pilihlah bangun yang ingin anda hitung(inputan angka saja) :')
print('1.Tabung')
print('2.Kubus')
print('3.balok')
pil=int(input('>>'))
if pil == 1:
    diameter=int(input("Masukan diameter (cm):"))
    tinggi=int(input("masukan tinggi :"))
    print(tabung(diameter,tinggi))
elif pil == 2:
    sisi=int(input('Masukkan sisi(cm) :'))
    print(kubus(sisi))
elif pil == 3:
    panjang=int(input("masukan panjang (cm) :"))
    lebar=int(input("masukan lebar (cm) :"))
    tinggi=int(input("masukan tinggi (cm) :"))
    print(balok(panjang,lebar,tinggi))
else:
    print('Inputan yang anda masukkan salah !!')



