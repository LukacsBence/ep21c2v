def feladat_1() -> list:
    print("Az első feladat megoldása: ")
    lista_1 = []
    try:
        fileobject = open("kosar.txt", "r", encoding="UTF-8")
        for line in fileobject:
            lista_1.append(line)
        fileobject.close()
        # print("1.feladat: A lista elkészült")
        print("Az első feladat vége.")
    except FileNotFoundError:
        print("Hiba! A keresett fájl nem található!")
    return lista_1


def feladat_2() -> None:
    """
    Kiírja, hányan fizettek a pénztárnál.
    """
    try:
        print("A második feladat megoldása:")
        fileobject = open("kosar.txt", "r", encoding="UTF-8")
        pays = 0
        pay_sign = "F"
        for line in fileobject:
            if pay_sign in line:
                pays = pays + 1
        fileobject.close()
        print(f"A kasszánál való fizetések száma: {pays}")
    except FileNotFoundError:
        print("Hiba! A keresett fájl nem található!")


def feladat_3() -> None:
    """
    Bekéri egy vásárlás sorszámát és kiírja:
        - hány darab árucikk volt a kosárban,
        - mely árucikkekből és milyen mennyiségben vásároltak,
        - a vásárlás összegét.
    """
    print("A harmadik feladat megoldása:")
    fileobject = open("kosar.txt", "r", encoding="UTF-8")
    print("Kérem adja meg a vásárlás sorszámát (pozitív egész szám): ")
    sorszam = (input(int))
    if sorszam == float or sorszam == str:
        print("A megadott szám érvénytelen, mivel nem egy pozitív egész!")
    else:
        sign = "F"
        counter_of_buyers = 0
        for line in fileobject:
            if sign in line:
                counter_of_buyers = counter_of_buyers + 1
            if sign not in line:
                counter_of_buyers = counter_of_buyers + 0
            break
    fileobject.close()


# megjegyzés: végi fut, nem counter_of_buyers != sorszam  -ig
def feladat_4() -> None:
    """
    Bekéri egy árucikk nevét és kiírja:
        - melyik vásárlásnál vettek először a termékből
        - melyik vásárlásnál vettek utoljára a termékből
        - összesen hány alkalommal vásároltak a termékből
    """
    print("A negyedik feladat megoldása:")
    fileobject = open("kosar.txt", "r", encoding="UTF-8")
    print("Kérem adja meg a keresni kívánt termék nevét (kérem szöveget adjon meg!): ")
    name_of_product = input(str)
    times_purchased = 0
    if name_of_product == "F":
        print("Az ~F~ nem egy termék, hanem egy jezés!")
    else:
        for line in fileobject:
            if name_of_product in line:
                times_purchased = times_purchased + 1
            if name_of_product not in line:
                times_purchased = times_purchased + 0
        print(f"A ~{name_of_product}~ nevű termék összesen {times_purchased} alkalommal lett megvásárolva.")


def feladat_5(filepath: str) -> None:
    """
    Elmenti a megadott fájlba a vásárlásonként fizetendő összeget.
    Beolvassa a fájlból a kosarak tartalmát.

    :param filepath: A kosarak tartalmát tartalmazó fájl elérési útvonala.
    """
    print("Az ötödik feladat megoldása:")
    open("kosar.txt", "r", encoding="UTF-8")
    print("A fájl mentése és kosarak tartalmának beolvasása folyamatban:")
    price_one = 1000
    price_two = 900
    price_all_left = 800
    products_left = 0
    one_product = price_one
    two_product = price_one + price_two
    three_or_more_product = price_one + price_two + (products_left * price_all_left)


class Bolt:
    """
    A vásárlásokat kezelő osztály. Az osztály egyetlen attribútuma a kosarak listája.
    """

    def __init__(self, termek: str, darabszam: int):
        """
        A bolt létrehozásakor beállítja az osztály attribútumait.
        """
        self.darabszam = darabszam
        self.termek = termek

# print("1. feladat: A fájl beolvasása:")
# filepath = "kosar.txt"
# fileobject = open(filepath, "r")
# print("\n")

# print("2. feladat: A kasszánál való fieztések száma:")
# pays = 0
# pay_sign = "F"
# for line in fileobject:
#    if pay_sign in line:
#        pays = pays + 1
# print(f"A kasszánál való fizetések száma: {pays}")
# print("\n")
