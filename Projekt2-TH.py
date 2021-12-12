# Projekt 02 (Bulls & Cows)– Tomáš H.
# Import balíčku pro náhodné volby
import random


def spustit_hru():
    pozdravit_uzivatele()
    tajne_cislo = generovani_tajneho_cisla()
    print(tajne_cislo)
    vyhodnot_hru(zadani_cisla(), tajne_cislo)
    # while True:
    #     zadane_cislo = zadani_cisla()
    #     if vyhodnot_hru(zadane_cislo, tajne_cislo):
    #         break


def pozdravit_uzivatele() -> str:
    print("Vítejte ve hře Bulls & Cows")
    print("-" * 32)
    print("Došlo k vygenerování 4ciferného čísla.")
    print("-" * 32)


def prubeh_hry(hadani: bool):
    un_seznam = random.sample(range(1, 9), 4)
    nov = str()
    print(un_seznam)
    for i in un_seznam:
        nov += str(i)
    return int(nov)


def zadani_cisla() -> int:
    zadane_cislo = input("Zadej svuj tip: ")
    if zadane_cislo.isdigit() and len(zadane_cislo) == 4 and int(zadane_cislo[0]) > 0:
        return zadane_cislo
    else:
        print("Zadane cislo nesplnuje podminky, ukončuji program ...")
        quit()


def vyhodnot_hru(zadane: int, tajne: int):
    # if zadane == tajne:
    #     print("Vyhrál si")
    bull = 0
    for i, prvek in enumerate(str(zadane)):
        for x, cislo in enumerate(str(tajne)):
            if (i, prvek) == (x, cislo):
                bull += 1

    # Výpis uhodlých císel se stejnou pozici
    if bull > 1:
        print(bull, "bulls")
    elif bull == 0:
        pass
    else:
        print(bull, "bull")


def generovani_tajneho_cisla():
    generated = []
    nov = str()
    cisla = list(range(1, 10))
    generated.append(cisla.pop(random.randint(0, len(cisla) - 1)))

    cisla.append(0)

    for i in range(3):
        generated.append(cisla.pop(random.randint(0, len(cisla) - 1)))

    for cislo in generated:
        nov += str(cislo)
    return int(nov)


if __name__ == '__main__':
    spustit_hru()
