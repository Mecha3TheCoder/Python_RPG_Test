#importing
import os, random
from this import d

#declareing basic vars
run = True
menu = True
play = False
rules = False
key = False
fight = False
standing = True
adv_txt = "\tHIT ENTER "

#area vars
buy = False
mayor_talk = False
boss = False
in_town = False
towerV = False
towerK = False
towerF = 0
towerHF = 0

#other vars
starting_cutscene = False

#char vars
HP = 50
MAXHP = HP
ATK = 3
pot = 1
elix = 0
gold = 0
x = 0
y = 0

#map
map = [["mountain", "mountain", "mountain", "mountain", "mountain", "mountain", "mountain", "mountain"],
       ["mountain", "town", "farm", "plains", "hills", "hills", "hills", "mountain"],
       ["mountain", "farm", "plains", "plains", "cave", "hills", "hills", "ocean"],
       ["mountain", "plains", "plains", "hills", "hills", "hills", "hills", "ocean"],
       ["mountain", "hills", "hills", "hills", "shrine", "river", "river", "ocean"],
       ["mountain", "hills", "tower", "river", "river", "river", "swamp", "ocean"],
       ["mountain", "plains", "plains", "river", "swamp", "swamp", "swamp", "ocean"],
       ["mountain", "ocean", "ocean", "ocean", "ocean", "ocean", "ocean", "ocean"]]

#cords
y_len = len(map)-1
x_len = len(map[0])-1

#biome map
biome = {
    "mountain": {
        "t": "MOUNTAINS",
        "e": True,
        "ne": False,
        "we": False,
        "ee": True
    },
    "ocean": {
        "t": "OCEAN",
        "e": True,
        "ne": False,
        "we": True,
        "ee": False
    },
    "farm": {
        "t": "FARMLAND",
        "e": True,
        "ne": False,
        "we": False,
        "ee": False
    },
    "tower": {
        "t": "TOWER",
        "e": False,
        "ne": False,
        "we": False,
        "ee": False
    },
    "shrine": {
        "t": "SHRINE",
        "e": False,
        "ne": False,
        "we": False,
        "ee": False
    },
    "swamp": {
        "t": "SWAMP",
        "e": True,
        "ne": False,
        "we": True,
        "ee": False
    },
    "plains": {
        "t": "PLAINS",
        "e": True,
        "ne": True,
        "we": False,
        "ee": False
    },
    "river": {
        "t": "RIVER",
        "e": True,
        "ne": False,
        "we": True,
        "ee": False
    },
    "town": {
        "t": "TOWN",
        "e": False,
        "ne": False,
        "we": False,
        "ee": False
    },
    "hills": {
        "t": "HILLS",
        "e": True,
        "ne": True,
        "we": False,
        "ee": False
    },
    "cave": {
        "t": "CAVE",
        "e": False,
        "ne": False,
        "we": False,
        "ee": False
    }
}

#enemy list
ne_list = ['Orc', 'Goblin', 'Boogers the slime']

we_list = ['Water Golem']

ee_list = ['Golem']

#enemy stats
mobs = {
    "Orc": {
        "hp": 25,
        "at": 3,
        "go": 15
    },
    "Goblin": {
        "hp": 10,
        "at": 1,
        "go": 5
    },
    "Boogers the slime": {
        "hp": 10,
        "at": 2,
        "go": 10
    },

    #Water Enemeys

#    "Water snake": {
#        "hp": 10,
#        "at": 1,
#        "go": 5
#    },
    "Water Golem": {
        "hp": 20,
        "at": 1,
        "go": 15
    },

    #Earth Enemeys

    "Golem": {
        "hp": 20,
        "at": 2,
        "go": 5
    },

    #other

    "Guardian": {
        "hp": towerF*2,
        "at": towerF,
        "go": towerF*4
    }

}

#clear termanal function
def clear():
    os.system("cls")

#draw line function
def draw():
    print("--------------------------------")

#saving function, writes data to file
def save() :
    list = [
        name,
        str(HP),
        str(ATK),
        str(pot),
        str(elix),
        str(gold),
        str(x),
        str(y),
        str(key),
        str(starting_cutscene)
    ]

    f = open("load.txt", "w")

    for item in list:
        f.write(item + "\n")
    f.close()

#healing function
def heal (amount):
    global HP, name
    if HP + amount < MAXHP:
        HP += amount
    else:
        HP = MAXHP
    print(name + " has healed " + str(HP) + "back to HP!")

#battle function, runs when a battle starts
def battle():
    global fight, play, run, HP, pot, elix, gold, boss

    if towerV:
        enemy = "Guardian"
    else:
        if not boss:
            if biome[map[y][x]]["ne"]:
                enemy = random.choice(ne_list)
            elif biome[map[y][x]]["we"]:
                enemy = random.choice(we_list)
            else:
                enemy = random.choice(ee_list)
        elif boss:
            enemy = "Dragon"
    hp = mobs[enemy]["hp"]
    maxhp = hp
    atk = mobs[enemy]["at"]
    g = mobs[enemy]["go"]

    while fight:
        clear()
        draw()
        print("A wild " + enemy + " has appered!!!")
        draw()
        print(enemy + "'s HP " + str(hp) + "/" + str(maxhp))
        print(name + "'s HP " + str(HP) + "/" + str(MAXHP))
        print("POTIONS: " + str(pot))
        print("ELIXIR: " + str(elix))
        draw()
        print("1 - ATTACK")
        if pot > 0:
            print("2 - USE POTION (30HP)")
        if elix > 0:
            print("3 - USE ELIXR (FUL RESTORE)")

        choice = input("# ")
        if choice == "1":
            hp -= ATK
            print(name + " dealt " + str(ATK) + " damge to the " + enemy + ".")
            if hp > 0:
               HP -= atk
               print(enemy + " dealt " + str(atk) + " damge to " + name + ".")
            input(adv_txt)
        if choice == "2":
            if pot > 0:
                pot -= 1
                heal(30)
                HP -= atk
                print(enemy + " dealt " + str(atk) + " damge to " + name + ".")
            else:
                print("No potions!")
            input(adv_txt)
        if choice == "3":
            if elix > 0:
                elix -= 1
                heal(50)
                HP -= atk
                print(enemy + " dealt " + str(atk) + " damge to " + name + ".")
            else:
                print("No elixers!")
            input(adv_txt)
        if HP <= 0:
            print(enemy + " defeted " + name + "...")
            draw()
            fight = False
            play = False
            run = False
            print("GAME OVER")
            input("RIP IN PIECES")

        if hp <= 0:
            print(name + " defeated the " + enemy + "!")
            draw
            fight = False
            gold += g
            #print("You've found " + str(g) + " gold!")
            print(' '.join(["You've found", str(g), "gold!"]))

            if random.randint(0, 100) < 30:
                pot += 1
                print("You've found a potion!")
                if enemy == "Dragon":
                    draw()
                    print("Congratulations, you've finished the game!!!")
                    input(adv_txt)
                    boss = False
                    play = False
                    run = False
                if enemy == "Guardian":
                    towerF += 1
            input(adv_txt)
            clear()

#shop function, runs when buy = true
def shop():
    global buy, gold, pot, elix, ATK, in_town
    
    while buy:
        clear()
        draw()
        print(" Welcome to the shop!")
        draw()
        print("ATK: " + str(ATK))
        print("GOLD: " + str(gold))
        print("POTIONS: " + str(pot))
        print("ELIXIRS: " + str (elix))
        draw()
        print("0 - LEAVE")
        print("1 - BUY POTION (30HP) - 15 GOLD")
        print("2 - BUY ELIXIR (FULL RESTORE) - 20 GOLD")
        print("3 - UPGRADE WEAPON (+2ATK) - 25 GOLD")
        draw()

        choice = input("# ")

        if choice == "0":
            buy = False
            in_town = True
        elif choice == "1":
            if gold >= 15:
                pot += 1
                gold -= 15
                print("You've bought a potion (30HP)!")
            else:
                print("Not enough gold!")
            input(adv_txt)
        elif choice == "2":
            if gold >= 20:
                elix += 1
                gold -= 20
                print("You've bought a elixir (FULL RESTORE)!")
            else:
                print("Not enough gold!")
            input(adv_txt)
        elif choice == "3":
            if gold >= 25:
                ATK += 2
                gold -= 25
                print("You've bought a upgraded weapon!")
            else:
                print("Not enough gold!")
            input(adv_txt)

#mayor function, runs when mayor = true, gives dragon key
def mayor():
    global mayor_talk, key, in_town
 
    while mayor_talk:
        clear()
        draw()
        print("Hello there, " + name + "!")
        if ATK < 10:
            print("Your not strong enough to face the dragon yet! Keep practicing and come back later")
            key = False
        else:
            print("You're strong enough to take on the dragon now! Take this key, but be careful...")
            key = True
        
        draw()
        print("0 - LEAVE")
        draw()

        choice = input("# ")

        if choice == "0":
            mayor_talk = False
            in_town = True

#cav function, if on cave tile let in to fight dragon if key = true
def cave():
    global boss, key, fight

    while boss:
        clear()
        draw()
        print("Here lies the cave of the dragon. What will you do?")
        draw()
        print("0 - TURN BACK")
        if key :
            print("1 - USE KEY")
        draw()

        choice = input("# ")
        
        if choice == "1":
            if key:
                fight = True
                battle()
        elif choice == "0":
            boss = False

#town function, runs when town = true, has shop and mayor
def town():
    global gold, buy, in_town, mayor_talk

    while in_town:
        clear()
        draw()
        print("You entered the town, were do you want to go?")
        draw()
        print("0 - LEAVE")
        print("1 - SHOP")
        print("2 - TOWN HALL")
        #print("3 - ")

        choice = input("# ")

        if choice == "0":
            in_town = False
        elif choice == "1":
            buy = True
            in_town = False
            shop()
        elif choice == "2":
            mayor_talk = True
            in_town = False
            mayor()

#WIP tower function, muti-level simi-random dungen
def tower(towerV,map,biome,towerK,towerHF,towerF):
    while towerV:
        clear()
        draw()
        print("You have entered a dark abanded tower, there are stairs up towards the top and a locked gate in front of stairs down below.")
        print("0 - LEAVE")
        print("1 - GO UP")
        if towerK == True:
            print("2 - GO DOWN")
        draw()

        choice = input("# ")

        if choice == "0":
            towerV = False
        elif choice == "1":
            towerF = 1
        elif choice == "2":
            if towerK == True:
                pass
            else:
                clear()
                print("You do not have the key to open the gate.")
                print(adv_txt)
        while towerF > 0:
            map = [["fl1"], ["fl2"], ["fl3"],["abandonstudy"]]

            biome = {
                "fl1" : {
                    "t" : "Floor 1"
                },
                "fl2" : {
                    "t": "Floor 2"
                },
                "fl3" : {
                    "t" : "Floor 3"
                },
                "abandonstudy" : {
                    "t" : "Abandoned Study"
                }
            }
            clear()
            print("Welcome to the tower, this is a WIP come back")
            input(adv_txt)
            
            if towerF > towerHF:
                towerHF = towerF
            
#main loop
while run:

    while menu:

        #starting menu
        clear()
        draw()
        print("1, NEW GAME")
        print("2, LOAD GAME")
        print("3, RULES")
        print("4, QUIT GAME")
        draw()

        if rules:
            print("Rules:\n A # means put the number of the choice you want to make. > means you can put whatever, you just need to hit enter.")
            rules = False
            choice = ""
            input(adv_txt)
        else:
            choice = input("# ")

        if choice == "1": #new game
            clear()
            name = input("# What's your name, hero? ")
            HP = 50
            MAXHP = HP
            ATK = 3
            pot = 1
            elix = 0
            gold = 0
            x = 4
            y = 4
            menu = False
            play = True
            starting_cutscene = False

        elif choice == "2": #load game

            try:

                f = open("load.txt","r")
                load_list = f.readlines()

                if len(load_list) == 10:

                    name = load_list[0][:-1]
                    HP = int(load_list[1][:-1])
                    ATK = int(load_list[2][:-1])
                    pot = int(load_list[3][:-1])
                    elix = int(load_list[4][:-1])
                    gold = int(load_list[5][:-1])
                    x = int(load_list[6][:-1])
                    y = int(load_list[7][:-1])
                    key = bool(load_list[8][:-1])
                    starting_cutscene = bool(load_list[9][:-1])
                    clear()

                    menu = False 
                    play = True

                else:

                    print("Corrupt save file")
                    input(adv_txt)

            except OSError:

                print("No save file found")
                input(adv_txt)

        elif choice == "3":#rules

            rules = True

        elif choice == "4":#quit

            clear()
            quit()

    #play loop
    while play:

        save()
        clear()

        #checking for a fight
        if not standing:

            if biome[map[y][x]]["e"]:

                if random.randint(0, 100) <= 45:

                     fight = True
                     battle()

        if play:

            if not starting_cutscene:

                clear()
                print("lore lol")
                starting_cutscene = True
                choice = input(adv_txt)

            else:

                #printing info
                clear()
                draw()
                print("LOCATION: " + biome[map [y][x]]["t"])
                print("COORDS: ", x, y)

                if map[y][x] == "mountain" or map[y][x] == "ocean":
                    draw()
                    print("You have reached the boreder of the world, check back after some updates.")
                    
                draw()
                print("NAME: " + name)
                print("HP: " + str(HP) + "/" + str(MAXHP))
                print("ATK: " + str(ATK))
                print("POTIONS: " + str(pot))
                print("ELIXIRS: " + str(elix))
                print("GOLD: "+ str(gold))
                draw()
                print("0 - SAVE AND QUIT TO MENU")

                #checking what actions can be done
                if y > 0:
                    print("1 - NORTH")
                if x < x_len:
                    print("2 - EAST")
                if y < y_len:
                    print("3 - SOUTH")
                if x > 0:
                    print("4 - WEST")
                if pot > 0:
                    print("5 - USE POTION (30HP)")
                if elix > 0:
                    print("6 - USE ELIXIR (50HP)")
                if map[y][x] == "tower" or map[y][x] == "town" or map[y][x] == "cave":
                    print("7 - ENTER")
                draw()

                dest = input("# ")

                #checking menu input
                if dest == "0":
                    play = False
                    menu = True
                    save()
                elif dest == "1":
                    if y > 0:
                        y -= 1
                        standing = False
                elif dest == "2":
                    if x < x_len:
                        x += 1
                        standing = False
                elif dest == "3":
                    if y < y_len:
                        y += 1
                        standing = False
                elif dest == "4":
                    if x > 0:
                        x -= 1
                        standing = False
                elif dest == "5":
                    if pot > 0:
                        pot -= 1
                        heal(30)
                        standing = True
                    else:
                        print("No potions!")
                    input(adv_txt)
                    
                elif dest == "6":
                    if elix > 0:
                        elix -= 1
                        heal(50)
                        standing = True
                    else:
                        print("No elixirs!")
                    input(adv_txt)
                    
                #checking area, town, tower, etc
                elif dest == "7":
                    #if map[y][x] == "shop":
                    #     buy = True
                    #    shop()
                    if map[y][x] == "town":
                        in_town = True
                        town()
                    if map[y][x] == "cave":
                        boss = True
                        cave()
                    if map[y][x] == "tower":
                        towerV = True
                        tower(towerV, map, biome, towerK, towerHF, towerF)
                else:
                    standing = True
