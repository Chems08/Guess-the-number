import random

a = random.randint(1, 100)
a = int(a)

x = input("Saisissez un nombre : ")
x = int(x)


while x != a:
    if x > a:
        print("Le nombre est moins grand.")
        x = input("\nSaisissez un autre nombre : ")
        x = int(x)
    elif x < a:
        print("Le nombre est plus grand.")
        x = input("\nSaisissez un autre nombre : ")
        x = int(x)
    else:
        break
print("Bravo ! Vous avez saisi le nombre correct.")

