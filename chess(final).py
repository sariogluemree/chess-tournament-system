import math
ELO_MIN = 1000 #elo alt sınırı
UKD_MIN = 1000 #ukd alt sınırı
ELOSUZ = 0 #elosu olmayan kişinin elosu
UKDSIZ = 0 #ukdsi olmayan oyuncu ukdsi
LNO_MIN = 1 #lno alt sınır
VARSAYILAN_DEGER = 0 #ilk değerlerini açıldıktan sonra alacak bazı değişkenler için default değer
LOG_TABANI = 2 #logaritma fonksitonun tabanı
MOD2BOLENI = 2 #sayının çift mi tek mi olduğu
EB_PUAN_CARPANI = 0.5 #eşitlik bozma sistemleri için tur atlama durumlarında hesaplamada kullanılacak çarpan
RENK_SINIR = 2 #aynı renkli iki rakip için eşleşmeyi önleyen renk sınırı
KAZANAN_PUANI = 1 #kazanan oyuncuya eklenecek puan
BERABERLIK_PUANI = 0.5 #berabere kalan oyunculara eklenecek puan
SB2BOLENI = 2 #sb hesaplanırken kullanılacak bölen
TUR_VERI_SAYISI = 3 #her tur için tutulacak veri sayısı (tur bilgileri:rakip bsno, taş rengi, masa sonucu için)

def oyuncu_al(oyuncular): #Tüm oyuncu bilgilerinin alınıp oyuncular dict'inin oluşturulduğu fonksiyon
    while True:
        lno = int(input("Oyuncunun lisans numarasını giriniz: "))
        while str(lno) in oyuncular: #lno'nun tekil olma zorunluluğuna uygun giriş yapılıp yapılmadığının kontrolü
            lno = int(input("Oyuncunun lisans numarasını giriniz: "))
        if lno < LNO_MIN:
            break
        ad_soyad = input("Oyuncunun adını soyadını giriniz: ")
        elo = int(input("Oyuncunun ELO puanını giriniz: "))
        while elo < ELO_MIN and elo != ELOSUZ: #uygun giriş yapılıp yapılmadığının kontrolü
            elo = int(input("Oyuncunun ELO puanını giriniz: "))
        ukd = int(input("Oyuncunun UKD puanını giriniz: "))
        while ukd < UKD_MIN and ukd != UKDSIZ: #uygun giriş yapılıp yapılmadığının kontrolü
            ukd = int(input("Oyuncunun UKD puanını giriniz: "))

        puan = VARSAYILAN_DEGER #Oyuncunun başlangıç puanı
        rakipler = [] #Oyuncunun karşılaştığı rakipler listesi
        bye = False #Oyuncunun o turda bye geçip geçmeyeceği durumu
        ayni_renk_say = VARSAYILAN_DEGER #Oyuncunun aynı rengi üst üste kaç kere aldığı
        renk_farki = VARSAYILAN_DEGER #Oyuncunun bir rengi diğerinden ne kadar fazla aldığı
        eslesme = False #Oyuncunun o turda eşleşip eşleşmediği
        bsno = None #Oyuncunun başlangıç sıra numarası
        renkler = [] #Oyuncunun turnuva boyunca aldığı renkler
        yendikleri = [] #Oyuncunun yendiği rakipler listesi
        berabere_kaldiklari = [] #Oyuncunun berabere kaldığı rakipler listesi
        gs = VARSAYILAN_DEGER #Eşitlik bozma sistemlerinden gs puanı
        rakiplerinin_puanlari = [] #!!! KULLANILMIYOR KODDAN ÇIKARILACAK!!!
        bh1 = VARSAYILAN_DEGER #Eşitlik bozma sistemlerinden bh1 puanı
        bh2 = VARSAYILAN_DEGER #Eşitlik bozma sistemlerinden bh2 puanı
        sb = VARSAYILAN_DEGER #Eşitlik bozma sistemlerinden sb puanı
        lno = str(lno)
        mustbye = False #Oyuncunun rakibi gelmemesi durumu ile tur atlayıp atlamadığı
        eb_tur_atlayan = VARSAYILAN_DEGER #Eşitlik bozma sistemleri için rakibinin gelmediği ya da tur atladığı turlar için eklenecek puan
        turlar = [] #Oyuncunun turnuva boyunca tur bilgilerini tutan liste (tur bilgileri:rakip bsno, taş rengi, masa sonucu)
        sno = None #Oyuncunun turnuva sonu başarı sıralaması
        oyuncular[lno] = [ad_soyad,elo,ukd,puan,rakipler,bye,ayni_renk_say,renk_farki,eslesme,bsno,renkler,yendikleri,berabere_kaldiklari,gs,rakiplerinin_puanlari,bh1,bh2,sb,mustbye,eb_tur_atlayan,turlar,sno]
    return oyuncular

def oyuncu_sırala(oyuncular): #oyuncular dict'ini puan, elo, ukd, ad_soyad(alfabetik), lno öncelik sırası ile sıralayan ve bu dict'i oyuncu_listesi olarak döndüren fonksiyon
    oyuncular = dict(sorted(oyuncular.items(), key=lambda oyuncu: oyuncu[0]))
    oyuncular = dict(sorted(oyuncular.items(), key = lambda oyuncu: (oyuncu[1][0]), reverse = False))
    oyuncu_listesi = sorted(oyuncular.items(), key = lambda oyuncu: (oyuncu[1][3],oyuncu[1][1],oyuncu[1][2]), reverse = True)
    return oyuncu_listesi

def bsno_ver(oyuncu_say,oyuncular,oyuncu_listesi): #oyunculara oyuncu_listesi'ndeki sıraya göre başlangıç sıra numarası veren fonksiyon
    for i in range(oyuncu_say):
        bsno = i+1
        oyuncular[oyuncu_listesi[i][0]][9] = bsno
    return oyuncular    

def baslangic_sıra_listesi_olustur(oyuncu_say,oyuncu_listesi): #oyuncuları başlangıç sıra numaralarına göre sıralayan bir tablo yazdıran fonksiyon
    print("BSNo  LNo    Ad-Soyad     ELO    UKD ")
    print("----  ---  ------------  -----  -----")
    for i in range(oyuncu_say):
        print(format(oyuncu_listesi[i][1][9], "4d"), end = "  ")
        print(format(oyuncu_listesi[i][0], "3"), end = "  ")
        print(format(oyuncu_listesi[i][1][0], "12"), end = "  ")
        print(format(oyuncu_listesi[i][1][1], "5d"), end = "  ")
        print(format(oyuncu_listesi[i][1][2], "5d"))

def tur_sayisi_belirle(oyuncu_say): #kullanıcıdan tur sayısı alan fonksiyon
    tur_sayisi = int(input("\nTurnuvadaki tur sayısını giriniz:"))
    tur_alt_sinir = math.ceil(math.log(oyuncu_say,LOG_TABANI))
    if tur_alt_sinir - 1 == math.log(tur_sayisi,LOG_TABANI): #oyuncu sayısının 2 tabanındaki logaritmasının tam sayı olma durumunda üste yuvarlanmaması için istisna durum kontrolü
        tur_alt_sinir -= 1
    tur_ust_sinir = oyuncu_say - 1
    while tur_sayisi < tur_alt_sinir or tur_sayisi > tur_ust_sinir: #oyuncu sayısına göre belirlenen alt sınır ve üst sınıra uygun girdi yapılıp yapılmadığının kontrolü
        tur_sayisi = int(input("\nTurnuvadaki tur sayısını giriniz:"))
    return tur_sayisi

def ilk_renk_ataması(oyuncular,oyuncu_listesi,oyuncu_say): #turnuvanın ilk turu için başlangıç sıra numarası 1 olan oyuncu için kullanıcıdan renk alan fonksiyon (bsno tek olanlar 1. ile aynı rengi, çift olanlar karşı rengi alır)
    renk = input("\nBSNo 1 için ilk tur tarafını giriniz (beyaz:b/siyah:s): ")
    while renk not in ["b","s"]:
        renk = input("\nBSNo 1 için ilk tur tarafını giriniz (beyaz:b/siyah:s): ")
    if renk == "b":
        karsi_renk = "s"
    else:
        karsi_renk = "b"    
    for i in range(oyuncu_say):
        if oyuncular[oyuncu_listesi[i][0]][9] % MOD2BOLENI != 0: #oyuncunun başlangıç sıra numarasının tek olma durumu
            oyuncular[oyuncu_listesi[i][0]][10].append(karsi_renk)
        else: #oyuncunun başlangıç sıra numarasının çift olma durumu
            oyuncular[oyuncu_listesi[i][0]][10].append(renk)
    return oyuncular        

def bye_ata(oyuncu_say,oyuncular,oyuncu_listesi,bye_gecenler,tur,tur_sayisi): #oyuncu sayısının tek olduğu durumda hangi oyuncunun bye alacağını bulan ve bye alan oyuncunun bazı verilerini güncelleyen fonksiyon
    if oyuncu_say % 2 != 0:
        for i in range(oyuncu_say):
            if oyuncu_listesi[oyuncu_say-(i+1)][0] not in bye_gecenler and oyuncular[oyuncu_listesi[oyuncu_say-(i+1)][0]][18] == False: #oyuncunun daha önceden tur atlayıp atlamadığının kontrolü
                bye_gecenler.append(oyuncu_listesi[oyuncu_say-(i+1)][0])
                oyuncular[oyuncu_listesi[oyuncu_say-(i+1)][0]][19] = (tur_sayisi - (tur+1)) * EB_PUAN_CARPANI + oyuncular[oyuncu_listesi[oyuncu_say-(i+1)][0]][3]
                oyuncular[oyuncu_listesi[oyuncu_say-(i+1)][0]][3] += 1
                oyuncular[oyuncu_listesi[oyuncu_say-(i+1)][0]][5] = True
                oyuncular[oyuncu_listesi[oyuncu_say-(i+1)][0]][10].append(None)
                oyuncular[oyuncu_listesi[oyuncu_say-(i+1)][0]][20].append("-")
                oyuncular[oyuncu_listesi[oyuncu_say-(i+1)][0]][20].append("-")
                oyuncular[oyuncu_listesi[oyuncu_say-(i+1)][0]][20].append("1")
                break
    return bye_gecenler,oyuncular        

def eslestirme_yap(oyuncu_say,oyuncular,oyuncu_listesi,puanlar,masalar,masa_no): #oyuncular için kriterleri sağlayan en uygun rakibi bulup sırası ile masaya yerleştirerek eşleştirme yapan fonsksiyon
    for i in range(oyuncu_say-1):
        if oyuncular[oyuncu_listesi[i][0]][8]==False and oyuncular[oyuncu_listesi[i][0]][5]==False: #rakip aranan oyuncunun bu tur içinde eşleşmemiş ve bye geçmeyecek olması durumu
            
            m=VARSAYILAN_DEGER
            ind = None
            while ind == None:
                if oyuncular[oyuncu_listesi[i][0]][3] == puanlar[m]: #rakip aranan oyuncunun puanının puanlar listesindeki indisini bulma
                    ind = m
                else:
                    m += 1
            
            while ind<len(puanlar) and oyuncular[oyuncu_listesi[i][0]][8]==False: #indisin aşılmamış ve oyuncunun eşleşmemiş olmasının kontrolü
                rakipler = [j for j in range(i+1, oyuncu_say) if oyuncular[oyuncu_listesi[j][0]][8]==False and oyuncular[oyuncu_listesi[j][0]][5]==False and oyuncu_listesi[j][0] not in oyuncular[oyuncu_listesi[i][0]][4] and oyuncular[oyuncu_listesi[j][0]][3] == puanlar[ind]]
                #bu tur içinde eşleşmemiş, bu tur bye geçmeyecek, daha önceden rakip aranan oyuncunun rakibi olmamış, rakip aranan oyuncuyla öncelikle aynı puan grubunda olan (eğer bulunamazsa bir alt puan grubundan devam ederek ilerleyen) oyuncuların listesi
                for j in rakipler:
                    if oyuncular[oyuncu_listesi[j][0]][10][-1] == None: #aranan rakibin bir önceki tur bye geçmiş olduğu durum eşleşmesi
                        if oyuncular[oyuncu_listesi[j][0]][10][-2] != oyuncular[oyuncu_listesi[i][0]][10][-1]: #oyuncuların son aldıkları rengin farklı olduğu durum eşleşmesi
                            if oyuncular[oyuncu_listesi[i][0]][10][-1] == "b":
                                oyuncular[oyuncu_listesi[i][0]][10].append('s')
                                oyuncular[oyuncu_listesi[i][0]][6] = 1
                                oyuncular[oyuncu_listesi[i][0]][7] -= 1
                                oyuncular[oyuncu_listesi[j][0]][10].append('b')
                                oyuncular[oyuncu_listesi[j][0]][6] = 1
                                oyuncular[oyuncu_listesi[j][0]][7] += 1
                                masalar[f'{masa_no}.Masa'] = [oyuncu_listesi[j][0], oyuncu_listesi[i][0]]      #1.1 eşleşmesinin yapılması
                            else:
                                oyuncular[oyuncu_listesi[i][0]][10].append("b")
                                oyuncular[oyuncu_listesi[i][0]][6] = 1
                                oyuncular[oyuncu_listesi[i][0]][7] += 1
                                oyuncular[oyuncu_listesi[j][0]][10].append("s")
                                oyuncular[oyuncu_listesi[j][0]][6] = 1
                                oyuncular[oyuncu_listesi[j][0]][7] -= 1
                                masalar[f'{masa_no}.Masa'] = [oyuncu_listesi[i][0], oyuncu_listesi[j][0]]
                            oyuncular[oyuncu_listesi[i][0]][8] = True
                            oyuncular[oyuncu_listesi[i][0]][4].append(oyuncu_listesi[j][0])
                            oyuncular[oyuncu_listesi[j][0]][8] = True
                            oyuncular[oyuncu_listesi[j][0]][4].append(oyuncu_listesi[i][0])
                            masa_no += 1
                            break
                    
                    elif oyuncular[oyuncu_listesi[i][0]][10][-1] == None: #rakip aranan oyuncunun bir önceki tur bye geçmiş olduğu durum eşleşmesi
                        if oyuncular[oyuncu_listesi[j][0]][10][-1] != oyuncular[oyuncu_listesi[i][0]][10][-2]: #oyuncuların son aldıkları rengin farklı olduğu durum eşleşmesi
                            if oyuncular[oyuncu_listesi[j][0]][10][-1] == "b":
                                oyuncular[oyuncu_listesi[j][0]][10].append('s')
                                oyuncular[oyuncu_listesi[j][0]][6] = 1
                                oyuncular[oyuncu_listesi[j][0]][7] -= 1
                                oyuncular[oyuncu_listesi[i][0]][10].append('b')
                                oyuncular[oyuncu_listesi[i][0]][6] = 1
                                oyuncular[oyuncu_listesi[i][0]][7] += 1
                                masalar[f'{masa_no}.Masa'] = [oyuncu_listesi[i][0], oyuncu_listesi[j][0]]      #1.1 eşleşmesinin yapılması
                            else:
                                oyuncular[oyuncu_listesi[j][0]][10].append("b")
                                oyuncular[oyuncu_listesi[j][0]][6] = 1
                                oyuncular[oyuncu_listesi[j][0]][7] += 1
                                oyuncular[oyuncu_listesi[i][0]][10].append("s")
                                oyuncular[oyuncu_listesi[i][0]][6] = 1
                                oyuncular[oyuncu_listesi[i][0]][7] -= 1
                                masalar[f'{masa_no}.Masa'] = [oyuncu_listesi[j][0], oyuncu_listesi[i][0]]  
                            oyuncular[oyuncu_listesi[i][0]][8] = True
                            oyuncular[oyuncu_listesi[i][0]][4].append(oyuncu_listesi[j][0])
                            oyuncular[oyuncu_listesi[j][0]][8] = True
                            oyuncular[oyuncu_listesi[j][0]][4].append(oyuncu_listesi[i][0])
                            masa_no += 1
                            break
                    
                    else:
                        if oyuncular[oyuncu_listesi[j][0]][10][-1] != oyuncular[oyuncu_listesi[i][0]][10][-1]: #oyuncuların ikisinin de geçen el bye geçmediği ve son renklerinin farklı olduğu durum eşleşmesi
                            if oyuncular[oyuncu_listesi[i][0]][10][-1] == "b":
                                oyuncular[oyuncu_listesi[i][0]][10].append('s')
                                oyuncular[oyuncu_listesi[i][0]][6] = 1
                                oyuncular[oyuncu_listesi[i][0]][7] -= 1
                                oyuncular[oyuncu_listesi[j][0]][10].append('b')
                                oyuncular[oyuncu_listesi[j][0]][6] = 1
                                oyuncular[oyuncu_listesi[j][0]][7] += 1
                                masalar[f'{masa_no}.Masa'] = [oyuncu_listesi[j][0], oyuncu_listesi[i][0]]      #1.1 eşleşmesinin yapılması
                            else:
                                oyuncular[oyuncu_listesi[i][0]][10].append("b")
                                oyuncular[oyuncu_listesi[i][0]][6] = 1
                                oyuncular[oyuncu_listesi[i][0]][7] += 1
                                oyuncular[oyuncu_listesi[j][0]][10].append("s")
                                oyuncular[oyuncu_listesi[j][0]][6] = 1
                                oyuncular[oyuncu_listesi[j][0]][7] -= 1
                                masalar[f'{masa_no}.Masa'] = [oyuncu_listesi[i][0], oyuncu_listesi[j][0]]  
                            oyuncular[oyuncu_listesi[i][0]][8] = True
                            oyuncular[oyuncu_listesi[i][0]][4].append(oyuncu_listesi[j][0])
                            oyuncular[oyuncu_listesi[j][0]][8] = True
                            oyuncular[oyuncu_listesi[j][0]][4].append(oyuncu_listesi[i][0])
                            masa_no += 1
                            break

                if oyuncular[oyuncu_listesi[i][0]][8]==False: #oyuncunun hala eşleşmemiş olmasının kontrolü. bu eşleşmeye girildiyse oyuncular bir önceki tur aynı rengi almışlar demektir.
                    for j in rakipler:
                        if oyuncular[oyuncu_listesi[j][0]][6] < RENK_SINIR and abs(oyuncular[oyuncu_listesi[j][0]][7]) < RENK_SINIR: #aranan rakibin bir önceki turla aynı rengi alabilmesi için gerekli koşulların kontrolü
                            if oyuncular[oyuncu_listesi[i][0]][10][-1] == "b":
                                oyuncular[oyuncu_listesi[i][0]][10].append('s')
                                oyuncular[oyuncu_listesi[i][0]][6] = 1
                                oyuncular[oyuncu_listesi[i][0]][7] -= 1
                                oyuncular[oyuncu_listesi[j][0]][6] += 1
                                oyuncular[oyuncu_listesi[j][0]][7] += 1
                                masalar[f'{masa_no}.Masa'] = [oyuncu_listesi[j][0],oyuncu_listesi[i][0]]      #1.2 eşleşmesinin yapılması
                            else:
                                oyuncular[oyuncu_listesi[i][0]][10].append("b")
                                oyuncular[oyuncu_listesi[i][0]][6] = 1
                                oyuncular[oyuncu_listesi[i][0]][7] += 1
                                oyuncular[oyuncu_listesi[j][0]][6] += 1
                                oyuncular[oyuncu_listesi[j][0]][7] -= 1
                                masalar[f'{masa_no}.Masa'] = [oyuncu_listesi[i][0],oyuncu_listesi[j][0]] 
                            oyuncular[oyuncu_listesi[i][0]][8] = True
                            oyuncular[oyuncu_listesi[i][0]][4].append(oyuncu_listesi[j][0])
                            oyuncular[oyuncu_listesi[j][0]][8] = True
                            oyuncular[oyuncu_listesi[j][0]][4].append(oyuncu_listesi[i][0])
                            masa_no += 1
                            break

                if oyuncular[oyuncu_listesi[i][0]][8]==False: #oyuncunun hala eşleşmemiş olmasının kontrolü
                    if oyuncular[oyuncu_listesi[i][0]][6] < RENK_SINIR and abs(oyuncular[oyuncu_listesi[i][0]][7]) < RENK_SINIR: #rakip aranan oyuncunun bir önceki turla aynı rengi alabilmesi için gerekli koşulların kontrolü
                        if len(rakipler):
                            j = rakipler[0] #bu eşleşme koşuluna girilmişse rakipler listesindeki ilk kişiyi koşulsuz alabiliriz
                            if oyuncular[oyuncu_listesi[i][0]][10][-1] == "b":
                                oyuncular[oyuncu_listesi[i][0]][6] += 1
                                oyuncular[oyuncu_listesi[i][0]][7] += 1
                                oyuncular[oyuncu_listesi[j][0]][10].append('s')
                                oyuncular[oyuncu_listesi[j][0]][6] = 1
                                oyuncular[oyuncu_listesi[j][0]][7] -= 1
                                masalar[f'{masa_no}.Masa'] = [oyuncu_listesi[i][0],oyuncu_listesi[j][0]]      #1.3 eşleşmesinin yapılması
                            else:
                                oyuncular[oyuncu_listesi[i][0]][6] += 1
                                oyuncular[oyuncu_listesi[i][0]][7] -= 1
                                oyuncular[oyuncu_listesi[j][0]][10].append("b")
                                oyuncular[oyuncu_listesi[j][0]][6] = 1
                                oyuncular[oyuncu_listesi[j][0]][7] += 1
                                masalar[f'{masa_no}.Masa'] = [oyuncu_listesi[j][0],oyuncu_listesi[i][0]]
                            oyuncular[oyuncu_listesi[i][0]][8] = True
                            oyuncular[oyuncu_listesi[i][0]][4].append(oyuncu_listesi[j][0])
                            oyuncular[oyuncu_listesi[j][0]][8] = True
                            oyuncular[oyuncu_listesi[j][0]][4].append(oyuncu_listesi[i][0])
                            masa_no += 1
                ind += 1 #oyuncu kendi puan gurubundaki kimseyle eşleşemediğinden bir alt puan grubundaki rakipleri aramak için indisin arttırılması
    return oyuncular,masalar

def eslesme_tablosu_yap(tur,masalar,oyuncular,bye_gecenler): #masalara eşleştirilen oyuncuları masa sırasına göre bir tablo olarak yazdıran fonksiyon
    print(f"{tur+1}.Tur Eşleştirme Listesi")
    print("        Beyazlar         Siyahlar    ")
    print(" MNo   BSNo   LNo   Puan - Puan   LNo   BSNo")
    print("------ ----  -----  ----   ----  -----  ----")
    for masa in masalar:
        print(format(masa, "6"), end = " ")
        print(format(oyuncular[masalar[masa][0]][9], "4d"), end = "  ")
        print(format(masalar[masa][0], "5"), end = "  ")
        print(format(oyuncular[masalar[masa][0]][3], "4.2f"), end = " ")
        print("-", end = " ")
        print(format(oyuncular[masalar[masa][1]][3], "4.2f"), end = "  ")
        print(format(masalar[masa][1], "5"), end = "  ")
        print(format(oyuncular[masalar[masa][1]][9], "4d"))
    if len(bye_gecenler) != 0: #bye geçen oyuncu olup olmadığının kontrolü (bye geçen oyuncular ekstra bir masaya tek başlarına yazılırlar ve karşılarına BYE yazdırılır)
        print(format(f'{len(masalar)+1}.Masa', "6"), end = " ")
        print(format(oyuncular[bye_gecenler[-1]][9], "4d"), end = "  ")
        print(format(bye_gecenler[-1], "5"), end = "  ")
        print(format(oyuncular[bye_gecenler[-1]][3]-1, "4.2f"), end = " ")
        print("- BYE")



def masa_sonucu_al(tur,tur_sayisi,masalar,oyuncular): #her masa için kullanıcıdan girdi (0-5) alan ve oyuncu verilerini güncelleyen fonksiyon
    print("\n0: beraberlik, yani maç sonucu ½ - ½\n1: beyaz galip, yani maç sonucu 1 - 0\n2: siyah galip, yani maç sonucu 0 - 1\n3: siyah maça gelmemiş, yani maç sonucu + - -\n4: beyaz maça gelmemiş, yani maç sonucu - - +\n5: her iki oyuncu da maça gelmemiş, yani maç sonucu - - -")
    for masa in masalar:
        sonuc = input(f"{tur+1}. tur {masa} maç sonucunu giriniz: ")
        while sonuc not in ["0","1","2","3","4","5"]: #geçerli girdi girilip girilmediğinin kontrolü
            sonuc = input(f"{tur+1}. tur {masa} maç sonucunu giriniz: ")
        if sonuc == "0":
            oyuncular[masalar[masa][0]][3] += BERABERLIK_PUANI
            oyuncular[masalar[masa][0]][12].append(masalar[masa][1])
            oyuncular[masalar[masa][0]][20].append(oyuncular[masalar[masa][1]][9])
            oyuncular[masalar[masa][0]][20].append("b")
            oyuncular[masalar[masa][0]][20].append('½')
            oyuncular[masalar[masa][1]][3] += BERABERLIK_PUANI
            oyuncular[masalar[masa][1]][12].append(masalar[masa][0])
            oyuncular[masalar[masa][1]][20].append(oyuncular[masalar[masa][0]][9])  #masa sonucunun 0 olduğu durum için oyuncu verilerinin güncellenmesi
            oyuncular[masalar[masa][1]][20].append("s")
            oyuncular[masalar[masa][1]][20].append('½')
        elif sonuc == "1":
            oyuncular[masalar[masa][0]][3] += KAZANAN_PUANI
            oyuncular[masalar[masa][0]][11].append(masalar[masa][1])
            oyuncular[masalar[masa][0]][20].append(oyuncular[masalar[masa][1]][9])
            oyuncular[masalar[masa][0]][20].append("b")
            oyuncular[masalar[masa][0]][20].append("1")
            oyuncular[masalar[masa][0]][13] += 1
            oyuncular[masalar[masa][1]][20].append(oyuncular[masalar[masa][0]][9])  #masa sonucunun 1 olduğu durum için oyuncu verilerinin güncellenmesi
            oyuncular[masalar[masa][1]][20].append("s")
            oyuncular[masalar[masa][1]][20].append("0")
        elif sonuc == "2":
            oyuncular[masalar[masa][0]][20].append(oyuncular[masalar[masa][1]][9])
            oyuncular[masalar[masa][0]][20].append("b")
            oyuncular[masalar[masa][0]][20].append("0")
            oyuncular[masalar[masa][1]][3] += KAZANAN_PUANI
            oyuncular[masalar[masa][1]][11].append(masalar[masa][0])
            oyuncular[masalar[masa][1]][20].append(oyuncular[masalar[masa][0]][9])  #masa sonucunun 2 olduğu durum için oyuncu verilerinin güncellenmesi
            oyuncular[masalar[masa][1]][20].append("s")
            oyuncular[masalar[masa][1]][20].append("1")
            oyuncular[masalar[masa][1]][13] += 1
        elif sonuc == "3":
            oyuncular[masalar[masa][0]][20].append(oyuncular[masalar[masa][1]][9])
            oyuncular[masalar[masa][0]][20].append("b")
            oyuncular[masalar[masa][0]][20].append("+")
            oyuncular[masalar[masa][0]][19] = (tur_sayisi-(tur+1)) * EB_PUAN_CARPANI + oyuncular[masalar[masa][0]][3]  #masa sonucunun 3 olduğu durum için oyuncu verilerinin güncellenmesi
            oyuncular[masalar[masa][0]][3] += KAZANAN_PUANI
            oyuncular[masalar[masa][0]][13] += 1
            oyuncular[masalar[masa][0]][18] = True
            oyuncular[masalar[masa][1]][20].append(oyuncular[masalar[masa][0]][9])
            oyuncular[masalar[masa][1]][20].append("s")
            oyuncular[masalar[masa][1]][20].append("-")
        elif sonuc == "4":
            oyuncular[masalar[masa][0]][20].append(oyuncular[masalar[masa][1]][9])
            oyuncular[masalar[masa][0]][20].append("b")
            oyuncular[masalar[masa][0]][20].append("-")
            oyuncular[masalar[masa][1]][19] = (tur_sayisi-(tur+1)) * EB_PUAN_CARPANI + oyuncular[masalar[masa][0]][3]  #masa sonucunun 4 olduğu durum için oyuncu verilerinin güncellenmesi
            oyuncular[masalar[masa][1]][3] += KAZANAN_PUANI
            oyuncular[masalar[masa][1]][13] += 1
            oyuncular[masalar[masa][1]][18] = True
            oyuncular[masalar[masa][1]][20].append(oyuncular[masalar[masa][0]][9])
            oyuncular[masalar[masa][1]][20].append("s")
            oyuncular[masalar[masa][1]][20].append("+")
        elif sonuc == "5":
            oyuncular[masalar[masa][0]][20].append(oyuncular[masalar[masa][1]][9])
            oyuncular[masalar[masa][0]][20].append("b")
            oyuncular[masalar[masa][0]][20].append("-")
            oyuncular[masalar[masa][1]][20].append(oyuncular[masalar[masa][0]][9])  #masa sonucunun 5 olduğu durum için oyuncu verilerinin güncellenmesi
            oyuncular[masalar[masa][1]][20].append("s")
            oyuncular[masalar[masa][1]][20].append("-")
    return oyuncular

def puanlar_olustur(oyuncular,puanlar): #oyuncu puanlarını alan ve tekil puanlardan oluşan liste yapan fonksiyon
    puanlar = []
    for oyuncu in oyuncular:
        if oyuncular[oyuncu][3] not in puanlar: #oyuncu puanının daha önceden listeye eklenip eklenmediğinin kontrolü
            puanlar.append(oyuncular[oyuncu][3])
    return puanlar

def veri_sıfırla(oyuncular): #tur sonunda oyuncuların eşleşme değerlerini ve o tur bye geçip geçmeyeceği durumlarını sıfırlayan fonksiyon
    for oyuncu in oyuncular:
        oyuncular[oyuncu][8] = False
        oyuncular[oyuncu][5] = False
    return oyuncular        

def esitlik_bozma_hesapla(oyuncular): #eşitlik bozma ölçütlerinin hesaplanması ve oyuncuların verilerinde güncellenmesi
    for oyuncu in oyuncular:
        for i in range(len(oyuncular[oyuncu][4])):
            if i == 0:
                min1 = oyuncular[oyuncular[oyuncu][4][i]][3]
            elif i == 1:
                if oyuncular[oyuncular[oyuncu][4][i]][3] < min1: 
                    min1 = oyuncular[oyuncular[oyuncu][4][i]][3]
                    min2 = oyuncular[oyuncular[oyuncu][4][i-1]][3]
                else:
                    min2 = oyuncular[oyuncular[oyuncu][4][i]][3]      #oyuncunun rakipler listesinde dolaşılıp en küçük puana sahip 2 oyuncunun puanlarının min1 ve min2 değişkenlerine atanması
            else:
                if oyuncular[oyuncular[oyuncu][4][i]][3] < min1:
                    min1 = oyuncular[oyuncular[oyuncu][4][i]][3]
                elif oyuncular[oyuncular[oyuncu][4][i]][3] < min2:
                    min2 = oyuncular[oyuncular[oyuncu][4][i]][3]
        
        for i in oyuncular[oyuncu][4]:
            oyuncular[oyuncu][15] += oyuncular[i][3]
        oyuncular[oyuncu][15] = oyuncular[oyuncu][15] + oyuncular[oyuncu][19] - min1   #oyuncunun bh1 ve bh2 değerlerinin hesaplanması ve dict'teki değerlerinin güncellenmesi
        oyuncular[oyuncu][16] = oyuncular[oyuncu][15] - min2

        sb1=VARSAYILAN_DEGER
        sb2=VARSAYILAN_DEGER
        for i in oyuncular[oyuncu][11]:
            sb1 += oyuncular[i][3]
        for i in oyuncular[oyuncu][12]:          #oyuncunun yendiği ve berabere kaldığı rakipler listeleri dolaşılarak hesaplanan sb1 ve sb2 değerleri ile sb değerinin hesaplanması ve dict'teki değerinin güncellenmesi
            sb2 += oyuncular[i][3]
        sb = sb1 + sb2/SB2BOLENI + oyuncular[oyuncu][19]
        oyuncular[oyuncu][17] = sb
    return oyuncular   
 
def nihai_sıra_olustur(oyuncular,oyuncu_say): #turnuva sonunda puan, bh1, bh2, sb, gs öncelik sırası dikkae alınarak oluşturulan nihai sıralama listesi oluşturan fonksiyon
    nihai_liste = sorted(oyuncular.items(), key = lambda oyuncu: (oyuncu[1][3],oyuncu[1][15],oyuncu[1][16],oyuncu[1][17],oyuncu[1][13]), reverse = True)
    for i in range(oyuncu_say):
        oyuncular[nihai_liste[i][0]][21] = i+1 #oyuncuların son sıralamaya göre nihai sıra numarası almaları
    return oyuncular, nihai_liste    

def nihai_tablo_olustur(oyuncu_say,nihai_liste): #oyuncuların nihai sıralama listesine göre sıralandığı, puan ve eşitlik bozma puanlarının yazdırıldığı fonksiyon
    print("Sno BSNo  LNo    Ad-Soyad     ELO    UKD  Puan  BH-1  BH-2   SB  GS")
    print("--- ----  ---  ------------  -----  ----- ---- ----- ----- ----- --")
    for i in range(oyuncu_say):
        print(format(i+1, "3d"),end = " ")
        print(format(nihai_liste[i][1][9], "4d"),end = "  ")
        print(format(nihai_liste[i][0], "3"),end = "  ")
        print(format(nihai_liste[i][1][0], "12"),end = "  ")
        print(format(nihai_liste[i][1][1], "5d"),end = "  ")
        print(format(nihai_liste[i][1][2], "5d"),end = " ")
        print(format(nihai_liste[i][1][3], "4.2f"),end = " ")
        print(format(nihai_liste[i][1][15], "5.2f"),end = " ")
        print(format(nihai_liste[i][1][16], "5.2f"),end = " ")
        print(format(nihai_liste[i][1][17], "5.2f"),end = " ")
        print(format(nihai_liste[i][1][13], "2d"))

def capraz_tablo_olustur(tur_sayisi,oyuncular): #oyuncuların başlangıç sıra numarasına göre sıralandığı, her turdaki maç verilerinin, puan ve eşitlik bozma puanlarının yazdırıldığı fonksiyon
    print("BSNo SNo  LNo   Ad-Soyad    ELO   UKD ", end = " ")
    for i in range(tur_sayisi):
        print(f"{i+1}.Tur", end = " ")
    print("Puan  BH-1  BH-2  SB   GS")    
    print("---- --- ---- ------------ ----- -----", end = " ")
    for i in range(tur_sayisi):
        print("-----", end = " ")
    print("---- ----- ----- ----- --")
    for oyuncu in oyuncular:
        print(format(oyuncular[oyuncu][9], "4d"), end = " ")
        print(format(oyuncular[oyuncu][21], "3d"), end = " ")
        print(format(oyuncu, "4"), end = " ")
        print(format(oyuncular[oyuncu][0], "12"), end = " ")
        print(format(oyuncular[oyuncu][1], "5d"), end = " ")
        print(format(oyuncular[oyuncu][2], "5d"), end = " ")
        for i in range(tur_sayisi):
            print(oyuncular[oyuncu][20][TUR_VERI_SAYISI*i],oyuncular[oyuncu][20][TUR_VERI_SAYISI*i+1],oyuncular[oyuncu][20][TUR_VERI_SAYISI*i+2], end = " ")
        print(format(oyuncular[oyuncu][3], "4.2f"), end = " ")
        print(format(oyuncular[oyuncu][15], "5.2f"), end = " ")
        print(format(oyuncular[oyuncu][16], "5.2f"), end = " ")
        print(format(oyuncular[oyuncu][17], "5.2f"), end = " ")
        print(format(oyuncular[oyuncu][13], "2d"))

def main():
    oyuncular = {} #her bir oyuncu için program boyunca gerekecek tüm verilerin tutulacağı dictionary
    masalar = {} #her bir masada eşleştirilen kişilerin lno'larını tutacak olan dictionary
    bye_gecenler = [] #bye geçen ouncuların lno'larının tutulacağı liste
    puanlar = [0] #tekil puanların olacağı puanlar listesi
    oyuncular = oyuncu_al(oyuncular) #oyuncu girdilerinin alınıp oyuncular dict'inin güncellenmesi
    oyuncu_listesi = oyuncu_sırala(oyuncular) #oyuncular dict'inin sıralanmasıyla oluşan ve geri döndürülen oyuncu listesinin oyuncu_listesine atanması
    oyuncu_say = len(oyuncu_listesi) #turnuvadaki oyuncu sayısı
    oyuncular = bsno_ver(oyuncu_say,oyuncular,oyuncu_listesi) #oyunculara başlangıç sıra numarası verilmesi
    baslangic_sıra_listesi_olustur(oyuncu_say,oyuncu_listesi) #başlangıç tablosu oluşturma
    tur_sayisi = tur_sayisi_belirle(oyuncu_say) #turnuvanın kaç tur süreceğinin belirlenmesi
    oyuncular = ilk_renk_ataması(oyuncular,oyuncu_listesi,oyuncu_say) #ilk tur için renklerin belirlenmesi
    for tur in range(tur_sayisi): #her tur için
        oyuncu_listesi = oyuncu_sırala(oyuncular) #tur başında oyuncu_listesinin güncel puanlarla sıralanması
        puanlar.sort(reverse = True) #puanlar listesinin büyükten küçüğe sıralanması
        bye_gecenler,oyuncular = bye_ata(oyuncu_say,oyuncular,oyuncu_listesi,bye_gecenler,tur,tur_sayisi) #bye atanacak kişinin belirlenmesi
        masa_no = 1 #ilk masa için masa numarası
        oyuncular,masalar = eslestirme_yap(oyuncu_say,oyuncular,oyuncu_listesi,puanlar,masalar,masa_no) #eşleşmelerin gerçekleşmesi
        eslesme_tablosu_yap(tur,masalar,oyuncular,bye_gecenler)    #eşleşme tablosunun yazdırılması        
        oyuncular = masa_sonucu_al(tur,tur_sayisi,masalar,oyuncular) #her masa için maç sonucu alınması
        puanlar = puanlar_olustur(oyuncular,puanlar) #puanlar listesinin yeni puanlara göre güncellenmesi
        oyuncular = veri_sıfırla(oyuncular) #tur sonunda oyuncuların sıfırlanması gereken verilerinin sıfırlanması
    oyuncular = esitlik_bozma_hesapla(oyuncular) #turnuva sonunda oyuncuların eşitlik bozma sistemleri için puanlarının hesaplanması
    oyuncular,nihai_liste = nihai_sıra_olustur(oyuncular,oyuncu_say) #nihai sıralama listesinin oluşturulması
    nihai_tablo_olustur(oyuncu_say,nihai_liste) #nihai sıralama listesine göre sonuç tablosunun yazdırılması
    oyuncular = dict(sorted(oyuncular.items(), key = lambda oyuncu: (oyuncu[1][9]), reverse = False)) #oyuncular dict'inin başlangıç sıra numarasına göre sıralanması
    capraz_tablo_olustur(tur_sayisi, oyuncular) #oyuncuların eşleşmelerini de gösteren kapsamlı bir çapraz tablo

main()
