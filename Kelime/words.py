import json
import random
import time

class Kelime():
    def __init__(self):
        self.durum= True
        self.veriler = self.kelimeleriAl
    
    def menu(self):
        self.menuGoster()
        secim = self.islemSec()
        if  secim == 1:
            self.kelimeCalis()
        if secim ==2:
            self.kelimeEkle()
        if secim==3:
            self.cikis()
         


    def menuGoster(self):
        print(
            """
1- Kelime Çalış 
2- Kelime Ekle 
3- Çıkış Yap
            """
        )
    def islemSec(self):
        while True:
            try:
                secim= int(input("Seçim Yapınız: "))
                while secim <1 or secim > 3:
                    secim=int(input("Hatalı Seçim. Lütfen 1 ile 3 Arasında Sayı Giriniz: "))
                break
            except:
                print("Hatalı Seçim. Lütfen 1 ile 3 Arasında Sayı Giriniz.")
                            
                
                
        return secim
    
    def kelimeleriAl(self):
        try:
            with open("kelimeler.json","r") as dosya:
                veriler = json.load(dosya)
        except FileNotFoundError:
            with open("kelimeler.json","w") as dosya:
                dosya.write("{}")
            with open("kelimeler.json","r") as dosya:
                veriler = json.load(dosya)
        
        return veriler    

    def kelimeEkle(self):
        tr_input=(input("Türkçe Kelimenizi Girin: "))
        en_input=input("İngilizce Karşılığını Girin: ")
        tr=tr_input.lower()
        en=en_input.lower()
        self.kelimeKaydet(tr,en)

    def kelimeKaydet(self,tr,en):
        self.veriler=self.kelimeleriAl()
        try:
            self.veriler["kelimeler"].append({"tr":tr,"en":en,})
        except KeyError:
            self.veriler["kelimeler"] = []
            self.veriler["kelimeler"].append({"tr":tr,"en":en,})
        with open("kelimeler.json","w") as dosya:
            json.dump(self.veriler,dosya)
            print("Kelime Eklendi. ")

    def kelimeCalis(self):
        self.veriler=self.kelimeleriAl()
        yeniListe={}
        tekrarSayi= 0
        while True:
            try:
                tekrar= int(input("Kaç Soru Sorulsun: "))
                while type(tekrar) == "int":
                    tekrar= int(input("Kaç Soru Sorulsun: "))
                break

            except:
                print("Hatalı Seçim. Lütfen Çalışmak İstediğiniz Kelime Sayını Giriniz.")
            
        dogruSayisi=0
        yanlisSayisi=0
        for kelime in self.veriler["kelimeler"]:
            yeniListe[kelime["tr"]]=kelime["en"]
        while True: 
              
            tr,en=(random.choice(list(yeniListe.items())))
            enCevap=input("{} kelimesinin ingilizce karşılığı nedir? ".format(tr))
            if en == enCevap:
                print("Cevap Doğru")
                
                time.sleep (0.3)
                dogruSayisi +=1
                tekrarSayi +=1
                print("Mevcut Doğru Sayısı: {}, Yanlış Sayısı: {}".format(dogruSayisi,yanlisSayisi))
                if tekrarSayi == tekrar:
                    break
            else:
                print("Cevap Yanlış")
                
                time.sleep (0.3)
                yanlisSayisi+=1
                tekrarSayi +=1
                print("Mevcut Doğru Sayısı: {}, Yanlış Sayısı: {}".format(dogruSayisi,yanlisSayisi))
                if tekrarSayi == tekrar :
                    break

        
        
            
               




    def cikis(self):
            self.durum= False
            



kelime= Kelime()

while kelime.durum:
    kelime.menu()

