#Muhammad Khalif Rizaldi Wibowo
#L200180217

#1
def cetakSiku(x):
    for i in range (1,x+1):
        print('*'*i)
        
#2
def gambarlahPersegiEmpat(a, b):
    for i in range (a):
        if i==0 or i==a-1:
            print (b * '@')
        else:
            print ('@' + " " * (b-2) + '@') 

#3
def jumlahHurufVokal(huruf):
    vokal = 'aiueoAIUEO'
    a = 0
    hasil = 0
    for i in huruf :
        if i in vokal:
            a += len(i)
        else:
            a += 0
    hasil = len(huruf), a
    return hasil
#3b
def jumlahHurufKonsonan(huruf):
    konsonan = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    b = 0
    hasil = 0
    for i in huruf:
        if i in konsonan:
            b +=len(i)
        else:
            b +=0
    hasil = len(huruf),b
    return hasil
#4
def rerata(b):
    return sum(b)/len(b)

#5
from math import sqrt as sq
def apakahPrima(n):
    n = int(n)
    assert n>=0
    primaKecil = [2,3,5,7,9,11]
    bukanPrKecil = [0,1,4,6,8,9,10]
    if n in primaKecil:
        return True
    elif n in bukanPrKecil:
        return False
    else:
        for i in range(2,int(sq(n))+1):
             if n%i==0:
                return False
        return True

#6
def bilanganPrima(n):
    for i in range(2,n):
        prima = True
        for j in range (2,i):
            if(i%j==0):
                prima = False
            if (prima):
                print(i)
#7
def faktorPrima(x):
    bilanganList = []
    loop = 2
    while loop <= x:
        if x%loop == 0:
            x/= loop
            bilanganList.append(loop)
        else:
            loop += 1
    return bilanganList
#8
def apakahTerkandung(a, b):
    x = True
    for i in range(len(b)):
        if a in b:
            x = True
        else:
            x = False
    return x
#9
def kelipatan(x):
    for i in range (x):
        if(i<=0):
            pass
        elif(i%3==0 and i%5==0):
            print ('Python UMS')
        elif(i%3==0):
            print ('Python')
        elif(i%5==0):
            print ('UMS')
        else:
            print(i)
#10
from math import sqrt as akar
def selesaikanABC(a,b,c):
    a = float(a)
    b = float(b)
    c = float(c)
    D = float(b**2 - 4*a*c)
    if (D<0):
        hasil = "Determinannya negatif, persamaan tidak mempunayai akar real."
        return hasil
    else:
        x1 = (-b + akar(D)/(2*a))
        x2 = (-b - akar(D)/(2*a))
        hasil = (x1,x2)
        return hasil

#11
def apakahKabisat(tahun):
    hasil = False
    if(tahun%4==0 and tahun%100 !=0 and tahun%400 !=0):
        hasil = True
    elif(tahun%100==0 and tahun%400 !=0):
        hasil = False
    elif(tahun%400==0):
        hasil = True
    else:
        hasil = False
    return False
#12
import random
def tebak():
    max = 7
    start = 1
    x = random.randrange(1,100,1)
    while (start <= max):
        s = 'Masukkan tebakan ke- ' +str(start)+ ':>'
        i = input(s)
        if(i == x):
            print ("Ya, anda benar")
        elif(i > x):
            print("itu terlalu besar")
        elif(i < x):
            print("Itu terlalu kecil")
        start +=1
