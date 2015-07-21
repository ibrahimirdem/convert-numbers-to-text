import math

def ucHaneOku(sayi):
    birler = {"0":"","1":"Bir","2":"Iki","3":"Uc","4":"Dort","5":"Bes","6":"Alti","7":"Yedi","8":"Sekiz","9":"Dokuz"}
    onlar = {"1":"On","2":"Yirmi","3":"Otuz","4":"Kirk","5":"Elli","6":"Altmis","7":"Yetmis","8":"Seksen","9":"Doksan","0":""}
    yuz = ["Yuz",]

    if len(sayi) == 3:
        if sayi[0] == "1":
            oku = yuz[0]+onlar[sayi[1]]+birler[sayi[2]]
            return oku
        if sayi[0] == "0":
            oku = onlar[sayi[1]]+birler[sayi[2]]
            return oku
        else:
            oku = birler[sayi[0]]+yuz[0]+onlar[sayi[1]]+birler[sayi[2]]
            return oku
    if  len(sayi) == 1:
        if sayi[0] == "0":
            oku = "Sifir"
            return oku
        else:
            oku = birler[sayi[0]]
            return oku
    if len(sayi) == 2:
        oku = onlar[sayi[0]]+birler[sayi[1]]
        return oku



sayi  = raw_input("Sayiyi Giriniz :")
basaSifirEkle = len(sayi)%3
if basaSifirEkle == 1:
    sayi = "00"+sayi
elif basaSifirEkle == 2:
    sayi = "0"+sayi
else:
    sayi = sayi

kacYuzlerVar =  math.ceil(int(len(sayi))/3.0)
ucluGrub = {"0":"","1":"Bin","2":"Milyon","3":"Milyar","4":"Trilyon","5":"Katrilyon"}

oku = ""
for i in range(int(kacYuzlerVar)):
    if sayi[-1*((i*3)+3)]+sayi[-1*((i*3)+2)]+sayi[-1*((i*3)+1)] == "000":
        oku = oku
    elif sayi[-1*((i*3)+3)]+sayi[-1*((i*3)+2)]+sayi[-1*((i*3)+1)] == "001" and len(sayi) == 6:
        oku = ucluGrub[str(i)] + oku
    else:
        oku = ucHaneOku(sayi[-1*((i*3)+3)]+sayi[-1*((i*3)+2)]+sayi[-1*((i*3)+1)]) + ucluGrub[str(i)] + oku

print oku
