#Les Fameux Import
import pickle
from  sty import *
from datetime import *
import os
import time
from datetime import date
from datetime import timedelta
from Verification import toutestla
from fait import *

gras='\033[1m'
rien='\033[0m'
Mounth=["Janvier","Février","Mars","Avril","Mai","Juin","Juillet","Aout","Septembre","Octobre","Novembre","Décembre"]

AJD=str(date.today())
reajd=date.today()
Hier= str(reajd-timedelta(days=1))
Demain= str(reajd-timedelta(days=-1))


#Des Fonction Utilse pour pas se répéter
def jolisdatetout(ladate):
    lajolisdate="("+ladate[8:10]+"/"+ladate[5:7]+"/"+ladate[:4]+")"
    return lajolisdate

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











#Lancement de Fate/ demande du mot de Passe
if not os.path.isdir("../Fate (En Pause (projet partiellement fini))/Data"):
    os.mkdir('Data')
    vide={}
    rais={}
    rais["Lancement"]=AJD
    mdp="Millénia"
    Ecrdico("Data","Intru.txt",vide)
    Ecrdico("Data","Raison.txt",vide)
    fichier=open("Data/Mdp.txt","w")
    fichier.write(mdp)
    fichier.close()

fichier=open("Data/Mdp.txt","r")
Mdp=fichier.read()
fichier.close()
intru=Lecdico("Data","Intru.txt")


AJD=str(date.today())
reajd=date.today()
Hier= str(reajd-timedelta(days=1))
Demain= str(reajd-timedelta(days=-1))



print("Fate".center(150))
print("Lancement du Programme".center(150))
tantative=input("\nVeuillez entrer le mot de passe : ".center(25))

tant=0
end = 0
while end == 0 :
    tant += 1
    if tantative == Mdp:
        end+=1
    if tant == 3 :
        imposter = ["KYLACREA", 'KYLA', "KYLA CREA", "TEDDY", "TEDDUS", "", " ", "PUTE", "FATE"]
        print("... Il semblerais que vous êtes un imposteur, qui que vous soyez, vous êtes bien audacieux\n"
              "de vouloir fourré votre nez dans les Affaires de Kyla... qui êtes vous ?")
        retien=input(f"{gras}{fg.red}Qui êtes vous ? {fg.rs}{rien}")
        if retien.upper() in imposter :
            print(f"...Je vois... vous allez jusqu'a vous moquez de moi ici encore soit..."
                  f"{fg(124)}{gras} Allez vous en loin{rien}{fg.rs}")
            quit()
        else:
            intru[AJD]=retien
            Ecrdico("Data","Intru.txt",intru)
            print(f"Merci d'avoir laissez votre nom\n"
                  f"si jamais vous voulez vraiment entrez dedans et voir tout sa demandez l'autorisation a Kyla/Teddy, s'il vous pait\n"
                  f"{fg(55),gras} Bonne Journée/Soirée :>")
            quit()
    if tantative != Mdp :
        print(f"{gras}{fg.red}Faux{fg.rs}{rien}\nIl ne vous reste que {3-tant} avant la fermeture de Fate")
        tantative = input("\nVeuillez entrer le mot de passe : ".center(25))


#Analise des donnée de Fate
print("Fate Analise les donnée a sa disposition".center(150))
time.sleep(0.5)
print("...".center(150))
time.sleep(0.5)

toutestla(AJD)


#Vérification des Donné et du lancement a appliqué
rais=Lecdico("Data","Raison.txt")
Dateraison=rais["Lancement"]
Aujourdhui = jolisdatetout(AJD)
ici = Mounth[int(Aujourdhui[4:6]) - 1] + Aujourdhui[7:11] + '.txt'

etla = Mounth[int(Aujourdhui[4:6]) - 2]
if etla == "Décembre":
    etla = "Décembre" + str(int(Aujourdhui[7:11]) - 1) + '.txt'
else:
    etla = etla + Aujourdhui[7:11] + '.txt'


j=Lecdico("Journal",ici)
a=Lecdico("Agenda",ici)

dateagenda=[]
datejournal=[]

for lol in j.keys():
    datejournal.append(lol)
for lol in a.keys():
    dateagenda.append(lol)

if Dateraison != AJD :
    raa=quinzejour("Agenda",ici)
    rjj=quinzejour("Journal",ici)

    letoutaa=raa[0]
    labonneaa=raa[1]
    letoutjj=rjj[0]
    labonnejj=rjj[1]


    if letoutaa != "" or letoutjj != "":
        if not AJD in dateagenda and not AJD in datejournal:
            print()
            time.sleep(0.5)
            print("En récupérant les données nécessaires au lancement, je me suis apperçu que vous n'aviez rien dis ces dernier jour".center(150))
            time.sleep(1)
            if letoutjj != "":
                print(f"Vous n'avez pas écrit dans votre journal depuis le {letoutjj}, je vous invite a remplire les donnée des {labonnejj} dernier jour".center(150))
            if letoutaa != "":
                print(f"Vous n'avez pas écrit dans votre agenda depuis le {letoutaa}, je vous invite a remplire les donnée des {labonneaa} dernier jour".center(150))
            time.sleep(2)
            print("Vous pouvez remplir sa dans 'Remplir l'agenda'".center(150))



#Lancement et Demande sur comment ce passe la journée du propriétaire
print()
print()
time.sleep(0.5)
print("Lancement de Fate".center(150))
time.sleep(1)
print("...".center(150))
time.sleep(1)

#Si rien écrit encore ajd, Comment ça va, et ecrit
if not AJD in dateagenda and not AJD in datejournal:
    print("Boujour, Bonsoir".center(150))
    time.sleep(0.5)
    print("Content de vous voir aujourd'hui :>".center(150))
    time.sleep(0.75)

    allo=Sentiment()

    sor=0
    while sor !=1:
        print("voulez vous écrire dans l'agenda ce que vous avez fait ajd ou dans le Journal sur comment vous vous sentez ajd ? (oui, non)".center(150))
        que=input("".center(75))
        sor=Vérif(que,0)

    if que == "non":
        print("Très, je serrais vraiment ravis que vous alliez remplir tout les truc d'ajd vous savez :>" .center(150))
        print("Je vous laisse faire ce qui vous plait :>".center(150))
        print()
        j=Lecdico("Journal",ici)
        a=Lecdico("Agenda",ici)
        j[AJD]="a écrire :>"
        a[AJD]="a écrire :>"
        Ecrdico("Journal",ici,j)
        Ecrdico("Agenda",ici,a)

    else:
        print()
        print("Très bien, Commençons par sa tout de suite :>".center(150))

        sor=0
        while sor !=1 :
            print("Voulez vous commencé par l'Agenda ou le Journal ? (agenda/journal)".center(150))
            que=input("".center(75)).lower()
            sor=Vérif(que,2)

        if que == "journal":
            Ecriture(AJD,"Journal",ici, allo)
            print("\n")

            sor=0
            while sor !=1:
                print("Voulez vous écrire dans l'Agenda ? (oui/non)".center(150))
                yep=input("".center(75))
                sor=Vérif(yep,0)

            if yep == "oui":
                Ecriture(AJD, "Agenda", ici, allo)
            else:
                print()
                print("Pas de soucis, hésité pas a allez remplir sa directement dans 'Remplir L'agenda'".center(150))

        if que == "agenda":
            Ecriture(AJD,"Agenda",ici, allo)
            print("\n")

            sor=0
            while sor !=1:
                print("Voulez vous écrire dans le Journal ? (oui/non)".center(150))
                yep=input("".center(75))
                sor=Vérif(yep,0)

            if yep == "oui":
                Ecriture(AJD, "Journal", ici, allo)
            else:
                print()
                print("Pas de soucis, hésité pas a allez remplir sa directement dans 'Journal'".center(150))


#LE MENUUUUUU C'EST GRAND MORT
print("\n\n\n\n")
print("BIENVENU DANS FATE".center(150))
time.sleep(1)
print(" votre espace rien que a vous".center(150))
aurevoir=0

while aurevoir !=1:

    sor=0
    while sor != 1:
        print("")
        print("1- Mon Univers".center(150))
        time.sleep(0.5)
        print("2- Mon Agenda".center(150))
        time.sleep(0.5)
        print("3- Paramètre".center(150))
        time.sleep(0.5)
        print("4- Le mode d'emplois".center(150))
        time.sleep(0.5)
        print("5- Ciao".center(150))
        print()
        print("que souhaitez vous faire ajd ? :>".center(150))
        lets=input("".center(75))
        sor=Vérif(lets,3)

    if lets== "5":
        print()
        print("Merci d'être passée faire un coucou :>".center(150))
        time.sleep(0.75)
        print("Je vous souhaite une bonne fin de Journée, courage et bonheur a vous 💖 ".center(150))
        time.sleep(1.25)
        quit()

    elif lets =="1":
        print('')

        retour=0
        while retour !=1:

            sor=0
            while sor !=1:
                print()
                print('1- Journal Intime'.center(150))
                time.sleep(0.5)
                print('2- Bilan de semaine (a faire)'.center(150))
                time.sleep(0.5)
                print("(pour retourner au Menu, écrire 'menu')".center(150))
                print("Bien de quoi allons nous discuter ?".center(150))
                ggnore=input(''.center(75))
                sor=Vérif(ggnore,5)

                if ggnore == "3" :
                    print("désolé, on dirait que il y a rien a faire sous le 3 snif".center(150))
                    time.sleep(0.75)
                    sor=0

            if ggnore == "menu" or ggnore == "retour":
                print()
                print("Yep, Compris, retournons en arriers".center(150))
                retour=1

            elif ggnore == "1":

                encorere=0
                while encorere != 1:
                    print("")
                    print("Ouverture de Votre Journal Intime".center(150))
                    time.sleep(1.5)
                    print("Voici :>".center(150))

                    sor=0
                    while sor !=1:
                        print()
                        print(f"1-Ecrire Aujourd'hui (le : {jolisdatejournale(AJD)} )".center(150))
                        time.sleep(0.5)
                        print("2- Ecrire les jours manqués".center(150))
                        time.sleep(0.5)
                        print(f"3- Lire les jours du mois de {Mounth[int(AJD[5:7])-1]}".center(150))
                        time.sleep(0.5)
                        print("4- Lire les jours d'un autre mois".center(150))
                        time.sleep(0.5)
                        print("Alors qu'alons nous faire?".center(150))
                        print("('Menu' pour retourner a l'accueil et 'Retour' pour retourner en arriers)".center(150))
                        yeyeye=input(''.center(75))

                        if yeyeye.lower() == "menu" or yeyeye.lower() == "retour":
                            sor=1

                        if sor !=1 :
                            sor=Vérif(yeyeye,3)

                        if yeyeye == "5":
                            print("désolé, on dirait que il y a rien a faire sous le 5 snif".center(150))
                            time.sleep(0.75)
                            sor = 0

                    if yeyeye=="1":
                        Univer1Ecri("Journal",ici)

                    elif yeyeye=="2":
                        Univer2Ecri("Journal")

                    elif yeyeye=="3":
                        Univers3Lec("Journal",ici)
                    elif yeyeye == "4":
                        Univers4lec("Journal")
                        #Faire la lecture et présetation d'un autre mois

                    elif yeyeye.lower() =="menu":
                        print()
                        print("Compris, je vous renvois au Menu :>".center(150))
                        time.sleep(1)
                        encorere=1
                        retour=1

                    else:
                        print()
                        print("Noté, je vous renvois en arriers :>".center(150))
                        time.sleep(0.75)
                        encorere=1

            elif ggnore == "2":

                encorere=0
                while encorere != 1 :
                    print("")
                    print("Ouverture es Archive de vos sentiement".center(150))
                    time.sleep(1.5)
                    print("Voici :>".center(150))

                    sor = 0
                    while sor != 1:
                        print()
                        print("1- Regarder vos emotion".center(150))
                        time.sleep(0.5)
                        print("2- Evolution".center(150))
                        time.sleep(0.5)
                        print("Alors qu'alons nous faire?".center(150))
                        print("('Menu' pour retourner a l'accueil et 'Retour' pour retourner en arriers)".center(150))
                        yeyeye = input(''.center(75))
                        sor= Vérif(yeyeye,5)

                        if yeyeye == "3":
                            print("désolé, on dirait que il y a rien a faire sous le 5 snif".center(150))
                            time.sleep(0.75)
                            sor = 0

                    if yeyeye == "1":
                        print("lolsaregardesec")
                        #Regarder emotion

                    elif yeyeye == "2":
                        print("Lolsaevolu")
                        #Faire l'évotlution de ça

                    elif yeyeye.lower() == "menu":
                        print()
                        print("Compris, je vous renvois au Menu :>".center(150))
                        time.sleep(1)
                        encorere = 1
                        retour = 1

                    else:
                        print()
                        print("Noté, je vous renvois en arriers :>".center(150))
                        time.sleep(0.75)
                        encorere = 1



    elif lets == "2":
        print('')

        retour = 0
        while retour != 1:

            sor = 0
            while sor != 1:
                print()
                print('1- Vos Notes'.center(150))
                time.sleep(0.5)
                print('2- Objectif'.center(150))
                time.sleep(0.5)
                print("3- Emplois du temps".center(150))
                time.sleep(0.5)
                print("(pour retourner au Menu, écrire 'menu')".center(150))
                print("Bien de quoi allons nous discuter ?".center(150))
                ggnore = input(''.center(75))
                sor = Vérif(ggnore, 5)

            if ggnore == "menu" or ggnore == "retour":
                print()
                print("Yep, Compris, retournons en arriers".center(150))
                retour = 1

            elif ggnore == "1":

                encorere = 0
                while encorere != 1:
                    print("")
                    print("Ouverture de Vos Notes".center(150))
                    time.sleep(1.5)
                    print("Voici :>".center(150))

                    sor = 0
                    while sor != 1:
                        print()
                        print(f"1-Ecrire Aujourd'hui (le : {jolisdatejournale(AJD)})".center(150))
                        time.sleep(0.5)
                        print("2- Ecrire les jours manqués".center(150))
                        time.sleep(0.5)
                        print("3- Lire les jours de ce mois ci".center(150))
                        time.sleep(0.5)
                        print("4- Lire les jours d'un autre mois".center(150))
                        time.sleep(0.5)
                        print("Alors qu'alons nous faire?".center(150))
                        print("('Menu' pour retourner a l'accueil et 'Retour' pour retourner en arriers)".center(150))
                        yeyeye = input(''.center(75))

                        if yeyeye.lower() == "menu" or yeyeye.lower() == "retour":
                            sor = 1

                        if sor != 1:
                            sor = Vérif(yeyeye, 3)

                        if yeyeye == "5":
                            print("désolé, on dirait que il y a rien a faire sous le 5 snif".center(150))
                            time.sleep(0.75)
                            sor = 0

                    if yeyeye == "1":
                        Univer1Ecri("Agenda",ici)

                    elif yeyeye == "2":
                        Univer2Ecri("Agenda")

                    elif yeyeye == "3":
                        print("lollit")
                        # faire la présentation et lecture des fichier

                    elif yeyeye == "4":
                        print("lollit")
                        # Faire la lecture et présetation d'un autre mois

                    elif yeyeye.lower() == "menu":
                        print()
                        print("Compris, je vous renvois au Menu :>".center(150))
                        time.sleep(1)
                        encorere = 1
                        retour = 1

                    else:
                        print()
                        print("Noté, je vous renvois en arriers :>".center(150))
                        time.sleep(0.75)
                        encorere = 1

            elif ggnore == "2":

                encorere = 0
                while encorere != 1:
                    print("")
                    print("Ouverture de vos Objecif".center(150))
                    time.sleep(1.5)
                    print("Voici :>".center(150))

                    sor = 0
                    while sor != 1:
                        print()
                        print("1- Regarder vos Objectif".center(150))
                        time.sleep(0.5)
                        print("2- Ajouter des Objecif".center(150))
                        time.sleep(0.5)
                        print("3- Modifier des Objectif".center(150))
                        time.sleep(0.5)
                        print("Alors qu'alons nous faire?".center(150))
                        print("('Menu' pour retourner a l'accueil et 'Retour' pour retourner en arriers)".center(150))
                        yeyeye = input(''.center(75))
                        sor = Vérif(yeyeye, 5)

                    if yeyeye == "1":
                        print("lolsaregardesec")
                        # Regarder Les Objecif

                    elif yeyeye == "2":
                        print("Lolsaevolu")
                        # Faire L'ecriture objectif

                    elif yeyeye == "3":
                        print("Modifiesalaud")
                        #Faire letruc pour modifier et tout

                    elif yeyeye.lower() == "menu":
                        print()
                        print("Compris, je vous renvois au Menu :>".center(150))
                        time.sleep(1)
                        encorere = 1
                        retour = 1

                    else:
                        print()
                        print("Noté, je vous renvois en arriers :>".center(150))
                        time.sleep(0.75)
                        encorere = 1

            elif ggnore == "3":

                encorere = 0
                while encorere != 1:
                    print("")
                    print("Ouverture de vos emplois du temps".center(150))
                    time.sleep(1.5)
                    print("Voici :>".center(150))

                    sor = 0
                    while sor != 1:
                        print()
                        print("1- Regarder vos emplois du temps".center(150))
                        time.sleep(0.5)
                        print("2- Crée un emplois du temps".center(150))
                        time.sleep(0.5)
                        print("3- Modifier vos emplois du temps".center(150))
                        time.sleep(0.5)
                        print("Alors qu'alons nous faire?".center(150))
                        print("('Menu' pour retourner a l'accueil et 'Retour' pour retourner en arriers)".center(150))
                        yeyeye = input(''.center(75))
                        sor = Vérif(yeyeye, 5)


                    if yeyeye == "1":
                        print("lolsaregardesec")
                        # Regarder les emplois du temps

                    elif yeyeye == "2":
                        print("Lolsaevolu")
                        # Faire les emplois du temps

                    elif yeyeye == "3":
                        print("Lolsas'emplois")
                        #modifier les emplois du temps

                    elif yeyeye.lower() == "menu":
                        print()
                        print("Compris, je vous renvois au Menu :>".center(150))
                        time.sleep(1)
                        encorere = 1
                        retour = 1

                    else:
                        print()
                        print("Noté, je vous renvois en arriers :>".center(150))
                        time.sleep(0.75)
                        encorere = 1


    elif lets == "3":
        print('')

        retour = 0
        while retour != 1:

            sor = 0
            while sor != 1:
                print()
                print('1- Le Mot de Passe'.center(150))
                time.sleep(0.5)
                print('2- Lire le Fichier des raison'.center(150))
                time.sleep(0.5)
                print("3- Goulag des intrus".center(150))
                time .sleep(0.5)
                print("(pour retourner au Menu, écrire 'menu')".center(150))
                print("Bien de quoi allons nous discuter ?".center(150))
                ggnore = input(''.center(75))
                sor = Vérif(ggnore, 5)

            if ggnore == "menu" or ggnore == "retour":
                print()
                print("Yep, Compris, retournons en arriers".center(150))
                retour = 1

            elif ggnore == "1":
                print("Lolles mdp")
                #Faire la modification du MDP

            elif ggnore == "2":
                print("LOLsaraisone")
                #faire l'affichage des raison

            else:
                print("Lol GOULAG")
                #Toute les personne mie au goulag


    else:
        print('')

        retour = 0
        while retour != 1:

            sor = 0
            while sor != 1:
                print()
                print("1- Mon Univers, c'est quoi ?".center(150))
                time.sleep(0.5)
                print('2- Mon Agenda, On y fait quoi ?'.center(150))
                time.sleep(0.5)
                print("3- Paramètre, a quoi sa sert ?".center(150))
                time.sleep(0.5)
                print("(pour retourner au Menu, écrire 'menu')".center(150))
                print("Bien de quoi allons nous discuter ?".center(150))
                ggnore = input(''.center(75))
                sor = Vérif(ggnore, 5)

            if ggnore == "menu" or ggnore == "retour":
                print()
                print("Yep, Compris, retournons en arriers".center(150))
                retour = 1

            elif ggnore == "1":
                print("Lolc'est quuoi un journale intime")
                # mode d'emplois journale intime

            elif ggnore == "2":
                print("LOLc'est quoi un agenda")
                # mode d'emplois agenda

            else:
                print("et des paramètre mmdr")
                # mode d'emplois paramètre

