from functools import reduce

soyad = ['Aygun', 'Çiçek', 'Deniz', 'Atar', 'Dener', 'Yılmaz']
toplam_satis_miktari = [['Ayse', 3, 6, 7], ['Ece', 5, 2, 4], ['Arya', 6, 5], ['Ali', 3], ['Can', 5, 7, 9, 11],['Aybar', 2, 3]]
sonuc = list(map(lambda m,u: [m[0]] + [u] + [reduce(lambda c, o: c + o, m[1:])],toplam_satis_miktari,soyad))
print(sonuc)