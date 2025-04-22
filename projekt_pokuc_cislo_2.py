ukoly = []

# Funkce pro přidání úkolu: volba 1
def pridat_ukol():
    while True:
        nazev_ukolu = input("Zadejte název úkolu: ")
        popis_ukolu = input("Zadejte popis úkolu: ")

        if nazev_ukolu == "" or popis_ukolu == "":
            print("Název ani popis nesmí být prázdné. Zkuste to znovu prosím.")
        else:
            ukoly.append({"nazev": nazev_ukolu, "popis": popis_ukolu})
            print(f"Úkol '{nazev_ukolu}' byl přidán.")
            break

# Funkce pro zobrazení úkolu: volba 2
def zobrazit_ukoly():
    if ukoly:
        print("Seznam úkolů: ")
        i = 1
        for polozka in ukoly:
            print(str(i) + ". " + polozka.get("nazev") + " - " + polozka.get("popis"))
            i = i + 1
    else:
        print("Seznam úkolů je prázdný.")

# Funkce pro zobrazení úkolů: volba 3
def odstranit_ukol():
    chybova_zprava = "Zadané číslo není v seznamu úkolů."
    zobrazit_ukoly()
    print("\n")
    if ukoly:
        while True:
            try:
                smazani_ukolu = int(input("Zadejte číslo úkolu, který chcete odstranit: ")) - 1
            except:
                print(chybova_zprava)
                continue
    
            if len(ukoly) <= smazani_ukolu or smazani_ukolu < 0:
                print(chybova_zprava)
            else:
                print(f"Úkol {ukoly[smazani_ukolu]['nazev']} byl smazán.")
                ukoly.pop(smazani_ukolu)
                break

def hlavni_menu():
    chybova_zprava = "Zadejte číslici z možností 1 až 4."
    while True:
        print("\nSprávce úkolů - Hlavní menu")
        print('''
    1 - Přidat úkol
    2 - Zobrazit úkol
    3 - Odstranit úkol
    4 - Ukončit program\n''')

        try:
            cislo_ukolu = int(input("Vyberte možnost (1-4): "))
        except:
            print(chybova_zprava)
            continue

        print("\n")
        if cislo_ukolu == 1:
            pridat_ukol()
        elif cislo_ukolu == 2:
            zobrazit_ukoly()
        elif cislo_ukolu == 3:
            odstranit_ukol()
        elif cislo_ukolu == 4:
            print("Konec programu.")
            break
        else:
            print(chybova_zprava)

hlavni_menu()