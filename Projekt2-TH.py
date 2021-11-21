# Projekt 02 (Bulls & Cows)– Tomáš H.
# Import balíčku pro náhodné volby
import random

def spustit_hru():
    pass


def pozdravit_uzivatele() -> str:
    print("Vítejte ve hře Bulls & Cows")
    print("-" * 32)
    print("Došlo k vygenerování 4ciferného čísla.")
    print("-" * 32)


def prubeh_hry(hadani : bool):
    un_seznam = random.sample(range(1,9),4)
    nov = str()
    for i in un_seznam:
        nov += str(i)
    return int(nov)

#     tajne_cislo = random.randint(1000,9999)
#     return tajne_cislo

print(prubeh_hry(hadani = True))