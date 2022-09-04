dosya = open("soru3 py.txt","w")

for m_sayi in range(1,99):
    m_sayi_1 = 0
    for u in str(m_sayi):
        m_sayi_1 += int(u)
        if (m_sayi_1 %2 == 0):
            print("sayı çift olduğu için yazılmaz yeniden dene...")
        else:
            print("dosya yazıldı",dosya.write(str(m_sayi_1)))

dosya.close()