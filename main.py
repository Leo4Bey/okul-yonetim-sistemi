import json

def ogrenci_giris():
    print("***** Öğrenci Sistemi *****")
    no = int(input("Öğrenci Numarınızı Giriniz: "))
    with open('ogrenci.json', 'r+') as f:
        ogrenci = json.load(f)

    ogrencimi = False

    for ogrenci_id in ogrenci['ogrenci']:
        if no == ogrenci_id['no']:
            ogrencimi = True
            break

    if not ogrencimi:
        print("numara kayıtlı değil")
        print("Hatalı numara girildiği için sistem kapatılıyor")
    elif ogrencimi:
        sifre = input("Şifrenizi Giriniz: ")
        if sifre != ogrenci_id['sifre']:
            print("Yanlış şifre girdiğiniz için program kapanıyor")
        elif sifre == ogrenci_id['sifre']:
            print("***** Öğrenci Sistemi *****")
            print("1. Notlarını Görüntüle")
            print("2. Devamsızlık Bilgisini Görüntüle")
            print("3. Ana Menüye Dön")
            print("***** Öğrenci Sistemi *****")
            choice = input("Seçiminiz (1/2/3): ")

            if choice == "1":
                print(f"Matematik: {ogrenci_id['mat']}")
                print(f"Fen: {ogrenci_id['fen']}")
                ortalama = (ogrenci_id['fen'] + ogrenci_id['mat']) / 2
                print(f"ortalama: {ortalama}")
            elif choice == "2":
                print(f"Devamsızlık {ogrenci_id['devamsizlik']} gün")
            elif choice == "3":
                ana_menu()
            else: 
                print("Hatalı işlem yaptınız uygulama öğrenci giriş ekranına yönlendirildi")
                ogrenci_giris()


def yonetici_giris():
    print("***** Yönetici Sistemi *****")
    tc = int(input("TC Kimlik Numaranızı Giriniz: "))
    sifre = input("Şirenizi Giriniz: ")
    with open('yonetici.json', 'r+') as f:
        yonetici = json.load(f)

    yoneticimi = False

    for yonetici_bilgi in yonetici['yonetici']:
        if tc == yonetici_bilgi['tc'] and sifre == yonetici_bilgi['sifre']:
            yoneticimi = True
            break

    if not yoneticimi:
        print("Yanlış TC Kimlik Numarası ya da Yanlış Şifre girdiniz\nLütfen bilgilerininizi kontrol edip tekrar deneyiniz.")
    elif yoneticimi:
        print(f"Hoş geldin {yonetici_bilgi['ad']}\n")
        print("***** Yönetici Sistemi *****")
        print("1. Kayıtlı Olan Öğrenciyi Görüntüle")
        print("2. Yeni Bir Öğrenci Ekle")
        print("3. Kayıtlı Olan Öğrenciyi Sil")
        print("4. Çıkış Yap")
        print("***** Yönetici Sistemi *****")
        choice = input("Seçiminiz (1/2/3/4): ")

        if choice == "1":
            no = int(input("Öğrencinin Numarasını Giriniz: "))
            with open('ogrenci.json', 'r+') as f:
                ogrenci = json.load(f)

            ogrencimi = False

            for ogrenci_id in ogrenci['ogrenci']:
                if no == ogrenci_id['no']:
                    ogrencimi = True
                    break

            if not ogrencimi:
                print("numara kayıtlı değil")
                print("Hatalı numara girildiği için sistem kapatılıyor")
            elif ogrencimi:
                ortalama = (ogrenci_id['fen'] + ogrenci_id['mat']) / 2 
                print("\n***** Öğrenci Bilgi *****")
                print(f"Öğrencinin Adı: {ogrenci_id['ad']}")
                print(f"Öğrencinin Sınıfı: {ogrenci_id['sinif']}")
                print(f"Öğrencinin Numarası: {ogrenci_id['no']}")
                print(f"Öğrencinin Not Ortalaması: {ortalama}")
                print(f"Öğrencinin Devamsızlık Bilgisi: {ogrenci_id['devamsizlik']} Gün")
                print("***** Öğrenci Bilgi *****")
        elif choice == "2":
            print("\n Kayıt edilecek öğrenci ile ilgili bilgileri doldurunuz.")
            no = int(input("Öğrenci No: "))
            with open('ogrenci.json', 'r+') as f:
                ogrenci = json.load(f)

            ogrencimi = False

            for ogrenci_id in ogrenci['ogrenci']:
                if no == ogrenci_id['no']:
                    ogrencimi = True
                    break

            if ogrencimi:
                print("Bu numara zaten bir öğrenci tarafından kullanılıyor.")
            elif not ogrencimi:
                sifre = input("Şifre Belirleyiniz: ")
                ad = input("Öğrencinin Adını Giriniz: ")
                mat = int(input("Öğrencinin Matematik Notunu Giriniz: "))
                fen = int(input("Öğrencinin Fen Notunu Giriniz: "))
                devamsizlik = int(input("Öğrencinin Devamsızlık Sayısını Giriniz: "))
                sinif = input("Öğrencinin Sınıfını Giriniz: ")
                print("Girdiğiniz veriler öğrencinin datasına kayıt ediliyor...")
                def write_json(new_data, filename="ogrenci.json"):
                    with open(filename, "r+", encoding='utf-8') as file:
                        file_data = json.load(file)
                        file_data["ogrenci"].append(new_data)
                        file.seek(0)
                        json.dump(file_data, file, indent=4)
                yeni_ogrenci = {"no": no,
                                "sifre": f"{sifre}",
                                "ad": f"{ad}",
                                "mat": mat,
                                "fen": fen,
                                "devamsizlik": devamsizlik,
                                "sinif": f"{sinif}"
                            }
                write_json(yeni_ogrenci)
                print(f"{ad} adlı öğrenci {no} numarası ile dataya kayıt edildi")
        elif choice == "3":
            print("\n Kaydı Silinecek Olan Öğrencinin No'sunu giriniz.")
            no = int(input("Öğrenci No: "))
            with open('ogrenci.json', 'r+', encoding="utf-8") as f:
                data = json.load(f)

            ogrencimi = False

            for ogrenci_id in data['ogrenci']:
                if no == ogrenci_id['no']:
                    ogrencimi = True
                    break

            if not ogrencimi:
                print("Girdiğiniz No'lu bir öğrenci bulunamadı.")
            elif ogrencimi:
                print(f"{no} Nolu Öğrencinin verileri siliniyor...")
                data['ogrenci'] = [ogrenci for ogrenci in data['ogrenci'] if ogrenci['no'] != no]
                with open('ogrenci.json', 'w') as f:
                    json.dump(data, f, indent=4)
                print(f"Bay bay {ogrenci_id['ad']}")
                print(f"{no} Nolu Öğrencinin verileri silindi.")
        else: 
            print("Hatalı işlem yaptınız uygulama yönetici giriş ekranına yönlendirildi")
            yonetici_giris()



def ana_menu():
    while True:
        print("***** Okul Sistemi *****")
        print("1. Öğrenci Girişi")
        print("2. Yönetici Girişi")
        print("3. Uygulamayı Kapat")
        print("***** Okul Sistemi *****")
        choice = input("Seçiminiz (1/2/3): ")

        if choice == "1":
            ogrenci_giris()
            break
        elif choice == "2":
            yonetici_giris()
            break
        elif choice == "3":
            print("Uygulamadan çıkış yapılıyor\n")
            break
        else:
            print("Lütfen geçerli bir tuşa basınız.")

ana_menu()