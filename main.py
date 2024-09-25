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

