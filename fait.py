#Les Fameux Import
import pickle
from  sty import *
from datetime import *
import os
import time
from datetime import date
from datetime import timedelta
from Verification import toutestla
from calendar import monthrange

gras='\033[1m'
rien='\033[0m'
Mounth=["Janvier","Février","Mars","Avril","Mai","Juin","Juillet","Aout","Septembre","Octobre","Novembre","Décembre"]

AJD=str(date.today())
reajd=date.today()
Hier= str(reajd-timedelta(days=1))
Demain= str(reajd-timedelta(days=-1))


#Fonction Utile

def jolisdatejournale(ladate):
    mois=Mounth[int(ladate[5:7])-1]
    lajolisdategrave=ladate[8:10]+" "+mois+" "+ladate[:4]
    return lajolisdategrave

def Lecdico(fich,nom):
    Fichier= open(f"{fich}/{nom}","rb")
    lol= pickle.load(Fichier)
    Fichier.close()
    return lol

def Ecrdico(fich,nom,quoi):
    Fichier= open(f"{fich}/{nom}","wb")
    pickle.dump(quoi,Fichier)
    Fichier.close()
    return
def Vérif(rep,le):
    lis=[["oui","non","yep"],["parfaite","bien","moyen","mal","désastreuse"],["agenda","journal"],["1","2","3","4","5"],
         ["ntm","tg","ta gueule","ftg","ferme ta gueule","ntr","nique ta race", "nique ta mere","salaud","fdp"],["1","2","3","menu","retour"]]
    if rep.lower() not in lis[le]:
        if le !=4 :
            print("La réponse que vous venez de donnez est fausse snif...".center(150))
        return 0
    return 1



#Les Fonction d'écriture et Lecture
def Sentiment():
    sor = 0
    while sor != 1:
        print("Comment ce passé votre journée ? (Parfaite, Bien, Moyen, Mal, Désastreuse)".center(150))
        allo = input("".center(75)).lower()
        sor = Vérif(allo, 1)

    if allo == "parfaite":
        print()
        print("OHOH, je crois que vous avez beaucoup a me racontez, vous".center(150))
        time.sleep(1)
        print(
            "Sa me fait extrèment plaisir de vous voir comme ça, c'est que vous tout vas bien et ça fait mon bonheur".center(
                150))
        time.sleep(1)

    elif allo == "bien":
        print()
        print("Nice, ça fait toujour plaisir d'entendre ça".center(150))
        time.sleep(1)
        print("Hate d'entendre ce que vous avez a me dire".center(150))
        time.sleep(1)
    elif allo == "moyen":
        print()
        print("Une Journée banal somme toute, c'est pas toujour mouvementé et heureusement :>".center(150))
        time.sleep(1)
        print("Quoi qu'il en soit, faut en parler du minimun eus donc venez donc".center(150))
        time.sleep(1)
    elif allo == "mal":
        print()
        print("Ah, ce sont des choses qui peuvent arrivé malheuresement".center(150))
        time.sleep(1)
        print("Mais quand cela arrive faut en parler avec des personne de confiance, je ne reste que un bot, mais je peux être la".center(150))
        time.sleep(1.3)
    else:
        print()
        print("Oh mon dieux, je suis vraiment térriblement désolé d'entendre ça".center(150))
        time.sleep(1)
        print("vous devez en parler a quelqu'un parent/ami/frére,soeur , Un vrai personne de confiance, mais je veux aussi vous écouter cher ami".center(150))
        time.sleep(1.3)

    return allo


def Ecriture(LosJournos, ou, fich, emo):
    if ou == "Journal":
        print()
        if emo == "":
            print("pour commencé déja".center(150))
            emo=Sentiment()
            print()


        if emo == "parfaite":
            letype="Une Journée parfaite :>"
            print("Bien parfait, je suis très intéresser par sa".center(150))
            time.sleep(0.5)
            print("Vous avez l'air de super humeur, dites moi ce qui vous avez arrivé pour que même un robot comme moi sente votre joie 💖".center(150))
            time.sleep(1)
        elif emo == "bien":
            letype="Une Bonne journée"
            print("Allons y, j'aime bien ça".center(150))
            time.sleep(0.5)
            print("Votre journée a l'air de cet plutot bien passée :>".center(150))
            time.sleep(1)
        elif emo == "moyen":
            letype="Une journée Classique"
            print("Allons y, toujours intéressant ça".center(150))
            time.sleep(0.5)
            print("Quelque soit les choses de cet journée il est toujours bien d'écrire dessus, même si 0 important au final sa l'est".center(150))
            time.sleep(1)
        elif emo == "mal":
            letype="Une Mauvaise Journée"
            print("AH OUI, parlez en moi, c'est bien".center(150))
            time.sleep(0.5)
            print("Il est toujours important de parler dans ses moment, ça donne des piste pour votre instropection :>".center(150))
            time.sleep(1)
        else:
            letype="Une très mauvaise journée snif"
            print("Merci beaucoup de vouloir en parlez avec moi".center(150))
            time.sleep(0.5)
            print("Et n'hésité pas sur les mot a utiliser, je suis un robot, je n'ai pas de sensibilité, dite moi tout ce qui c'est passé et surtout vos ressenti".center(150))
            time.sleep(1)
            print(" 🌟 ❤️ 🌠 💖 Courage cher ami et allons y :> 💖 🌠 ❤️ 🌟 ".center(150))
            print(1)

        fin=0
        while fin !=1:
            print("Raconteé moi donc en détail comment vous vous êtes senti ajd et pourquoi :>".center(150))
            print("si vous voulez annulé, écrivé seulement /")
            Dorime=input("\n")

            if Dorime == '/' or Dorime == "" or Dorime == " ":
                print('\n\n')

                sor=0
                while sor !=1:
                    print()
                    print("Vous êtes sur de pas vouloir écrire ajd, je pense clairement que c'est important ? (oui/non)".center(150))
                    sarep=input(''.center(75))
                    sor=Vérif(sarep,0)

                if sarep == "oui":

                    sor = 0
                    while sor != 1:
                        print()
                        print("Etes vous vraiment sur, sa serrai super de faire part de sa, vous pouvez pas tout portez seul ? (oui/non)".center(150))
                        sarep = input(''.center(75))
                        sor = Vérif(sarep, 0)

                    if sarep == "oui":
                        print("très bien j'insiste pas plus :>".center(150))
                        time.sleep(0.75)
                        print("Hésité pas a allez faire un tours dans le journal pour remplir sa".center(150))

                        if emo == "bien" or emo == "moyen" or emo == "mal":
                            ecr=Lecdico("Journal",fich)
                            ecr[LosJournos]="a écrire :>"
                            Ecrdico("Journal",fich,ecr)
                            fin=1
                            time.sleep(1)

                        else:
                            time.sleep(1.5)
                            print("...".center(150))
                            time.sleep(1)
                            print("...".center(150))
                            time.sleep(2)
                            print("J'ai changé d'avis...".center(150))
                            print("Je souhaite que vous me dite de suite comment vous allez au vus de ce que vous m'avez dis avant... donc".center(150))

                if sarep == "non":
                    print('\n')
                    print("Sa arrive de ce trompé, reprenons :>".center(150))

            elif Dorime == "rien" or Dorime == "nul" or Dorime == "rien de bien" or Dorime == "rien d'interessant":
                print('\n\n')
                print("Vous savez, quoi que vous aviez fait, vous avez forcément fait et surtout vous avez ressenti des sentiment, partagé donc".center(150))
                time.sleep(1)
                print("vous vous êtes pas dématarialisé pendant une journée entier, je veux tout entendre :>".center(150))
                time.sleep(1.5)
                print("reprenons donc".center(150))
                time.sleep(0.5)
                print()

            elif Vérif(Dorime,4) == 1:
                print('\n\n')
                print("Je vous pries, je suis la pour vous et vous ne pouvez pas me véxer".center(150))
                time.sleep(1)
                print("vous essayer de jouer au plus malin, mais j'aimerais que vous me parliez de vous :>".center(150))
                time.sleep(1.5)
                print("Reprenons s'il vous plait".center(150))
                time.sleep(0.5)
                print()

            else:
                print('\n\n')
                print("Mhh.. Je vois on ma l'air d'être bon :>".center(150))
                time.sleep(1.3)
                print("Merci de m'avoir fait part de ça, si vous voulez consulté, hésité pas je grade tout, c'est la pour ça".center(150))
                time.sleep(1.3)
                fin=1
                ecr=Lecdico("Journal",fich)
                ecr[LosJournos]=[letype,Dorime]
                Ecrdico("Journal",fich,ecr)

    else:
        print()
        print("Parfait, allons y".center(150))
        fin = 0
        while fin != 1:
            print("Raconteé moi donc ce que vous avez fait ajd :>".center(150))
            print("si vous voulez annulé, écrivé seulement /")
            Dorime = input("\n")

            if Dorime == '/' or Dorime == "" or Dorime == " ":
                print('\n\n')

                sor = 0
                while sor != 1:
                    print()
                    print(
                        "Vous êtes sur de pas vouloir écrire ce que vous avez fait ajd, je pense que il y a des chose a dire, sur ? (oui/non)".center(150))
                    sarep = input(''.center(75))
                    sor = Vérif(sarep, 0)


                if sarep == "oui":
                    print("très bien j'insiste pas plus :>".center(150))
                    time.sleep(0.75)
                    print("Hésité pas a allez faire un tours dans 'remplir l'agenda' pour remplir sa".center(150))
                    ecr = Lecdico("Agenda", fich)
                    ecr[LosJournos] = "a écrire :>"
                    Ecrdico("Agenda", fich, ecr)
                    fin = 1
                    time.sleep(1)

                if sarep == "non":
                    print('\n')
                    print("Sa arrive de ce trompé, reprenons :>".center(150))

            elif Dorime == "rien" or Dorime == "nul" or Dorime == "rien de bien" or Dorime == "rien d'interessant":
                print('\n\n')
                print("Vous savez, quoi que vous aviez fait, vous avez forcément fait quelque choses,toujours intéressant de le dire".center(150))
                time.sleep(1)
                print("même si c'est que dormir, c'est toujours du repos vous savez".center(150))
                time.sleep(1.5)
                print("reprenons donc".center(150))
                time.sleep(0.5)
                print()

            elif Vérif(Dorime,4) == 1:
                print('\n\n')
                print("Je vous pries, je suis la pour vous et vous ne pouvez pas me véxer".center(150))
                time.sleep(1)
                print("vous essayer de jouer au plus malin, mais j'aimerais que vous me parliez de vous :>".center(150))
                time.sleep(1.5)
                print("Reprenons s'il vous plait".center(150))
                time.sleep(0.5)
                print()

            else:
                print('\n\n')
                print("Mhh.. intéressant, bien parfait".center(150))
                time.sleep(1.3)
                print("Je vous Note ça dans l'agenda si jamais vous voulez le relire :>".center(150))
                time.sleep(1.3)
                fin=1
                ecr=Lecdico("Agenda",fich)
                ecr[LosJournos]=Dorime
                Ecrdico("Agenda",fich,ecr)


def quinzejour(donc,ici):
    Quinze=[]
    for f in range(15):
        if not f == 0 :
            xd=str(reajd-timedelta(days=f))
            Quinze.append(xd)


    if donc == "Journal":
        Jj=Lecdico("Journal",ici)

        letoutjj=""
        labonnejj=30
        listejj=[]
        for cleejj in Quinze:
            if cleejj not in Jj.keys():
                listejj.append(cleejj)
                if labonnejj >= Quinze.index(cleejj):
                    labonnejj=Quinze.index(cleejj)
                    letoutjj=cleejj
        labonnejj+=1
        return [letoutjj,labonnejj,listejj]

    Aa=Lecdico("Agenda",ici)
    letoutaa = ""
    labonneaa = 30
    listeaa=[]
    for cleeaa in Quinze:
        if cleeaa in Aa.keys():
            listeaa.append(cleeaa)
            if labonneaa >= Quinze.index(cleeaa):
                labonneaa = Quinze.index(cleeaa)
                letoutaa=cleeaa
    labonneaa+=1
    return [letoutaa,labonneaa,listeaa]












#Les Fonction du Menu
def Univer1Ecri(quoi,dos):
    jj=Lecdico(quoi,dos)


    if jj[AJD] != "a écrire :>":
        print()
        print("'On dirait que vous avez déja écrit ajd, donc pas d'inquiétude je garde ça".center(150))
        print("je vous renvois en arrier, encore merci pour sa, hésité pas a allez regarder".center(150))
        return

    Ecriture(AJD,quoi,dos,"")
    return



def Univer2Ecri(quoi):
    laraison=Lecdico("Data","Raison.txt")
    lancer=laraison["Lancement"]


    Quinze=[]
    for f in range(15):
        if not f == 0 and not lancer in Quinze:
            xd=str(reajd-timedelta(days=f))
            Quinze.append(xd)

    if lancer == AJD:
        print()
        print("Je craint ue vous ayez lancer pour la première fois Fate Aujourd'hui ou que vous ayez rencontrez des soucis récement avec".center((150)))
        print("désolé, je vous renvois en arriers".center(150))
        return


    else:
        Quinze.pop(-1)

        for i in Quinze:
            cestla = Mounth[int(i[5:7]) - 1] + str(i[:4]) + ".txt"
            etoui=Lecdico(quoi,cestla)
            if i in etoui :
                if etoui[i] != "a écrire :>":
                    Quinze.pop(Quinze.index(i))


        voilala=0
        theend=0
        while theend != 1 :
            jpp=[]
            lol=0
            sor = 0

            print()
            time.sleep(1)
            print("Voici les jours qui n'ont rien d'écrit :>".center(150))
            for j in Quinze:
                lol += 1
                print(f"{lol}- {jolisdatejournale(j)}".center(150))
                jpp.append(lol)
                time.sleep(0.5)

            lol += 1
            print(f"{lol}- Quitez".center(150))
            jpp.append(lol)

            while sor != 1:

                print("dans quel jour voulez vous écrire ?".center(150))
                rep=input("".center(75))
                if int(rep) not in jpp:
                    print("La réponse que vous venez de donnez est fausse snif...".center(150))
                else:
                    sor=1


            rep=int(rep)
            if rep == jpp[-1]:
                time.sleep(0.5)
                print("Très bien, je vous laisse retourner en Arriers :>".center(150))
                return

            else:
                letruc=Quinze[rep-1]
                cestla = Mounth[int(letruc[5:7]) - 1] + str(letruc[:4]) + ".txt"
                etoui = Lecdico(quoi, cestla)
                if letruc in etoui:
                    if etoui[letruc] != "a écrire :>":
                        print()
                        print("On dirait que vous avez déja écrit pour ce jour la :>".center(150))

                    else:
                        print()
                        print("Très bien, je vous ouvre le Journal, pas de soucis".center(150))
                        time.sleep(1)
                        print("...".center(150))
                        time.sleep(1.5)
                        print("Let's go :>".center(150))
                        Ecriture(letruc, quoi, cestla, "")
                        voilala += 1


                else:
                    print()
                    print("Très bien, je vous ouvre le Journal, pas de soucis".center(150))
                    time.sleep(1)
                    print("...".center(150))
                    time.sleep(1.5)
                    print("Let's go :>".center(150))
                    Ecriture(letruc,quoi,cestla,"")
                    voilala += 1



def Univers3Lec(dossier,fichier):
    ecrit=fichier[:-4]
    print()
    print("Ouverture de Fate".center(150))
    time.sleep(1.3)
    print("...".center(150))
    time.sleep(1)
    print(f"Ouverture : {ecrit} .. je crois".center(150))
    time.sleep(1.5)

    laraison=Lecdico("Data","Raison.txt")
    lancer=laraison["Lancement"]

    Quinze=[]
    for f in range(15):
        if not f == 0 and not lancer in Quinze:
            xd=str(reajd-timedelta(days=f))
            Quinze.append(xd)


    nombredej= monthrange(int(ecrit[-4:]),Mounth.index(ecrit[:-4])+1)
    Firsst=nombredej[0]
    nombredej=nombredej[1]

    jour=" |   Lundi   |   Mardi   | Mercredi  |   Jeudi   | Vendredi  |  Samedi   | Dimanche  |\n"
    ligne="-------------------------------------------------------------------------------------\n"
    suite="|           |           |           |           |           |           |           |\n"
    # Incomplet |  Complet  | a remplir |  a venir  |

    letout=[]

    un="|"
    epi1="|"
    for i in range(Firsst):
        un+="   avant   |"
        epi1+="           |"


    moisnum=Mounth.index(ecrit[:-4])+1
    if moisnum < 10 :
        moisnum="0"+str(moisnum)


    ledico=Lecdico(dossier,fichier)
    for j in range(7-Firsst):
        un+="   "+"0"+str(j+1)+"/"+str(moisnum)+"   |"
        letout.append("0"+str(j+1)+"/"+str(moisnum))

        vérif=ecrit[-4:]+"-"+str(moisnum)+"-"+"0"+str(j+1)

        if vérif in ledico:
            if ledico[vérif] != "a écrire :>":

                lolo=ledico[vérif][0]

                if lolo == "Une très mauvaise journée snif":
                    epi1+=f"  {fg(25)}{gras}Complet{rien}{fg.rs}  |"
                elif lolo == "Une Bonne journée":
                    epi1+=f"  {fg(124)}{gras}Complet{rien}{fg.rs}  |"
                elif lolo == "Une journée Classique":
                    epi1+=f"  {fg(11)}{gras}Complet{rien}{fg.rs}  |"
                elif lolo == "Une Mauvaise Journée":
                    epi1+=f"  {fg(22)}{gras}Complet{rien}{fg.rs}  |"
                else :
                    epi1+=f"  {fg(54)}{gras}Complet{rien}{fg.rs}  |"

            elif vérif in Quinze:
                epi1+=f" {fg(15)}{gras}a remplir{fg.rs}{rien} |"

            else :
                epi1+=f" {fg(243)}{gras}Incomplet{fg.rs}{rien} |"

        elif vérif in Quinze:
            epi1 += f" {fg(15)}{gras}a remplir{fg.rs}{rien} |"

        else:
            if AJD[5:7] == moisnum and int(AJD[8:10]) < int(vérif[8:10]):
                epi1 += f"  {fg(5)}a venir{fg.rs}  |"
            else:
                epi1 += f" {fg(243)}{gras}Incomplet{fg.rs}{rien} |"

    un+="\n"
    epi1+="\n"



    deux="|"
    epi2="|"

    bra=int(7-Firsst)
    for k in range(7):
        bra+=1

        if bra < 10 :
            deux += "   " + "0" + str(bra) + "/" + str(moisnum) + "   |"
            letout.append("0" + str(bra) + "/" + str(moisnum))
            vérif = ecrit[-4:] + "-" + str(moisnum) + "-" + "0" + str(bra)
        else:
            deux += "   " + str(bra) + "/" + str(moisnum) + "   |"
            letout.append(str(bra) + "/" + str(moisnum))
            vérif = ecrit[-4:] + "-" + str(moisnum) + "-" + str(bra)


        if vérif in ledico:
            if ledico[vérif] != "a écrire :>":

                lolo=ledico[vérif][0]

                if lolo == "Une très mauvaise journée snif":
                    epi2+=f"  {fg(25)}{gras}Complet{rien}{fg.rs}  |"
                elif lolo == "Une Bonne journée":
                    epi2+=f"  {fg(124)}{gras}Complet{rien}{fg.rs}  |"
                elif lolo == "Une journée Classique":
                    epi2+=f"  {fg(11)}{gras}Complet{rien}{fg.rs}  |"
                elif lolo == "Une Mauvaise Journée":
                    epi2+=f"  {fg(22)}{gras}Complet{rien}{fg.rs}  |"
                else :
                    epi2+=f"  {fg(54)}{gras}Complet{rien}{fg.rs}  |"

            elif vérif in Quinze:
                epi2 += f" {fg(15)}{gras}a remplir{fg.rs}{rien} |"

            else:
                epi2 += f" {fg(243)}{gras}Incomplet{fg.rs}{rien} |"

        elif vérif in Quinze:
            epi2 += f" {fg(15)}{gras}a remplir{fg.rs}{rien} |"

        else:
            if int(AJD[5:7]) == int(moisnum) and int(AJD[8:10]) < int(vérif[8:10]):
                epi2 += f"  {fg(5)}a venir{fg.rs}  |"
            else:
                epi2 += f" {fg(243)}{gras}Incomplet{fg.rs}{rien} |"

    deux += "\n"
    epi2 += "\n"


    trois="|"
    epi3="|"

    for l in range(7):
        bra+=1

        if bra < 10 :
            trois += "   " + "0" + str(bra) + "/" + str(moisnum) + "   |"
            letout.append("0" + str(bra) + "/" + str(moisnum))
            vérif = ecrit[-4:] + "-" + str(moisnum) + "-" + "0" + str(bra)
        else:
            trois += "   " + str(bra) + "/" + str(moisnum) + "   |"
            letout.append( str(bra) + "/" + str(moisnum))
            vérif = ecrit[-4:] + "-" + str(moisnum) + "-" + str(bra)


        if vérif in ledico:
            if ledico[vérif] != "a écrire :>":

                lolo=ledico[vérif][0]

                if lolo == "Une très mauvaise journée snif":
                    epi3+=f"  {fg(25)}{gras}Complet{rien}{fg.rs}  |"
                elif lolo == "Une Bonne journée":
                    epi3+=f"  {fg(124)}{gras}Complet{rien}{fg.rs}  |"
                elif lolo == "Une journée Classique":
                    epi3+=f"  {fg(11)}{gras}Complet{rien}{fg.rs}  |"
                elif lolo == "Une Mauvaise Journée":
                    epi3+=f"  {fg(22)}{gras}Complet{rien}{fg.rs}  |"
                else :
                    epi3+=f"  {fg(54)}{gras}Complet{rien}{fg.rs}  |"

            elif vérif in Quinze:
                epi3 += f" {fg(15)}{gras}a remplir{fg.rs}{rien} |"

            else:
                epi3 += f" {fg(243)}{gras}Incomplet{fg.rs}{rien} |"

        elif vérif in Quinze:
            epi3 += f" {fg(15)}{gras}a remplir{fg.rs}{rien} |"

        else:
            if int(AJD[5:7]) == int(moisnum) and int(AJD[8:10]) < int(vérif[8:10]):
                epi3 += f"  {fg(5)}a venir{fg.rs}  |"
            else:
                epi3 += f" {fg(243)}{gras}Incomplet{fg.rs}{rien} |"

    trois += "\n"
    epi3 += "\n"


    quatre="|"
    epi4="|"

    for m in range(7):
        bra+=1

        if bra < 10 :
            quatre += "   " + "0" + str(bra) + "/" + str(moisnum) + "   |"
            letout.append("0" + str(bra) + "/" + str(moisnum))
            vérif = ecrit[-4:] + "-" + str(moisnum) + "-" + "0" + str(bra)
        else:
            quatre += "   " + str(bra) + "/" + str(moisnum) + "   |"
            letout.append( str(bra) + "/" + str(moisnum))
            vérif = ecrit[-4:] + "-" + str(moisnum) + "-" + str(bra)


        if vérif in ledico:
            if ledico[vérif] != "a écrire :>":

                lolo=ledico[vérif][0]

                if lolo == "Une très mauvaise journée snif":
                    epi4+=f"  {fg(25)}{gras}Complet{rien}{fg.rs}  |"
                elif lolo == "Une Bonne journée":
                    epi4+=f"  {fg(124)}{gras}Complet{rien}{fg.rs}  |"
                elif lolo == "Une journée Classique":
                    epi4+=f"  {fg(11)}{gras}Complet{rien}{fg.rs}  |"
                elif lolo == "Une Mauvaise Journée":
                    epi4+=f"  {fg(22)}{gras}Complet{rien}{fg.rs}  |"
                else :
                    epi4+=f"  {fg(54)}{gras}Complet{rien}{fg.rs}  |"

            elif vérif in Quinze:
                epi4 += f" {fg(15)}{gras}a remplir{fg.rs}{rien} |"

            else:
                epi4 += f" {fg(243)}{gras}Incomplet{fg.rs}{rien} |"

        elif vérif in Quinze:
            epi4 += f" {fg(15)}{gras}a remplir{fg.rs}{rien} |"

        else:
            if int(AJD[5:7]) == int(moisnum) and int(AJD[8:10]) < int(vérif[8:10]):
                epi4 += f"  {fg(5)}a venir{fg.rs}  |"
            else:
                epi4 += f" {fg(243)}{gras}Incomplet{fg.rs}{rien} |"

    quatre += "\n"
    epi4 += "\n"


    cinq="|"
    epi5="|"

    roule=nombredej-(4*7)+Firsst
    for n in range(roule):
        bra += 1

        if bra < 10:
            cinq += "   " + "0" + str(bra) + "/" + str(moisnum) + "   |"
            letout.append("0" + str(bra) + "/" + str(moisnum))
            vérif = ecrit[-4:] + "-" + str(moisnum) + "-" + "0" + str(bra)
        else:
            cinq += "   " + str(bra) + "/" + str(moisnum) + "   |"
            letout.append( str(bra) + "/" + str(moisnum))
            vérif = ecrit[-4:] + "-" + str(moisnum) + "-" + str(bra)

        if vérif in ledico:
            if ledico[vérif] != "a écrire :>":

                lolo=ledico[vérif][0]

                if lolo == "Une très mauvaise journée snif":
                    epi5+=f"  {fg(25)}{gras}Complet{rien}{fg.rs}  |"
                elif lolo == "Une Bonne journée":
                    epi5+=f"  {fg(124)}{gras}Complet{rien}{fg.rs}  |"
                elif lolo == "Une journée Classique":
                    epi5+=f"  {fg(11)}{gras}Complet{rien}{fg.rs}  |"
                elif lolo == "Une Mauvaise Journée":
                    epi5+=f"  {fg(22)}{gras}Complet{rien}{fg.rs}  |"
                else :
                    epi5+=f"  {fg(54)}{gras}Complet{rien}{fg.rs}  |"

            elif vérif in Quinze:
                epi5 += f" {fg(15)}{gras}a remplir{fg.rs}{rien} |"

            else:
                epi5 += f" {fg(243)}{gras}Incomplet{fg.rs}{rien} |"

        elif vérif in Quinze:
            epi5 += f" {fg(15)}{gras}a remplir{fg.rs}{rien} |"

        else:
            if int(AJD[5:7]) == int(moisnum) and int(AJD[8:10]) < int(vérif[8:10]):
                epi5 += f"  {fg(5)}a venir{fg.rs}  |"
            else:
                epi5 += f" {fg(243)}{gras}Incomplet{fg.rs}{rien} |"


    for o in range(7-roule):
        cinq +="   après   |"
        epi5 +="           |"


    cinq += "\n"
    epi5 += "\n"

    encoreunefin=0
    while encoreunefin != 1 :
        print("\n")
        print(jour,ligne,suite,un,epi1,ligne,suite,deux,epi2,ligne,suite,trois,epi3,ligne,suite,quatre,epi4,ligne,suite,cinq,epi5,ligne)

        print()
        time.sleep(0.5)
        print(f"quel jour voulez vous lire ? (ex : 04/{moisnum})".center(150))
        print('si vous voulez retournez en arrier écrivez "Retour"'.center(150))
        celui=input("".center(75))


        if celui.lower() == "retour" or celui.lower()== "menu":
            print()
            print("Noté, je vous renvois au Menu :> ".center(150))
            encoreunefin=1
            time.sleep(0.75)

        elif celui in letout:
            check=ecrit[-4:]+"-"+str(moisnum)+"-"+str(celui[:2])

            if check in ledico:
                if ledico[check] != "a écrire :>":

                    print("\n\n")

                    lolo=ledico[check][0]
                    if lolo == "Une très mauvaise journée snif":
                        print(f"{fg(111)}{jolisdatejournale(check)}{fg.rs}".center(170))
                        print(f"{fg(25)}{gras}{lolo}{fg.rs}{rien}".center(175))
                    elif lolo == "Une Bonne journée":
                        print(f"{fg(124)}{jolisdatejournale(check)}{fg.rs}".center(170))
                        print(f"{fg(88)}{gras}{lolo}{fg.rs}{rien}".center(175))
                    elif lolo == "Une journée Classique":
                        print(f"{fg(11)}{jolisdatejournale(check)}{fg.rs}".center(170))
                        print(f"{fg(3)}{gras}{lolo}{fg.rs}{rien}".center(175))
                    elif lolo == "Une Mauvaise Journée":
                        print(f"{fg(34)}{jolisdatejournale(check)}{fg.rs}".center(170))
                        print(f"{fg(22)}{gras}{lolo}{fg.rs}{rien}".center(175))
                    else:
                        print(f"{fg(54)}{jolisdatejournale(check)}{fg.rs}".center(170))
                        print(f"{fg(92)}{gras}{lolo}{fg.rs}{rien}".center(175))


                    print()
                    compte=0
                    acrire=""
                    tiret=0
                    for jpp in ledico[check][1]:
                        compte+=1
                        tiret+=1
                        acrire+=jpp

                        if compte == 125:
                            compte=0
                            if ledico[check][1][tiret] == ",":
                                acrire+=","
                            elif jpp != " " and ledico[check][1][tiret] != " ":
                                acrire+="-"
                            print(acrire.center(150))
                            acrire=""
                    print(acrire.center(150))

                    print("(pour quittez appuyez sur entrer :>)")
                    input("")

                elif check in Quinze:
                    print()
                    print("Il n'y a encore rien d'écrit a se jour, mais hésité pas a allez remplir tant que c'est disponible :>".center(150))
                    time.sleep(0.75)

                else:
                    print()
                    print("Malheuresement, ce jour est déja passé et vous n'avez rien eus a me dire snif".center(150))
                    time.sleep(0.75)

            elif check in Quinze:
                print()
                print("Il n'y a encore rien d'écrit a se jour, mais hésité pas a allez remplir tant que c'est disponible :>".center(150))
                time.sleep(0.75)

            else:
                if int(AJD[5:7]) == int(moisnum) and int(AJD[8:10]) < int(check[8:10]):
                    print()
                    print(f"ce jour n'est pas encore arrivé, n'oubliez de venir me voir le {celui} <3".center(150))
                    time.sleep(0.75)
                else:
                    print()
                    print("Malheuresement, ce jour est déja passé et vous n'avez rien eus a me dire snif".center(150))
                    time.sleep(0.75)

        else:
            print()
            print("La réponse que vous venez de donnée n'a pas de jour associez, désolé".center(150))
            time.sleep(0.75)



def Univers4lec(dossier):
    fichiers = [f for f in os.listdir(f"../Fate (En Pause (projet partiellement fini))/{dossier}") if os.path.isfile(os.path.join(f"../Fate (En Pause (projet partiellement fini))/{dossier}", f))]

    print()
    print("Recherche des dossier disponnible".center(150))
    time.sleep((1))

    end=0
    while end != 1:
        disp=0
        ouai=[]
        toutou=[]
        print()
        print("voici les Mois disponible :".center(150))
        for i in fichiers:
            disp+=1
            ouai.append(str(disp))
            toutou.append(i)
            print(f"{disp}- {i[:-4]}".center(150))
        disp+=1
        ouai.append(str(disp))
        print(f"{disp}- Quittez".center(150))

        soso=0
        while soso != 1:
            print("Que souhaitez vous faire ?".center(150))
            larep=input("".center(75))

            if not larep in ouai:
                print('je crois bien, que la réponse que vous venez de donner conrepont a rien snif'.center(150))

            else:
                soso =1

        if larep == ouai[-1]:
            print("Notez, je vous renvois au Menu :>".center(150))
            end = 1
            soso = 1

        else:
            print("je vous l'ouvre".center(150))
            time.sleep(1)

            Univers3Lec(dossier,toutou[int(larep)-1])

            print("\n")
            sor=0
            while sor !=1 :
                print("Voulez vous continuez a lire les Archive ? (oui/non)".center(150))
                mmhh=input("".center(75))
                sor=Vérif(mmhh,0)

            if mmhh.lower()=="non":
                print()
                print("Notez, merci d'avoir regarder les Archive avec moi :>".center(150))
                end=1
                time.sleep(1)

            else:
                print()
                print("Très bien continuons :>".center(150))
                time.sleep(1)