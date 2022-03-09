#Les Fameux Import
import pickle
from  sty import *
from datetime import *
import os
import time
from datetime import date
from datetime import timedelta

gras='\033[1m'
rien='\033[0m'
Mounth=["Janvier","Février","Mars","Avril","Mai","Juin","Juillet","Aout","Septembre","Octobre","Novembre","Décembre"]

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
    lis=[["oui","non","yep"],["1","2","3","4","5","6","7","8"]]
    if rep.lower() not in lis[le]:
        print("La réponse que vous venez de donnez est fausse snif...".center(150))
        return 0
    return 1



def toutestla(AJD):
    if not os.path.isdir('../Fate (En Pause (projet partiellement fini))/Journal') or not os.path.isdir('../Fate (En Pause (projet partiellement fini))/Agenda'):
        sor = 0
        while sor != 1:
            print("Premier utilisation de Fate ? (oui/non)".center(150))
            perm = input("".center(75))
            sor = Vérif(perm, 0)

        # Si fichier suprimer
        if perm.lower() == "non":
            print("")
            print(
                "Dans ce cas, je ne vois pas la présence du dossier Journale, qui contient en tant normale le résumé".center(
                    160))
            print("des émotions que vous me faite part quotidiennement et vos acvivité journalière.".center(150))
            print("je suis inquiet et je pense que il est touours utilles d'en parler pour le vous futur".center(150))
            time.sleep(1.5)
            fin = 0
            while fin != 1:
                print("Pourquoi avez vous suprimez les dossiés comme cela ?\n".center(150))
                raison = input("")

                if raison == "":
                    sor = 0
                    while sor != 1:
                        print("Vous n'avez rien dis...".center(150))
                        time.sleep(0.33)
                        print("Vous êtes sur de pas vouloir en parler ? (oui/non)".center(150))
                        permi = input("".center(75))
                        sor = Vérif(permi, 0)

                    if permi.lower() == "non":
                        print()

                    if permi.lower() == "oui":
                        print()
                        print("Pourquoi ? qu'est ce qui vous tracasse ?\n".center(150))
                        raison = input("")

                        if raison == "":
                            print(
                                "Bon, je comprend ta non envie d'en parler, je suis désolé de vous avoir ennuyez avec sa".center(
                                    150))
                            print(
                                "je vous ennuie pas trop avec ça, on va recrée les dossiers et repartir sur des bonne base".center(
                                    150))
                            time.sleep(1.25)
                            print("Bon retour a vous :> heureux de te revoir".center(150))
                            fin = 1

                        else:
                            print(
                                "je comprend totallement... ce sont des choses qui arrive comme dis Bob Lennon ahah".center(
                                    150))
                            print(
                                "passons a autre choses, je vais déja enrengistrer sa pour que vous le retrouviez et relançons tout".center(
                                    150))
                            time.sleep(1.25)
                            print("Bon retour a vous :> heureux de te revoir".center(150))
                            fin = 1
                            pourecri = Lecdico("Data", "Raison.txt")
                            raison = "Je ne veux parler de ça car : " + raison
                            pourecri[AJD] = raison
                            Ecrdico("Data", "Raison.txt", pourecri)

                else:
                    print(
                        "Formidable, content que vous ayez bien voulu me le dire, vous pourrez le relire a même l'aplit".center(
                            150))
                    print(
                        "je vais recrée les dossier qui manque et enrengister sa dans le fichier Raison.txt aussi :>".center(
                            150))
                    print("SINON bon retour parmis nous, vraiment heureux de vous voir :>".center(150))
                    fin = 1
                    pourecri = Lecdico("Data", "Raison.txt")
                    raison = "J'ai Suprimer les dossier car : " + raison
                    pourecri[AJD] = raison
                    Ecrdico("Data", "Raison.txt", pourecri)

        # Premier Lancement
        else:
            print("")
            print("Hey Très bien dans ce cas..".center(150))
            print(f"{fg(208)}{bg(17)} 🌟 🌠 ⭐ 🌠 🌟 🌠 ⭐ 🌠 🌟 FATE 🌟 🌠 ⭐ 🌠 🌟 🌠 ⭐ 🌠 🌟 {bg.rs}{fg.rs}\n".center(
                169))
            print(f"Je vais parler de moi a la 3eme personne ahah\n".center(150))
            time.sleep(1)
            print(
                "Fate est un Agenda permettant de créé et Modifier des emplois du temps et des Objectifs et ses Rendez vous,".center(
                    150))
            time.sleep(2)
            print(
                " Fate sert aussi de Journal intime au quel partager ses Emotion et ce que on a fait dans la journée et celui ci pourra".center(
                    150))
            time.sleep(2)
            print("faire des Bilan de semaine, aussi il serra possible de le personnalisé.".center(150))
            time.sleep(2)
            print(
                " Fate à pour projet de devenir un outil à l'image de l'utilisateur, aussi, le premier objectif de celui si est de devenir".center(
                    150))
            time.sleep(2)
            print(
                "aussi le plus interactif et intéressant avec qui partage des choses et '''humains''' possible.\n".center(
                    150))
            time.sleep(3)

            sor = 0
            while sor != 1:
                print("Tout ceci vous va ? (oui/non)".center(150))
                permi = input("".center(75))
                sor = Vérif(permi, 0)
            if permi.lower() == "non":
                print('')
                print("Je vois que vous êtes une personne taquine ahah, C'est noté".center(150))
                time.sleep(0.33)
            print("Très bien, je crées tout les dossiers qui manque et on y va :>".center(150))

        MOIS = Mounth[int(AJD[5:7]) - 1]
        text = MOIS + str(AJD[:4]) + ".txt"
        if not os.path.isdir('../Fate (En Pause (projet partiellement fini))/Agenda'):
            os.mkdir('Agenda')
            dicvide = {}
            Ecrdico("Agenda", text, dicvide)
        if not os.path.isdir('../Fate (En Pause (projet partiellement fini))/Journal'):
            os.mkdir('Journal')
            dicvide = {}
            Ecrdico("Journal", text, dicvide)

        pourecri = Lecdico("Data", "Raison.txt")
        pourecri["Lancement"] = AJD
        Ecrdico("Data", 'Raison.txt', pourecri)



    # si tout les fichier et crée le 1er
    else:
        Aujourdhui = jolisdatetout(AJD)
        ici = Mounth[int(Aujourdhui[4:6]) - 1] + Aujourdhui[7:11] + '.txt'

        if Aujourdhui[1:3] == "01" :
            if not os.path.isfile(f'../Fate (En Pause (projet partiellement fini))/Journal/{ici}') or not os.path.isfile(
                f'../Fate (En cours)/Agenda/{ici}'):
                dicvide = {}
                if not os.path.isfile(f'../Fate (En Pause (projet partiellement fini))/Journal/{ici}'):
                    Ecrdico("Journal", ici, dicvide)
                if not os.path.isfile(f'../Fate (En Pause (projet partiellement fini))/Agenda/{ici}'):
                    Ecrdico("Agenda", ici, dicvide)

                etla = Mounth[int(Aujourdhui[4:6]) - 2]
                if etla == "Décembre":
                    etla = "Décembre" + str(int(Aujourdhui[7:11]) - 1) + '.txt'
                else:
                    etla = etla + Aujourdhui[7:11] + '.txt'

                if not os.path.isfile(f'../Fate (En Pause (projet partiellement fini))/Agenda/{etla}') or not os.path.isfile(
                    f'../Fate (En Pause (projet partiellement fini))/Journal/{etla}'):
                    print(f"Aujourd'hui nous somme le {jolisdatejournale(AJD)}, j'ai donc crée les nouveau fichier pour ce mois ci :>".center(150))
                    time.sleep(1.5)
                    print("CEPENDANT, je viens vers vous car je n'ai pas trouver certain fichier du mois dernier".center(150))
                    time.sleep(1.5)
                    print("Vous savez pourquoi ? si oui, vous pouvez expliqué ?".center(150))
                    raison = input("")
                    pourecri = Lecdico("Data", "Raison.txt")
                    if raison == "":
                        print('')
                        print(f"vous n'avez pas l'air d'en savoir plus que moi...".center(150))
                        time.sleep(0.33)
                        print("BON c'est vraiment dommage, on ferra sans\n".center(150))
                    else:
                        print('')
                        print("Très bien je vois, je vais enrengister sa pour si vous voulez le relire :>\n".center(150))
                        raison = "Le Fichier " + etla + " a été surpimer car : " + raison
                        pourecri[AJD] = raison
                    pourecri["Lancement"] = AJD
                    Ecrdico("Data", "Raison.txt", pourecri)


        #Si on est pas le premier du Mois et que pas de fichier
        else:
            if not os.path.isfile(f'../Fate (En Pause (projet partiellement fini))/Agenda/{ici}') or not os.path.isfile(f'../Fate (En Pause (projet partiellement fini))/Journal/{ici}'):
                print("nous n'avons pas trouver le fichier de ce Mois  ci snif".center(150))
                time.sleep(1)

                sor = 0
                while sor != 1:
                    print("C'est votre premier connexion ce mois ci ? (oui/non)".center(150))
                    rep = input("".center(75))
                    sor = Vérif(rep, 0)

                if rep == "oui":
                    print('')
                    print("Oh je vois, je vais crée les fichier de ce Mois si alors :>".center(150))
                    time.sleep(0.5)
                    print("...".center(150))
                    time.sleep(1)
                    print("Mais j'y pense, sa fait un moment que vous vous êtes pas connecter".center(150))

                    fin=0
                    while fin != 1 :
                        print("Comment c'est passé ce début de mois ?".center(150))
                        rais = input("")

                        if rais == "":
                            sor = 0
                            while sor != 1:
                                print("Vous n'avez rien dis...".center(150))
                                time.sleep(0.33)
                                print("Vous êtes sur de pas vouloir en parler ? (oui/non)".center(150))
                                permi = input("".center(75))
                                sor = Vérif(permi, 0)

                            if permi.lower() == "non":
                                print()
                                print('Bien Alors'.center(150))

                            if permi.lower() == "oui":
                                print()
                                print("Je peux bien comprendre ça, je n'irait pas plus loin".center(150))
                                fin=1
                        else:
                            pourecri=Lecdico("Data","Raison.txt")
                            rais="Je n'était pas la en début "+ici+" mais : "+rais
                            pourecri[AJD]=rais
                            print()
                            print("Mission Accomplit".center(150))
                            time.sleep(0.5)
                            print("Nous avons bien enrengister ça et recrée vos fichier, ON EST REPARTI :>".center(150))
                            fin=1


                    etla = Mounth[int(Aujourdhui[4:6]) - 2]
                    if etla == "Décembre":
                        etla = "Décembre" + str(int(Aujourdhui[7:11]) - 1) + '.txt'
                    else:
                        etla = etla + Aujourdhui[7:11] + '.txt'

                    if not os.path.isfile(f'../Fate (En Pause (projet partiellement fini))/Journal/{etla}') or not os.path.isfile(f'../Fate (En Pause (projet partiellement fini))/Agenda/{etla}'):
                        rere=Lecdico("Data","Raison.txt")
                        rere["Lancement"]=AJD
                        Ecrdico("Data","Raison.txt",rere)

                else:
                    print()
                    print("Vous avez donc suprimez les fichier...".center(150))

                    fin = 0
                    while fin != 1:
                        print("Pourquoi avoir fait ça ?".center(150))
                        rais = input("")

                        if rais == "":
                            sor = 0
                            while sor != 1:
                                print("Vous n'avez rien dis...".center(150))
                                time.sleep(0.33)
                                print("Vous êtes sur de pas vouloir en parler ? (oui/non)".center(150))
                                permi = input("".center(75))
                                sor = Vérif(permi, 0)

                            if permi.lower() == "non":
                                print()
                                print('Bien Alors'.center(150))

                            if permi.lower() == "oui":
                                print()
                                print("Je peux bien comprendre ça, je n'irait pas plus loin".center(150))
                                fin = 1
                        else:
                            pourecri = Lecdico("Data", "Raison.txt")
                            rais = "J'ai suprimmé les fichiers de " + ici + " car : " + rais
                            pourecri[AJD] = rais
                            Ecrdico("Data","Raison.txt",pourecri)
                            print()
                            print("Mission Accomplit".center(150))
                            print("Nous avons bien enrengister ça et recrée vos fichier, ON EST REPARTI :>".center(150))
                            fin = 1
                    pourecri = Lecdico("Data", "Raison.txt")
                    pourecri["Lancement"] = AJD
                    Ecrdico("Data", "Raison.txt", pourecri)
                vide={}
                if not os.path.isfile(f'../Fate (En Pause (projet partiellement fini))/Agenda/{ici}'):
                    Ecrdico("Agenda",ici,vide)
                if not os.path.isfile(f'../Fate (En Pause (projet partiellement fini))/Journal/{ici}'):
                    Ecrdico("Journal",ici,vide)