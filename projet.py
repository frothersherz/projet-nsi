def decimal_vers_binaire(decimal):
    """Convertit un nombre décimal en binaire"""  
    if decimal < 0:  # Vérifie si le nombre est négatif
        decimal += 256  # Si oui, ajuste le nombre en conséquence
    binaire = ""  # Initialise une chaîne vide pour stocker le binaire
    for _ in range(8):  # Boucle 8 fois pour obtenir les 8 bits du binaire
        binaire = str(decimal % 2) + binaire  
        decimal //= 2  # Effectue une division entière par 2 pour obtenir le prochain bit
    return binaire  # Retourne la représentation binaire du nombre décimal

def menu():
    """Affiche le menu et retourne le choix de l'utilisateur"""  
    print("Choisissez une conversion :")  # Affiche les options de conversion
    print("1. Décimal vers Binaire")  # Option pour convertir un décimal en binaire
    print("2. Quitter")  # Option pour quitter le programme
    choix = input("Entrez votre choix : ")  # Demande à l'utilisateur de choisir une option
    return choix  # Retourne le choix de l'utilisateur

def conversion_decimal_vers_binaire():
    """Effectue la conversion de décimal vers binaire"""  
    decimal = input("Entrez un nombre décimal entre -128 et 127 : ")  # Demande à l'utilisateur de saisir un nombre décimal
    decimal = int(decimal)  # Convertit la saisie en entier
    if -128 <= decimal <= 127:  # Vérifie si le nombre décimal est dans l'intervalle spécifiée
        binaire = decimal_vers_binaire(decimal)  # Convertit le décimal en binaire
        print("Le nombre binaire est :", binaire)  # Affiche le résultat de la conversion
    else:
        print(" Veuillez entrer un nombre décimal valide.")  # Affiche un message d'erreur si le nombre décimal n'est pas valide

def main():
    while True:  # Boucle principale pour maintenir le menu
        choix = menu()  # Affiche le menu et récupère le choix de l'utilisateur
        if choix == '1':  # Si l'utilisateur choisit de convertir un décimal en binaire
            conversion_decimal_vers_binaire()  # Appelle la fonction de conversion décimal-binaire
        elif choix == '2':  # Si l'utilisateur choisit de quitter le programme
            print("Au revoir !")  # Affiche un message de sortie
            break  # Sort de la boucle principale pour terminer le programme

if __name__ == "__main__":
    main()  
