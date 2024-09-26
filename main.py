import random

# 1. Sukurkite 4 kintamuosius, kurie saugotų jūsų vardą, pavardę, gimimo metus ir šiuos metus (nebūtinai tikrus).
# Parašykite kodą, kuris pagal gimimo metus paskaičiuotų jūsų amžių ir naudodamas vardo ir pavardės kintamuosius atspausdintų tokį sakinį :
# "Aš esu Vardenis Pavardenis. Man yra XX metai(ų)".


# vardas = "Lalo"
# pavarde = "Salamanca"
# gm = 1999
# sm = 2024
# print(f"As esu {vardas} {pavarde}. Man yra {sm - gm} metai(-u)")


# 2. Sukurkite du kintamuosius ir naudodamiesi funkcija random.randint(x,x) jiems priskirkite atsitiktines reikšmes nuo 0 iki 4.
# Didesnę reikšmę padalinkite iš mažesnės. Atspausdinkite rezultatą jį suapvalinę iki 2 skaičių po kablelio.
# sk1 = random.randint(0, 4)
# sk2 = random.randint(0, 4)
# print(f"{sk1} \n{sk2}")
# if sk1 != 0 and sk2 != 0:
#     if sk1 > sk2:
#         print(f"{sk1} / {sk2} = {sk1 / sk2:.2f}")
#     elif sk2 > sk1:
#             print(f"{sk2} / {sk1} = {sk2 / sk1:.2f}")
# else:
#     print("Dalyba neimanoma, nes vienas is skaiciu yra 0")

# 3. Naudokite funkcija random.randint(x,x). Sukurkite tris kintamuosius ir naudodamiesi funkcija random.randint(x,x)
# jiems priskirkite atsitiktines reikšmes nuo 0 iki 25. Raskite ir atspausdinkite kintąmąjį turintį vidurinę reikšmę.

# sk1 = random.randint(0, 25)
# sk2 = random.randint(0, 25)
# sk3 = random.randint(0, 25)
# print(f"{sk1} \n{sk2} \n{sk3}")
# if (sk1 > sk2 and sk1 < sk3) or (sk1 <= sk2 and sk1 >= sk3):
#     print(f"Vidurine reiksme:{sk1}")
# elif (sk2 > sk1 and sk2 < sk3) or (sk2 <= sk1 and sk2 >= sk3):
#     print(f"Vidurine reiksme:{sk2}")
# elif (sk3 > sk1 and sk3 < sk2) or (sk3 <= sk1 and sk3 >= sk2):
#     print(f"Vidurine reiksme:{sk3}")


# sk1 = random.randint(0, 25)
# sk2 = random.randint(0, 25)
# sk3 = random.randint(0, 25)
# print(f"{sk1} \n{sk2} \n{sk3}")
# number = [sk1, sk2, sk3]
# number.sort()
# middle_value = number[1]
# print(f"Vidurine reiksme: {middle_value}")


# 4. Įvedami skaičiai - a, b, c –kraštinių ilgiai, trys kintamieji (naudokite random.randint(x,x) funkciją nuo 1 iki 10).
# Parašykite Python programą, kuri nustatytų, ar galima sudaryti trikampį ir atsakymą atspausdintų.

# a = random.randint(1, 10)
# b = random.randint(1, 10)
# c = random.randint(1, 10)
# print(f"a = {a} \nb = {b} \nc = {c}")
# if (a + b > c) and (a + c > b) and (b + c > a):
#     print("trikampi sudaryti galima")
# else:
#     print("trikampi sudaryti neimanoma")

# 5. Sukurkite keturis kintamuosius ir random.randint(x,x) funkcija sugeneruokite jiems reikšmes nuo 0 iki 2.
# Suskaičiuokite kiek yra nulių, vienetų ir dvejetų. (sprendimui masyvo nenaudoti).

# a = random.randint(0, 2)
# b = random.randint(0, 2)
# c = random.randint(0, 2)
# d = random.randint(0, 2)
# count0 = 0
# count1 = 0
# count2 = 0
# print(f"a = {a} \nb = {b} \nc = {c} \nd = {d}")
# if a == 0:
#     count0 = count0 + 1
# elif a == 1:
#     count1 = count1 + 1
# elif a == 2:
#     count2 = count2 + 1
# if b == 0:
#     count0 = count0 + 1
# elif b == 1:
#     count1 = count1 + 1
# elif b == 2:
#     count2 = count2 + 1
# if c == 0:
#     count0 = count0 + 1
# elif c == 1:
#     count1 = count1 + 1
# elif c == 2:
#     count2 = count2 + 1
# if d == 0:
#     count0 = count0 + 1
# elif d == 1:
#     count1 = count1 + 1
# elif d == 2:
#     count2 = count2 + 1
# print(f" 0 yra:{count0}")
# print(f" 1 yra:{count1}")
# print(f" 2 yra:{count2}")


# antra variantas
# a = random.randint(0, 2)
# b = random.randint(0, 2)
# c = random.randint(0, 2)
# d = random.randint(0, 2)
# print(f"a = {a} \nb = {b} \nc = {c} \nd = {d}")
# skaiciai = [a, b, c, d]
# nuliu = skaiciai.count(0)
# vienetu = skaiciai.count(1)
# dvejetu = skaiciai.count(2)
# print(f" 0 yra:{nuliu}")
# print(f" 1 yra:{vienetu}")
# print(f" 2 yra:{dvejetu}")

# 6. Naudokite funkcija random.randint(x,x).
# Sukurkite ir atspausdinkite 3 skaičius nuo -10 iki 10. Skaičiai mažesni už 0 turi būti  laužtiniuose skliaustuose
# [], 0 -  (), didesni už 0 {}.   [-4],  (0)

# a = random.randint(-10, 10)
# b = random.randint(-10, 10)
# c = random.randint(-10, 10)
# print(f"a = {a} \nb = {b} \nc = {c}")
# if a < 0:
#     print(f"a skaicius = [{a}]")
# elif a == 0:
#     print(f"a skaicius = ({a})")
# elif a > 0:
#     print(f"a skaicius = {{{a}}}")
# if b < 0:
#     print(f"b skaicius = [{b}]")
# elif b == 0:
#     print(f"b skaicius = ({b})")
# elif b > 0:
#     print(f"b skaicius = {{{b}}}")
# if c < 0:
#     print(f"c skaicius = [{c}]")
# elif c == 0:
#     print(f"c skaicius = ({c})")
# elif c > 0:
#     print(f"c skaicius = {{{c}}}")

# 7. Įmonė parduoda žvakes po 1 EUR. Perkant daugiau kaip 1000 vienetų taikoma 3 % nuolaida, daugiau kaip 2000 vienetų- 4 % nuolaida.
# Parašykite programą, kuri skaičiuos žvakių kainą ir atspausdintų atsakymą kiek žvakių ir kokia kaina perkama.
# Žvakių kiekį generuokite random.randint(x,x) funkcija nuo 5 iki 3000.

# a = random.randint(5, 3000)
# print(f"zvakiu kiekis = {a}")
# kaina = a * 1
# print(f"Bendra zvakiu kaina = {kaina}Eur")
# if a > 2000:
#     print(f"Kaina perkant daugiau kaip 2000 vienetu bus sumoketa (su 4 % nuolaida): {a}*0.96 = {round(kaina * 0.96, 2)}Eur.")
# elif a > 1000:
#     print(f"Kaina perkant daugiau kaip 1000 vienetu bus sumoketa (su 3 % nuolaida): {a}*0.97 = {round(kaina * 0.97, 2)}Eur.")
# else:
#     print(f"Nuolaida netaikoma, iprasta kaina = {kaina}Eur")

# 8. Naudokite funkcija random.randint(x,x). Sukurkite tris kintamuosius su atsitiktinėm reikšmėm nuo 0 iki 100.
# Paskaičiuokite jų aritmetinį vidurkį. Ir aritmetinį vidurkį atmetus tas reikšmes, kurios yra mažesnės nei 10 arba didesnės nei 90.
# Abu vidurkius atspausdinkite. Rezultatus apvalinkite iki sveiko skaičiaus.

# a = random.randint(0, 100)
# b = random.randint(0, 100)
# c = random.randint(0, 100)
# print(f"a = {a} \nb = {b} \nc = {c}")
# vidurkis = (a + b + c) / 3
# print(f"aritmetinis vidurkis = {round(vidurkis)}")
# fm = 0
# fk = 0
# if 10 <= a <= 90:
#     fm += a
#     fk += 1
# if 10 <= b <= 90:
#     fm += b
#     fk += 1
# if 10 <= c <= 90:
#     fm += c
#     fk += 1
# if fk > 0:
#     vidurkis = fm / fk
#     print(f"{round(fm / fk, 0)}")

# 9. Padarykite skaitmeninį laikrodį, rodantį valandas, minutes ir sekundes.
# Valandom, minutėm ir sekundėm sugeneruoti panaudokite funkciją random.randint(x,x).
# Sugeneruokite skaičių nuo 0 iki 300. Tai papildomos sekundės. Skaičių pridėkite prie jau sugeneruoto laiko.
# Atspausdinkite laikrodį prieš ir po sekundžių pridėjimo ir pridedamų sekundžių skaičių.
h = random.randint(0, 300)
minutes = random.randint(0, 300)
sec = random.randint(0, 300)
print(f"valandos = {h} \nminutes = {minutes} \nsekundes = {sec}")




#  10. Naudokite funkcija random.randint(x,x). Sugeneruokite 6 kintamuosius su atsitiktinem reikšmėm nuo 1000 iki 9999.
# Atspausdinkite reikšmes viename strige, išrūšiuotas nuo didžiausios iki mažiausios, atskirtas tarpais. Naudoti ciklų ir masyvų NEGALIMA.
# a1 = random.randint(1000, 9999)
# a2 = random.randint(1000, 9999)
# a3 = random.randint(1000, 9999)
# a4 = random.randint(1000, 9999)
# a5 = random.randint(1000, 9999)
# a6 = random.randint(1000, 9999)
# print(a1)
# print(a2)
# print(a3)
# print(a4)
# print(a5)
# print(a6)
# pirmas = max(a1, a2, a3, a4, a5, a6)
# if pirmas == a1:
#     a1 = -1
# elif pirmas == a2:
#     a2 = -1
# elif pirmas == a3:
#     a3 = -1
# elif pirmas == a4:
#     a4 = -1
# elif pirmas == a5:
#     a5 = -1
# elif pirmas == a6:
#     a6 = -1
# antras = max(a1, a2, a3, a4, a5, a6)
# if antras == a1:
#     a1 = -1
# elif antras == a2:
#     a2 = -1
# elif antras == a3:
#     a3 = -1
# elif antras == a4:
#     a4 = -1
# elif antras == a5:
#     a5 = -1
# elif antras == a6:
#     a6 = -1
# trecias = max(a1, a2, a3, a4, a5, a6)
# if trecias == a1:
#     a1 = -1
# elif trecias == a2:
#     a2 = -1
# elif trecias == a3:
#     a3 = -1
# elif trecias == a4:
#     a4 = -1
# elif trecias == a5:
#     a5 = -1
# elif trecias == a6:
#     a6 = -1
# ketvirtas = max(a1, a2, a3, a4, a5, a6)
# if ketvirtas == a1:
#     a1 = -1
# elif ketvirtas == a2:
#     a2 = -1
# elif ketvirtas == a3:
#     a3 = -1
# elif ketvirtas == a4:
#     a4 = -1
# elif ketvirtas == a5:
#     a5 = -1
# elif ketvirtas == a6:
#     a6 = -1
# penktas = max(a1, a2, a3, a4, a5, a6)
# if penktas == a1:
#     a1 = -1
# elif penktas == a2:
#     a2 = -1
# elif penktas == a3:
#     a3 = -1
# elif penktas == a4:
#     a4 = -1
# elif penktas == a5:
#     a5 = -1
# elif penktas == a6:
#     a6 = -1
# sestas = max(a1, a2, a3, a4, a5, a6)
# print(f" Surusiuotos reiksmes: {pirmas} {antras} {trecias} {ketvirtas} {penktas} {sestas}")
