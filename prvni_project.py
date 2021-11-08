# /Kurz Engeto/Python Academy/Project 1/Analyzator textu
# Autor : Lubomír Klubus

#import textu
from task_template import TEXTS

#import users
from usersfile import users

oddelovac = '-' * 40
barva_start = '\033[94m'
barva_stop = '\033[0m'


# Prihlasovaci udaje vstup
username = input('username: ')
password = input('password: ')

print (oddelovac)

# overeni uzivatele a uvitani
if not(username in users and password == users.get(username)):
    print ("Wrong username or password. END ")



else:
    print(
        f'Welcome to the app, {barva_start}{username}{barva_stop}\nWe have {barva_start}3{barva_stop} texts to be analyzed.',
        sep='')
    print(oddelovac)
    str_cislo_vybraneho_textu = ''
    cislo_vybraneho_textu = 0


    #vyber textu


    while ((cislo_vybraneho_textu <=0) or (cislo_vybraneho_textu > 3)) :


        str_cislo_vybraneho_textu = input('Enter a number btw. 1 and 3 to select: ')
        print(oddelovac)
        if str_cislo_vybraneho_textu.isdigit():
            cislo_vybraneho_textu = int(str_cislo_vybraneho_textu)
        else: cislo_vybraneho_textu = 0


    pracovni_text = TEXTS[cislo_vybraneho_textu - 1]


    # rozdělím `str` na `list`
    vycistena_slova = list()

    for slovo in pracovni_text.split():
        vycistena_slova.append(
            slovo.strip(",.:;")
        )


    #analyza textu
    pocet_slov = len(vycistena_slova)
    slova =''
    pocet_title = 0
    pocet_upper = 0
    pocet_lower = 0
    pocet_numeric = 0
    suma = 0
    seznam_delek = []
    for slova in  vycistena_slova:
        seznam_delek.append(len(slova))
        if slova.istitle():
            pocet_title += 1
        if slova.isupper() and slova.isalpha():
            pocet_upper += 1
        if slova.islower() and slova.isalpha():
            pocet_lower += 1
        if slova.isdigit():
            pocet_numeric += 1
            suma += int(slova)




    #Vypis vysledku analyzy
    print(f'There are {barva_start}{pocet_slov}{barva_stop} words in the selected text.')
    print(f'There are {barva_start}{pocet_title}{barva_stop} titlecase words.')
    print(f'There are {barva_start}{pocet_upper}{barva_stop} uppercase words.')
    print(f'There are {barva_start}{pocet_lower}{barva_stop} lowercase words.')
    print(f'There are {barva_start}{pocet_numeric}{barva_stop} numeric strings.')
    print(f'The sum of all the numbers {barva_start}{suma}{barva_stop} ')

    #Vypis cetnosti delek slov
    print (oddelovac)
    print('LEN| OCCURENCES         |NR.')
    print(oddelovac)
    for delka in range(min(seznam_delek),max(seznam_delek)+1):
        cetnost = seznam_delek.count(delka)
        if  cetnost != 0:
            radek = '*' * cetnost
            print(f'{barva_start}{str(delka).rjust(2)}.{barva_stop}|{radek.ljust(20)}|{barva_start}{cetnost}{barva_stop}')

    print(oddelovac)
