####################################
#        Author: Amber Lee         #
# Email: cryptoboxcomics@gmail.com #
#      Info: A choose-your-own     #
#          adventure game          #
####################################

####################################
#              Imports             #
####################################

import time

####################################
#           Player Assets          #
####################################

player_name = ""
player_health = 100
player_money = 50
player_species = "Human"
player_weapons = []
player_items = []

####################################
#            Game Start!           #
####################################

###         Introduction         ###

print()
print()
print("   ####################################################")
print("   # Hello! This is a choose-your-own-adventure game. #")
print("   #  You are a hero trying to save your kingdom of   #")
print("   #       Kanbal from the evil King Rogsam.          #")
print("   ####################################################")
print()
print()

while(player_name == ""):
    player_name = input("What is your name, Hero? : ")

print()
print("Hi, " + player_name + "! You are our hero and savior! Please save the Kanbalese mountain people from the evil King Rogsam.")
print("You start off with no weapons or items, but if you make the right choices, you might survive.")
print()

#    ---Section Author: <your name>---   #
print("You pass by a traveler who looks injured by the woods. What do you do?")
print("1. Ignore him")
print("2. Try to help him")
decision = ""
while(decision == ""):
    decision = input("Pick a number: ")
    print()
    if (decision == "1"):
        print("You try to leave, but trip over a rock and hit your head!")
        player_health = player_health - 10
        print("Your health now: ")
        print(player_health)
    elif (decision == "2"):
        print("He appreciates that you helped him, and he gives you a potion! A potion heals 20 health points.")
        player_items.append("Potion")
        print("Your items now: ")
        print(player_items)
print()
time.sleep(1)
#            ---section end---           #

#    ---Section Author: Oleg---   #
print("The Kanbalese police stop you and tries to fine you for being outside during coronavirus!")
print("1. Run away")
print("2. Sign the ticket")
print()
decision = ""
while(decision == ""):
    decision = input("Pick a number: ")
    print()
    if (decision == "1"):
        print("You ran but police shoot you with rubber bullets")
        player_health -= 10
        print("Your health now: ")
        print(player_health)
    elif (decision == "2"):
        print("You signed your ticket and got sent on you way with 10 ticket")
        print("Now you need to hide and wait till it is safe to walk on the street")
        player_money -= 10
        print("Your money now: ")
        print(player_money)
print()
time.sleep(1)
#            ---section end---           #

#   Section Author: Zarina... #
print("There is a warrior who stands in your way!")
print("1. Fight him")
print("2. Try negotiating with him")
print()
decision = ""
while(decision == ""):
    decision = input("Pick a number: ")
    print()
    if (decision == "1"):
        print("You got injured but you steal his money!!!")
        player_health .= 20
        print("Your health now:")
        print(player_health)
    elif (decision == "2"):
        print("You are able to get him to work with your mission")
        player_items.append("Warrior")
        print("Your items now:")
        print(player_items)
    print()
    time.sleep(1)