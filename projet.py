def decimal_vers_binaire(decimal):
    """Convertit un nombre décimal en binaire"""
    if decimal < 0:
        decimal += 256
    binaire = ""
    for _ in range(8):
        binaire = str(decimal % 2) + binaire
        decimal //= 2
    return binaire

def menu():
    """Affiche le menu et retourne le choix de l'utilisateur"""
    print("Choisissez une conversion :")
    print("1. Décimal vers Binaire")
    print("2. Quitter")
    choix = input("Entrez votre choix : ")
    return choix




    
def conversion_decimal_vers_binaire():
    """Effectue la conversion de décimal vers binaire"""
    decimal = input("Entrez un nombre décimal entre -128 et 127 : ")
    if decimal.isdigit():
        decimal = int(decimal)
        if -128 <= decimal <= 127:
            binaire = decimal_vers_binaire(decimal)
            print("Le nombre binaire est :", binaire)
        else:
            print(" Le nombre doit être compris entre -128 et 127.")
    else:
        print(" Veuillez entrer un nombre décimal valide.")

def main():
    while True:
        choix = menu()
        if choix == '1':
            conversion_decimal_vers_binaire()
        elif choix == '2':
            print("Au revoir !")
            break
        
            

if __name__ == "__main__":
    main()

