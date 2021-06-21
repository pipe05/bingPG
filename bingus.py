#BingPG
#VERSION:  DEV0.1.9(Save: 9, Stage: Initial Design and Developement)
#---CREDITS---
#PROGRAMMING BY: pipe05#7599
#ART BY: Cosmic#5422
#DESIGN AND IDEAS: bonkbug#3241
#---CREDITS---
import time
import winsound
#LIBRARIES ^^^
winsound.PlaySound("music1.wav", winsound.SND_ASYNC)
name = input("Insert a name:")
loc = "Abandoned Warehouse"
quest = "Green Pebbles"
role = "Unknown"
attack = 6
defence = 5
speed = 4
health = 12
MP = 5
armorlvl = 1
armornm = "Blue Cap"
print("You are 18 years old and finished school, you want to explore the world!")
favcolor = input("What's your favorite color?:")
classsel = input("What do you like to do? (Class selection!!!)\n\nI like to chop things. [1](Swordsman)\nI like reading books. [2](Magician)\nI like to help people. [3](Cleric)\nI like acrobatics. [4](Thief)\nI like hunting. [5](Bowman)\nI like chemistry. [6](Scholar):")
if classsel == "1":
    pclass = 1
    classnm = "Swordsman"
    print("You are now a", classnm)
    weapon = "Dull Sword"
    weaponlvl = 1
elif classsel == "2":
    pclass = 2
    classnm = "Magician"
    print("You are now a", classnm)
    weapon = "Tattered Spellbook"
    weaponlvl = 1
elif classsel == "3":
    pclass = 3
    classnm = "Cleric"
    print("You are now a", classnm)
    weapon = "Lightless Staff"
    weaponlvl = 1
elif classsel == "4":
    pclass = 4
    classnm = "Theif"
    print("You are now a", classnm)
    weapon = "Cracked Knife"
    weaponlvl = 1
elif classsel == "5":
    pclass = 5
    classnm = "Bowman"
    print("You are now a", classnm)
    weapon = "Hand-Me Down Bow"
    weaponlvl = 1
elif classsel == "6":
    pclass = 6
    classnm = "Scholar"
    print("You are now a", classnm)
    weapon = "Small Beaker"
    weaponlvl = 1
time.sleep(1)
print("\n\nName:", name, "\nLocation:", loc,"\nQuest:", quest, "\nRole:", role, "\nClass:", classnm)
time.sleep(5)
print("\nStats:\n\nAttack:", attack, "\nDefense/Defence:", defence, "\nSpeed:", speed, "\nHealth:", health, "\nMP:", MP, "\n\n")
time.sleep(5)
guide = input('[Enter for next]')

if guide == "":
    print("-------------------------------------------------------------------------------------")

    print("Bingus Merchant (Bonkbug) Info:")

    print("The main point of Bingi is that they bring good luck, meaning that in a battle, if you have (a) Bingus/Bingi with you, your HP and MP is boosted by x (the value of x is determined by the level of the bingus)")

    print("\n\nLevels\nNovice: Costs 1 strawberry +2 HP +2 MP\nCompetent: Costs 2 strawberries +3 HP +3 MP\nProficient: Costs 3 strawberries +4 HP +4 MP\nExpert: Costs 4 strawberries +5 HP +5 MP")

    print("1 Bingus = (___) strawberry\nYou get strawberries from defeating Anti-Bingi\nA user can have up to 2 bingi unless they upgrade.\nThe more you use a bingus, the more damaged it gets. Once in a while, you might have to repair one.\n(for every 5 battles a bingus will lose 1 HP. Every bingus has a total HP of 4\nRefunds are free, repairs cost 3 strawberries.")

    print("-------------------------------------------------------------------------------------")
    
    time.sleep(10)
    
    print("[DEBUG VDEV: 0.1.9] Succeded!")