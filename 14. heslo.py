heslo = input('Zadej heslo: ')
heslo_je_spravne = heslo == "333"

if heslo_je_spravne:
    print('Odpověď na základní otázku života, vesmíru a vůbec je 42')
    print('"Stopařův průvodce po galaxii"')
else:
    print ("Heslo jsi neuhodl, zkus to znova")

