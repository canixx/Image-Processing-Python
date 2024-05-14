#numpy

"""
-matrisler için hesaplama kolaylığı sağlar.
"""
import numpy as np

# 1*15 boyutunda bir array-dizi

dizi = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
print(dizi)
print(dizi.shape) #arrayin boyutu

dizi2= dizi.reshape(3,5) #15lik arrayı yeniden şekillendirdik.
print("Şekil:", dizi2.shape)
print("Boyut:",dizi2.ndim)
print("Veri Tipi:", dizi2.dtype.name)
print("Boy:", dizi2.size)

#array type
print("Type:", type(dizi2))

#2 boyutlu array
dizi2D = np.array([[1,2,3,4],[5,6,7,8],[9,8,7,5]]) # 4 sutun 3 satır
print(dizi2D)

#sıfırlrdan oluşan bir array
sifir_dizi = np.zeros((3,4)) #3 satır, 4 sütun
print(sifir_dizi)

#birlerden oluşan array
bir_dizi = np.ones((3,4)) #3 satır, 4 sütun
print(bir_dizi)

#boş array
bos_dizi = np.empty((3,4)) #3 satır, 4 sütun
print(bos_dizi)

#arrange (x,y, basamak) = x'ten başlayıp basamak büyüklüğünde artırarak y'ye gidiyor y dahil değil.
dizi_aralik = np.arange(10,50,5)
print(dizi_aralik)

#linspace(x,y,basamak)= x ten  baslayip y'ye kadar basamak boyutunda bölerek gidiyor. y dahil.

dizi_bosluk = np.linspace(10,20,5) # 10 ve 20 arasını 5 e bölüyor
print(dizi_bosluk)

#float array
float_array = np.float32([[1,2],[3,4]])
print(float_array)

#matematiksel işlemler
a = np.array([1,2,3])
b = np.array([4,5,6])
print(a+b)
print(a-b)
print(a**2)

#dizi elamanı toplama
print(np.sum(a))

#max değer
print(np.max(a))

#min değer
print(np.min(a))

#mean ortalama
print(np.mean(a))

#median değer (ortadaki sayı)
print(np.median(a))

#rastgele sayı üretme [0,1] arasında sürekli üniform 3x3 matris
rastgele_dizi = np.random.random((3,3))
print(rastgele_dizi)

# indeks
dizi = np.array([1,2,3,4,5,6,7])
print(dizi[0])

# dizinin ilk 4 elemanı
print(dizi[0:4])

# dizinin tersi
print(dizi[::-1])

#
dizi2D = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(dizi2D)

# dizinin 1. satır ve 1. sutununda bulunan elemanı
print(dizi2D[1,1])

# 1. sütun ve tüm satılar
print(dizi2D[:,1])

# satır 1, sütun 1,2,3
print(dizi2D[1,1:4])

# dizinin son satır tüm sütunları
print(dizi2D[-1, :])

#
dizi2D = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(dizi2D)

# vektör haline getirme
vektor = dizi2D.ravel()
print(vektor)

maksimum_sayinin_indeksini = vektor.argmax()
print(maksimum_sayinin_indeksini)