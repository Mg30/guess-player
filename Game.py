#import des fichiers

import pandas as pd

df = pd.read_csv('Ligue1_Clean.csv')
df.head()

#  Application
# Sélectionnez un joueur au hasard
rejouer = True
score = 0

while rejouer:
    joueur = df.sample().iloc[0]

    # Affiche les informations sélectionnées
    print("Nationalité:", joueur['Nation'])
    print("Âge:", joueur['Age'])
    print("Poste:", joueur['Pos'])
    print("Qui est ce joueur ?\n")

    nom = input()

    compteur_essais = 1
    essais_max = 3

    while nom.lower() not in joueur['Player'].lower():
        if compteur_essais == essais_max:
            print("Désolé, c'est perdu. La réponse est", joueur['Player'])
            score -= 1  # Décrémente le score en cas d'échec après 3 essais
            break

        nom = input("Essaie encore : ")
        compteur_essais += 1

    if nom.lower() == joueur['Player'].lower():
        print("Bravo, c'est gagné !")
        score += 1  # Incrémente le score en cas de bonne réponse
    elif nom.strip() == '':
        print("Le joueur était", joueur['Player'])
        score -= 1  # Décrémente le score en cas de réponse vide

    print("Score actuel:", score)

    choix_rejouer = input("Voulez-vous rejouer ? (Oui/Non) ")

    if choix_rejouer.lower() != "oui":
        print("Merci à bientôt !")
        rejouer = False
