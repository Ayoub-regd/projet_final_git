# script.py - Un script simple en Python
print("Bienvenue dans mon projet versionné avec Git !")

# code cour php lire un fichier et afficher son contenu
try:
    with open("data.txt", "r") as file:
        print("Contenu de data.txt :")
        print(file.read())
except FileNotFoundError:
    print("Fichier data.txt non trouvé. on crée un fichier de base.")

   # test Ajout d'une fonctionnalité pour écrire dans data.txt
    with open("data.txt", "a") as file:
        file.write("Nouvelle ligne ajoutée avec la branche dev.\n")

    print("Nouvelle ligne ajoutée dans data.txt.")

