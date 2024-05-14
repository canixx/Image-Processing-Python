#deque
#listelerden tek farkı boyutunun önceden belirleniyor olması.

from collections import deque
dq = deque(maxlen=3)

dq.append(1) #sona ekler
print(dq)

dq.append(2)
print(dq)

dq.append(3)
print(dq)

dq.append(4)
print(dq)

dq.append(5)
print(dq)

dq.appendleft(6) #soldan ekler
print(dq)

dq.clear()
print(dq)

"""
-----------------------------------------------------
"""

#dictionary

dict = {"İstanbul": 34,
        "İzmir" : 35,
        "Konya":42}

print(dict)
print(dict["İstanbul"])
print(dict.keys())
print(dict.values())


"""
-------------------------------------------------------
"""
#if-elif-else

dict = {"İstanbul": 34,
        "İzmir" : 35,
        "Konya":42}

keys = dict.keys()
deger = "İstanbul"

if deger in keys:
    print("Evet")
else:
    print("Hayır")

"""
----------------------------------------------------------------
"""

#DÖNGÜLER

"""
- bir dizi üzerinde yineleme yapmak için kullanılan yapılardır.
-diziler: liste,tuple,string,sözlük, numpy pandas veri tipleri
"""

#FOR
liste = [1,4,5,6,8,3,3,4,67]
print(sum(liste))

toplam = 0
for c in liste:
    toplam = toplam + c
print(toplam)

tup1 = ((1,2,3),(3,4,5))
for x,y,z in tup1:
    print(x,y,z)

#WHILE
liste = [1,4,5,6,8,3,3,4,67]
limit = len(liste)

her = 0
hesapla = 0
while her < limit:
    hesapla = hesapla + liste[her]
    her = her + 1
print(hesapla)

#FONKSİYON

def carpma(x,y,z):
    return x*y*z
sonuc = carpma(2,3,4)
print(sonuc)

#aynı işlem with lambda
fonksiyon_lambda = lambda x,y,z : x*y*z
sonuc2 = fonksiyon_lambda(2,3,4)
print(sonuc2)

#YIELD
"""
-iterasyon : yineleme (for döngüleri gibi)
-generator : yineleyiciler. değerleri bellekte saklamaz. yeri gelince anında üretir.
-yield : fonksiyon eğer return olarak generator döndürecek ise bunu return yerine yield sozcugu yapar.
"""
generator = (x for x in range(1,4))
for i in generator:
    print(i)

def createGenarator():
    liste = range(1,4)
    for i in liste:
        yield i
genarator = createGenarator()
print(genarator)

for i in genarator:
    print(i)
