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

# Įvedami skaičiai - a, b, c –kraštinių ilgiai, trys kintamieji (naudokite random.randint(x,x) funkciją nuo 1 iki 10).
# Parašykite Python programą, kuri nustatytų, ar galima sudaryti trikampį ir atsakymą atspausdintų.