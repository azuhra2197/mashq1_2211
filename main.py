# 1-misol
def kassa_hisobla(narx, tolov):
    if tolov < 0 or narx < 0:
        print(f"Xatolik")
    elif tolov >= narx:
        qaytim = tolov - narx
        print(f"Qaytim: {qaytim}")
    else:
        kerak = narx - tolov
        print(f"Yetishmaydi: {kerak}")


kassa_hisobla(18000, 13000)

kassa_hisobla(26000, 22000)

kassa_hisobla(-5000, -9000)

kassa_hisobla(193000, 84000)

kassa_hisobla(1000, 8000)
