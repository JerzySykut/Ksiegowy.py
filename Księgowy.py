import sys
dozwolone_operacje = ("saldo","zakup","sprzedaż","konto","magazyn","przegląd","stop")

operacje = []        #opercje do wydruku
towary = dict()      #operacje "magazyn"
wartosc_saldo = 0    #operacje "konto"

while True:
    argument = str(input())
    if argument not in dozwolone_operacje:
        print(("blad - nieznana operacja"))
        break
    if argument == "saldo":        #funkcja saldo
        operacje.append(argument)
        if wartosc_saldo:
            wartosc_saldo += int(input())
        else:
            wartosc_saldo = int(input())
        operacje.append(wartosc_saldo)
        komentarz = str(input())
        operacje.append(komentarz)
    elif argument == "zakup":
        indentyfikator = str(input())
        cena = int(input())
        liczba = int(input())
        if wartosc_saldo < cena*liczba:
            print("\nblad - saldo ujemne\n)")
            break
        operacje.append(argument)
        operacje.append(indentyfikator)
        operacje.append(cena)
        operacje.append(liczba)
        towary[indentyfikator] = liczba
        wartosc_saldo = wartosc_saldo - (cena*liczba)
    elif argument =="sprzedaż":

        indentyfikator = str(input())
        cena = int(input())
        liczba = int(input())
        if towary[indentyfikator] < liczba:
            print(f"\nstan towaru {indentyfikator} jest mniejszy od {liczba} \n")
            break
        operacje.append(argument)
        operacje.append(indentyfikator)
        operacje.append(cena)
        operacje.append(liczba)
        towary[indentyfikator] -= liczba
        wartosc_saldo = wartosc_saldo + (cena*liczba)
    elif argument == "stop":
        #operacje.append(argument)
        break
if len(sys.argv) > 1:
    argument = sys.argv[1]
    if argument == "saldo":
        if len(sys.argv) < 4:
            print("Bledna ilosc argumentow dla operacji saldo, powinno byc: saldo wartosc komentarz")
            exit()
        operacje.append(argument)
        if wartosc_saldo:
            wartosc_saldo += int(sys.argv[2])
        else:
            wartosc_saldo = int(sys.argv[2])
        operacje.append(wartosc_saldo)
        komentarz = sys.argv[3]
        operacje.append(komentarz)
    elif argument == "zakup":
        if len(sys.argv) < 5:
            print("Bledna ilosc argumentow dla operacji zakup, powinno byc: zakup nazwa_towaru cena ilosc")
            exit()
        indentyfikator = sys.argv[2]
        cena = int(sys.argv[3])
        liczba = int(sys.argv[4])
        if wartosc_saldo < cena*liczba:
            print("\nblad - saldo ujemne\n)")
            exit()
        operacje.append(argument)
        operacje.append(indentyfikator)
        operacje.append(cena)
        operacje.append(liczba)
        towary[indentyfikator] = liczba
        wartosc_saldo = wartosc_saldo - (cena*liczba)
    elif argument == "sprzedaż":
        if len(sys.argv) < 5:
            print("Bledna ilosc argumentow dla operacji sprzedaż, powinno byc: sprzedaż nazwa_towaru cena ilosc")
            exit()
        indentyfikator = sys.argv[2]
        cena = int(sys.argv[3])
        liczba = int(sys.argv[4])
        if towary[indentyfikator] < liczba:
            print(f"\nstan towaru {indentyfikator} jest mniejszy od {liczba} \n")
            exit()
        operacje.append(argument)
        operacje.append(indentyfikator)
        operacje.append(cena)
        operacje.append(liczba)
        towary[indentyfikator] -= liczba
        wartosc_saldo = wartosc_saldo + (cena * liczba)
    elif argument == "konto":
        operacje.append(argument)
        print(wartosc_saldo)
        exit()
    elif argument == "magazyn":
        if len(sys.argv) > 2:
            for i in range(2, len(sys.argv)):
                indentyfikator = sys.argv[i]
                print(f"{indentyfikator}:{towary[indentyfikator]}")
        exit()
    elif argument == "przegląd":
        # ??
        exit()
operacje.append("stop")
for i in operacje:
    print (i)
