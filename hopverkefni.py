#hopverkefni
#22.11.2017
#Oliver og Arnór
import random
svar = "ja"
while svar == "ja":
    print("1.Fótboltalið")
    print("2.Þversumma")
    print("3.skæri, blað steinn")
    print("4.texti")
    print("5.heiltölur")
    print("6.teningaspilið Craps")
    print("7.þyngadrstuðull")
    print("8.teningar")
    print("9.Byggingaupplýsingar úr Hópverkefni 1 ")
    print("10.hætta")
    val = int(input("veldu númer "))

    if val == 1:
        print("fótboltalið")
        fjoldiSpilanda = int(input("sláðu inn fjölda spilenda "))
        fjoldiLid = int(input("hvað eru margir í liði "))
        heild = int(fjoldiSpilanda/fjoldiLid)
        print ("liðafjöldi", heild)
        afgang = fjoldiSpilanda % fjoldiLid
        print ("varamenn",afgang)

    elif val == 2:
        print("þversumma")
        afram = True

        while afram:
            tala = int(input("Sláðu inn tölu: "))
            # Þegar notandinn velur 0
            if tala == 0:
                # þá hætta
                afram = False
            else:
                if (tala < 0):
                    teljari = 0
                    # telur afturábak
                    for x in range(tala, 0, 1):
                        teljari = teljari + x
                        print("(" + str(x) + ")", end="")
                        if (x != -1):
                            print("+", end="")
                    print(" =", teljari)
                else:
                    teljari = 0
                    for x in range(1, tala + 1, 1):
                        teljari = teljari + x
                        print(x, end="")
                        if (x != tala):
                            print("+", end="")
                    print(" =", teljari)
            print()

    elif val == 3:
        print("slæri blað steinn")
        nafn = input("Hvað heitir þú?: ")
        aldur = int(input("Hvað ertu gamall/gömul?: "))
        print()

        afram = True
        while afram:

            print("Skæri blað steinn, veldu")
            print("1. fyrir skæri")
            print("2. fyrir blað")
            print("3. fyrir stein")
            print("4. til að hætta")
            val = int(input("Veldu: "))

            hlutir = ["", "skæri", "blað", "steinn"]

            if val == 4:
                afram = False
            else:
                tolvan = random.randint(1, 3)
                if tolvan == val:
                    print("Jafntefli")
                elif (val == 1 and tolvan == 2) or (val == 2 and tolvan == 3) or (val == 3 and tolvan == 1):
                    print("Þú vannst! Þú gerðir", hlutir[val], "og tölvan reyndi", hlutir[tolvan])
                else:
                    print("Þú tapaðir! Þú reyndir", hlutir[val], "og tölvan gerði", hlutir[tolvan])

    elif val == 4:

        texti = input("Skrifaðu texta: ")
        listi = ["J", "j", "b", "l", "n", " "]

        utkoma = texti
        for x in texti:
            if listi.count(x) == 0:
                utkoma = utkoma.replace(x, "*")

        print(utkoma.replace(" ", "_"))

    elif val == 5:
        print("heiltöur")
        listi = []
        for x in range(12):
            tala = input("veldu tölu")



    elif val == 6:
        print("Teningaspilið")
        stada = "spila"

        stig = -1

        while stada == "spila":
            teningur1 = random.randint(1, 6)
            teningur2 = random.randint(1, 6)

            summa = teningur1 + teningur2

            print("Summan er", summa)
            if (summa == 7 and stig == -1) or summa == 11:

                stada = "sigur"
            elif (summa == 2 or summa == 3 or summa == 12) and stig == -1:
                stada = "tap"
            elif summa == 7 and stig != -1:

                stada = "tap"
            elif summa > 3:
                print("þú þarft að ná sömu summu til að vinna, og ekki fá 7 á meðan")
                stig = summa

        if stada == "tap":
            print("Þú tapaðir!")
        elif stada == "sigur":
            print("Þú vannst!")
        else:
            print("Hmm.. er þetta einhver villa?")



    elif val == 7:
        print("Þyngdarstuðull")
        nafn = input("Hvað heitir notandinn ? ")
        kyn = input("sláðu inn kk eða kvk ")
        thyngd = int(input("Hvað ertu þungur í kílóum ? "))
        head = int(input("sláðu inn hæð þína í metrum " + nafn))
        headd= head*head
        bmi = thyngd/headd
        bmi = bmi *10000
        print("hér er talan ", format(bmi, ".2f"))

        if bmi < 18.5 and bmi > 18.5:
            print("vannæring")

        elif bmi > 18.5 and bmi < 24.9:
            print("kjörþyngd")

        elif bmi > 25.0 and bmi < 29.9:
            print("ofþyngd")

        elif bmi > 30:
            print("offita")

        else:
            break







    elif val == 8:
        print("Teningar")
        kast = []

        for x in range(200):
            teningur1 = random.randint(1, 6)
            teningur2 = random.randint(1, 6)
            teningur3 = random.randint(1, 6)

            summa = teningur1 + teningur2 + teningur3

            kast.append(summa)

        strengur = ""
        for x in kast:
            strengur = strengur + str(x) + ", ";
        print("Listinn óraðaður:", strengur)
        kast.sort()

        strengur = ""
        for x in kast:
            strengur = strengur + str(x) + ", ";

        print("Listinn raðaður:", strengur)

        teljari = 0
        for x in kast:
            teljari = teljari + x;
        print("Summa:", str(teljari))
        print("Meðaltal:", str(teljari / 200))
        print("Summan 10 kom", kast.count(10), "sinnum")
        print("Summan 15 kom", kast.count(15), "sinnum")
        print("Summan 18 kom", kast.count(18), "sinnum")

    elif val == 9:
        print("byggingaupplýsingar")


    else:
        break







