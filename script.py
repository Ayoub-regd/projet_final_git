# script.py - Un script simple en Python
print("Bienvenue dans mon projet versionné avec Git !")

# code cour php lire un fichier et afficher son contenu
try:
    with open("data.txt", "r") as file:
        print("Contenu de data.txt :")
        print(file.read())
except FileNotFoundError:
    print("Fichier data.txt non trouvé. on crée un fichier de base.")

    with open("data.txt", "w") as file:
        file.write(" ligne de test.\n")
    print("Fichier data.txt créé.")
