'''
author = 
'''
import string

TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.''']

# Vyžádá si od uživatele přihlašovací jméno a heslo.
# Zjistí, jestli zadané údaje odpovídají někomu z registrovaných uživatelů.
# Pokud je uživatel registrovaný, pozdrav jej a umožni mu analyzovat texty. Pokud není, upozorni jej a ukonči program.

# Uživatelé
"""
| USER |   PASSWORD  |
-----------------------
| bob  |     123     |
| ann  |    pass123  |
| mike | password123 |
| liz  |    pass123  |
"""

users = {"bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123"}
print("Vítejte v aplikaci Text analyzátor")
user_in= input("Zadej uživatelské jméno: ")
user = user_in.strip(" ")
pwd_in = input("Zadej své heslo: ")
pwd = pwd_in.strip(" ")
if user in users.keys():
    if True and users.get(user) == pwd:
        print(f"Ahoj, Tvé přihlašovací údaje jsou : {user} , {pwd}")
    else:
        print("Vaše heslo nesouhlasí s uživatelským jménem"); exit(-1)
else:
    print("Uživatelské jméno je špatně"); exit(-1)

print("-" * 50)
txt_cs_in = input("Vyber si číslo textu[1-3] ")

if not txt_cs_in.isdigit():
    print("Nejedná se o číslo")
    exit(-1)
else:
    if int(txt_cs_in) >= 1 and int(txt_cs_in) <= 3:
        txt_cs = int(txt_cs_in) - 1

    else:
        print("Zadané číslo je mimo rozsah")
        exit(-1)

print("-" * 50)
txt_anal = TEXTS[txt_cs].split()
lst_anal = list()
pct_prvni_velke = 0
pct_velka = 0
pct_mala = 0
pct_cislice = 0
lst_cislic = list()

#char = " ?.!/;:,"
chars = [';', ':', '!', "*"," ","",'?','.',' .','/',',']
for wrd in txt_anal:
        wrd_cl = ''.join(i for i in wrd if not i in chars)
        lst_anal.append(wrd_cl)

print(lst_anal)
for i in range(0,len(lst_anal)):
        if lst_anal[i].istitle():
            pct_prvni_velke += 1
        if lst_anal[i].isalpha() and lst_anal[i].isupper():
            pct_velka += 1
        if lst_anal[i].isalpha() and lst_anal[i].islower():
            pct_mala += 1

        if lst_anal[i].isdigit():
            pct_cislice += 1
            lst_cislic.append(int(lst_anal[i]))

print(f"There are {len(lst_anal)} words in the selected text")
print(f"There are {pct_prvni_velke} titlecase words.")
print(f"There are {pct_velka} uppercase words.")
print(f"There are {pct_mala} lowercase words.")
print(f"There are {pct_cislice} numeric strings.")
print("The sum of all the numbers: ", sum(lst_cislic))

vyskyt = dict()
lst = list()
lst_count = 0
for wrd in lst_anal:
    lst.append(len(wrd))
    dict_help = {len(wrd):lst.count(len(wrd))}
    vyskyt.update(dict_help)

print("=" * 50)
print(f"LEN| OCCURENCES | NR.")
print("."* 40)
for klic, hod in sorted(vyskyt.items()):
    print(f"{klic} | {'*' * int(hod)} | {hod}")



