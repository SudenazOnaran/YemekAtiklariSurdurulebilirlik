corba_malzeme_listesi = {}
anayemek_malzeme_listesi = {}
tatli_malzeme_listesi = {}

while True:
    corba_adi = input("Çorba adını girin (Çıkmak için 'q' tuşuna basın): ")
    if corba_adi == "q":
        break

    while True:
        malzeme_corba = input(f"{corba_adi} için kullanılan malzemeleri girin (Çıkmak için 'q' tuşuna basın): ")
        if malzeme_corba == "q":
            break
        miktar_corba = float(input("Miktarını girin: "))
        birim_corba = input("Malzeme birimini girin (örn. 'ml', 'gram'): ")
        corba_malzeme_listesi[malzeme_corba] = (miktar_corba, birim_corba)

    print(f"\n{corba_adi} Malzeme Listesi:")
    for malzeme, (miktar, birim) in corba_malzeme_listesi.items():
        print(f"{malzeme}: {miktar} {birim}")

    porsiyon_sayisi = int(input(f"Günlük satılan {corba_adi} porsiyonu: "))

    # Haftalık malzeme miktarlarını hesapla
    print(f"\nHaftalık {corba_adi} Malzeme Miktarı:")
    for malzeme, (miktar, birim) in corba_malzeme_listesi.items():
        if birim == "ml":
            toplam_miktar = miktar * porsiyon_sayisi * 7
        elif birim == "gram":
            toplam_miktar = miktar * porsiyon_sayisi * 7 / 1000  # gramı kg'ye çevir
        print(f"{malzeme}: {toplam_miktar} {birim}")

while True:
    anayemek_adi = input("Ana yemek adını girin (Çıkmak için 'q' tuşuna basın): ")
    if anayemek_adi == "q":
        break

    while True:
        malzeme_anayemek = input(f"{anayemek_adi} için kullanılan malzemeleri girin (Çıkmak için 'q' tuşuna basın):")
        if malzeme_anayemek == "q":
            break
        miktar_anayemek = float(input("Miktarını girin:"))
        birim_anayemek = input("Malzeme birimini girin(örn. 'gram' , 'adet'): ")
        anayemek_malzeme_listesi[malzeme_anayemek] = (miktar_anayemek, birim_anayemek)

    print(f"\n{anayemek_adi} Malzeme Listesi:")
    for malzeme, (miktar, birim) in anayemek_malzeme_listesi.items():
        print(f"{malzeme}: {miktar} {birim}")

    porsiyon_sayisi_anayemek = int(input(f"Günlük satılan {anayemek_adi} porsiyonu: "))

    # Haftalık ana yemek malzeme miktarlarını hesapla
    print(f"\nHaftalık {anayemek_adi} Malzeme Miktarı")
    for malzeme, (miktar, birim) in anayemek_malzeme_listesi.items():
        if birim == "gram":
            toplam_miktar = miktar * porsiyon_sayisi_anayemek * 7 / 1000  # gramı kg'ye çevir
        elif birim == "adet":
            toplam_miktar = miktar * porsiyon_sayisi_anayemek * 7
        print(f"{malzeme}: {toplam_miktar} {birim}")

while True:
    tatli_adi = input("Tatlı adını girin (Çıkmak için 'q' tuşuna basın): ")
    if tatli_adi == "q":
        break

    while True:
        malzeme_tatli = input(f"{tatli_adi} için kullanılan malzemeleri girin (Çıkmak için 'q' tuşuna basın):")
        if malzeme_tatli == "q":
            break
        miktar_tatli = float(input("Miktarını girin:"))
        birim_tatli = input("Malzeme birimini girin(örn. 'gram' , 'adet'): ")
        tatli_malzeme_listesi[malzeme_tatli] = (miktar_tatli, birim_tatli)

    print(f"\n{tatli_adi} Malzeme Listesi")
    for malzeme, (miktar, birim) in tatli_malzeme_listesi.items():
        print(f"{malzeme}: {miktar} {birim}")

    porsiyon_sayisi_tatli = int(input(f"Günlük satılan {tatli_adi} porsiyonu: "))

    # Haftalık tatlı malzeme miktarlarını hesapla
    print(f"\nHaftalık {tatli_adi} Malzeme Miktarı")
    for malzeme, (miktar, birim) in tatli_malzeme_listesi.items():
        if birim == "gram":
            toplam_miktar = miktar * porsiyon_sayisi_tatli * 7 / 1000  # gramı kg'ye çevir
        elif birim == "adet":
            toplam_miktar = miktar * porsiyon_sayisi_tatli * 7
        print(f"{malzeme}: {toplam_miktar} {birim}")

