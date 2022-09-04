# #soru-2
import random

m_dizi = []
for jr in range(6):
    u_sayi = random.randint(1, 50)
    if len(m_dizi) == u_sayi:
        print(jr)
    else:
        m_dizi.append(u_sayi)
print(m_dizi)