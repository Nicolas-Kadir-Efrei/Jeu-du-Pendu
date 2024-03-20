# Implementation du jeu de pendu

#mot clee a deviner
mot_a_deviner = "bonjour"
#historique des lettres utilisees
liste_lettre_utilise = []

#Phase intial
liste_mot_actuel = []

#Creation de la liste du mot à l'étape actuel
for i in range(len(mot_a_deviner)):
    liste_mot_actuel.append("-")

mot_actuel = "".join(liste_mot_actuel)



# #Une itération
# lettre_joue = input("Entrez une lettre \n")
# liste_lettre_utilise.append(lettre_joue)

# #On va parcourir le mot à deviner pour chercher la lettre jouée
# #Si la lettre existe à la position i, on modifie liste_mot_actuel[i] par la lettre
# for i in range(len(mot_a_deviner)):
#     if lettre_joue == mot_a_deviner[i]:
#         liste_mot_actuel[i] = lettre_joue


# mot_actuel = "".join(liste_mot_actuel)
# print(liste_lettre_utilise)
# print(mot_actuel)

print(mot_actuel)
#tous le jeu
while mot_actuel != mot_a_deviner:
    lettre_joue = input("Entrez une lettre \n")
    #Vérifier si la lettre a été déjà joué
    if lettre_joue in liste_lettre_utilise:
        print("La lettre était déjà joué, essaye une autre lettre")
    #Une lettre jamais joué
    else:
        liste_lettre_utilise.append(lettre_joue)
        #Verifier si la lettre existe
        if lettre_joue in mot_a_deviner:
            print("La lettre existe sur le mot")
            for i in range(len(mot_a_deviner)):
                if lettre_joue == mot_a_deviner[i]:
                    liste_mot_actuel[i] = lettre_joue
        else:
            print("la lettre n'existe pas, essaye une autre lettre")
        mot_actuel = "".join(liste_mot_actuel)
        print("Voici le mot actuelle")
        print(mot_actuel)
        print("Historique des lettres")
        print(liste_lettre_utilise)
        