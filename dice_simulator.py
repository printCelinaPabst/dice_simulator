# Import von zufälligen Zahlen
import random

# Introduction Würfelsimulator
print("Herzlich Willkommen beim Würfelsimulator!🎲")
print("Hier kannst du virtuell Würfel zum Rollen bringen!")

# Start der while-Schleife
while True:
#Abfrage 1 , 2 oder 3 für Würfelauswahl
    user_choice = (input("Tippe 1 ein für einen Würfel, 2 für zwei Würfel oder 3 für drei Würfel: ")) # die Abfrage MUSS innerhalb der while schleife sein, 
                                                                                                    # falls der User den else--Block durch Falscheingabe aktiviert hat, 
                                                                                                    # damit der Input von neuem Starten und eine
                                                                                                    # neue Eingabe gemacht werden kann.
# basierend auf der Eingabe des Benutzers wird die Summe der Würfel berechnet
    if user_choice == "1":
        total = random.randint(1, 7) # wählt eine zufällige Zahl von 1 bis 6
        print(f'''Du hast einen Würfel ausgewählt🎲.
    Hier ist dein Ergebnis: {total}''') #Ausgabe gewürfelte Zahl


    elif user_choice == "2":
        dice1 = random.randint(1, 7)
        dice2 = random.randint(1, 7)
        total = dice1 + dice2 #Summe ausrechnen
        print(f'''Du hast zwei Würfel ausgewählt🎲🎲.
    Hier ist dein Ergebnis: {total}''') #Ausgabe gewürfelte Zahl


    elif user_choice == "3":
        dice1 = random.randint(1, 7)
        dice2 = random.randint(1, 7)
        dice3 = random.randint(1, 7)
        total = dice1 + dice2 + dice3 #Summe ausrechnen
        print(f'''Du hast drei Würfel ausgewählt🎲🎲🎲.
    Hier ist dein Ergebnis: {total}''') #Ausgabe gewürfelte Zahl
        

    elif user_choice != "1" and user_choice != "2" and user_choice != "3":
        print("Ungültige Eingabe!")
        continue


    roll_again = input("Nochmal würfeln?(j/n):").lower()
    if roll_again != "j":
        print('''Danke, dass du den Würfelsimulator benutzt hast.
Bis zum nächsten Mal!🎲''')
        break