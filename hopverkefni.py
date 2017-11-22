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
    val = int(input("veldu númer"))

    if val == 1:
        print("fótboltalið")
        fjoldiSpilanda = int(input("sláðu inn fjölda spilenda"))
        fjoldiLid = int(input("hvað eru margir í liði"))
        heild = fjoldiSpilanda/fjoldiLid
        print (int("liðafjöldi",heild))
        afgang = fjoldiSpilanda % fjoldiLid
        print(int("varamenn",afgang))

    elif val == 2:
        print("þversumma")

    elif val == 3:
        print("slæri blað steinn")

    elif val == 4:
        print("texti")
        setning = input("sláðu inn setningu")
        takn = ("æ","a","r")
        breyta = setning
        breyta = setning.replace(takn,"*")
        print(breyta)

    elif val == 5:
        print("heiltöur")
        listi = []
        for x in range(12):
            listi = (input("veldu þér tölu"))
            laegri = min(listi)
            print(laegri)
            staerri = max(listi)
            print(staerri)
            suma = sum(listi)
            print(suma)
            medal = suma//suma
            print(medal)



    elif val == 6:
        print("teningaspilið Craps")

    elif val == 7:
        print("Þyngdarstuðull")
        nafn = input("sláðu inn nafn")
        thyngd = input("sláðu inn þyngd")
        kyn = input("sláðu inn kk eða kvk")



        print("nafnið er", nafn)
        print("kynið þitt er", kyn)
        print("þyngdin er",thyngd)



    elif val == 8:
        print("Teningar")

    elif val == 9:
        print("byggingaupplýsingar")

    else:
        break







