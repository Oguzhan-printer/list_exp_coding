#TASK 1

fruits = ['apple', 'banana', 'Strawberry ', 'cherry ']
fruits.append('Orange')
fruits.insert(2,'Pear')
fruits.remove('banana')
print(fruits)
print('list length:', len(fruits))

#TASK 2

numbers = [15, 8, 22, 31, 5, 10]
b= max(numbers)
a= min(numbers)
print('The minumum is:', a)
print('The maximum number is:', b)

#TASK 3

num = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

new_list = [i for i in num if i < 60]

print(new_list)

last_list = [i for i in num if i > 70]

print(last_list)

end_list = [i for i in num if i > 40 and i < 80]

print('3 and 7 between 40 and 80:', end_list)


#TASK 4

dersler = ["Matematik", "Fizik", "Kimya", "Biyoloji"]
print(enumerate[dersler])

for index, ders in enumerate(dersler):
    print(f"{index}. ders: {ders}")

#TASK 5

A = {10, 20, 30, 40, 50}

B = {30, 40, 50, 60, 70}

birlesim = A.union(B)  # A | B 
print(birlesim)

kesisim = A.difference(B)
print(kesisim)

C_sorusu  = B.difference(A)
print(C_sorusu)

D_sorusu = A.difference(B)
print(D_sorusu)

#TASK 6

input = (5, 10, 15, 20, 25, 30, 35)

first_three_element = input[:3]
print(first_three_element)

last_two_element = input[-2:]
print(last_two_element)

for i in input:
    if i == 20 :
        print(i,'sayısı tuple içerisinde var.')
    else:
        print(i,'sayısı tuple içerisinde yok.')

#TASK 7    

ogrenci = {"isim": "Ahmet", "yas": 20, "bolum": "Bilgisayar Mühendisliği"}

ogrenci.update({"yas":21})
ogrenci.update({"okul":'İTÜ'})
print(ogrenci)

x =list(ogrenci.values())
print(x)

print(ogrenci["isim"])


#TASK 8

ders_notlari = {
"Ali": 85,
"Zeynep": 90,
"Mehmet": 78,
"Elif": 95
}
print('***SONUÇLAR***')
for isim, puan in ders_notlari.items():
    print(f'{isim} : {puan}')


#TASK 9

sehirler = ["Ankara", "İstanbul", "İzmir", "Bursa", "Antalya", "Adana", "Trabzon"]
new_sehirler =[]

for sehir in sehirler:
    if sehir.startswith('İ'):
        new_sehirler.append(sehir)
        print(new_sehirler)
    else :
        print(sehir)

aynı_islem =  [sehir for sehir in sehirler if sehir.startswith('İ') ]    
print(aynı_islem)


#TASK 10

sayılar = [1, 2, 3, 4, 5, 6, 7 , 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]

transaction = [i for i in sayılar if i % 5 == 0]

print(transaction)

    





















