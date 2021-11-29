import random
x = input("Saisissez un nombre : ")

a = random.randint(1, 100)

while x != a:
    if x > a:
        print("Le chiffre est moins grand.")
        x = input("\nSaisissez un nombre : ")
    elif x < a:
        print("Le chiffre est plus grand.")
        x = input("\nSaisissez un nombre : ")
    else:
        break
print("Vous avez saisi le chiffre correct.")

