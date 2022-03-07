import os, random

run = True
menu = True
play = False
rules = False
key = False
fight = False
standing = True
buy = False
speak = False
boss = False

HP = 50
MAXHP = HP
ATK = 3
pot = 1
elix = 0
gold = 0
x = 0
y = 0

map = [["hills", "plains", "river"],
       ["plains", "river", "hills"],
       ["river", "town", "shop"],
       ["plains", "hills", "cave"]]

y_len = len(map)-1
x_len = len(map[0])-1

biome = {
    "plains": {
        "t": "PLAINS",
        "e": True
        },
    "river": {
        "t": "RIVER",
        "e": True
    },
    "town": {
        "t": "TOWN",
        "e": False
    },
    "shop": {
        "t": "SHOP",
        "e": False
    },
    "hills": {
        "t": "HILLS",
        "e": True
    },
    "cave": {
        "t": "CAVE",
        "e": False
    }
}

e_list = ['Orc', 'Baby Dragon', 'Pig']

mobs = {
    "Orc": {
        "hp": 15,
        "at": 3,
        "go": 18
    },
    "Baby Dragon": {
        "hp": 35,
        "at": 5,
        "go": 12
    },
    "Pig": {
        "hp": 25,
        "at": 2,
        "go": 14
    },
    "Dragon": {
        "hp": 100,
        "at": 10,
        'go': 10
    }
}

def clear():
    os.system("cls")

def draw():
    print("--------------------------------")

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
        str(key)
    ]

    f = open("text_rpg_test/load.txt", "w")

    for item in list:
        f.write(item + "\n")
    f.close()

def heal (amount):
    global HP, name
    if HP + amount < MAXHP:
        HP += amount
    else:
        HP = MAXHP
    print(name + " has healed " + str(HP) + "HP!")

def battle(): 
    global fight, play, run, HP, pot, elix, gold, boss

    if not boss:
        enemy = random.choice(e_list)
    else:
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
            print("3 - USE ELIXR (50HP)")

        choice = input("# ")

        if choice == "1":
            hp -= ATK
            print(name + " dealt " + str(ATK) + " damge to the " + enemy + ".")
            if hp > 0:
               HP -= atk
               print(enemy + " dealt " + str(atk) + " damge to " + name + ".")
            input("> ")
        if choice == "2":
            if pot > 0:
                pot -= 1
                heal(30)
                HP -= atk
                print(enemy + " dealt " + str(atk) + " damge to " + name + ".")
            else:
                print("No potions!")
            input("> ")
        if choice == "3":
            if elix > 0:
                elix -= 1
                heal(50)
                HP -= atk
                print(enemy + " dealt " + str(atk) + " damge to " + name + ".")
            else:
                print("No elixers!")
            input("> ")
        if HP <= 0:
            print(enemy + " defeted " + name + "...")
            draw()
            fight = False
            play = False
            run = False
            print("GAME OVER")
            input("> ")

        if hp <= 0:
            print(name + " defeated the " + enemy + "!")
            draw
            fight = False
            gold += g
            print("You've found " + str(g) + " gold!")
            if random.randint(0,100) < 30:
                pot += 1
                print(" You've found a potion!")
                if enemy == "Dragon":
                    draw()
                    print("Congratulations, you've finished the game!!!")
                    input("> ")
                    boss = False
                    play = False
                    run = False
            input("> ")
            clear()

def shop():
    global buy, gold, pot ,elix, ATK
    
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
        print("1 - UPGRADE WEAPON (+2ATK) - 10 GOLD")
        print("2 - BUY POTION (30HP) - 5 GOLD")
        print("3 - BUY ELIXIR (FULL RESTORE) - 8 GOLD")
        print("4 - LEAVE")
        draw()

        choice = input("# ")

        if choice == "1":
            if gold >= 10:
                ATK += 2
                gold -= 10
                print("You've bought a upgraded weapon!")
            else:
                print("Not enough gold!")
            input("> ")
        elif choice == "2":
            if gold >= 5:
                pot += 1
                gold -= 5
                print("You've bought a potion (30HP)!")
            else:
                print("Not enough gold!")
            input("> ")
        elif choice == "3":
            if gold >= 8:
                elix += 1
                gold -= 8
                print("You've bought a elixir (FULL RESTORE)!")
            else:
                print("Not enough gold!")
            input("> ")
        elif choice == "4":
            buy = False

def mayor():
    global speak, key

    while speak:
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
        print("1 - LEAVE")
        draw()

        choice = input("# ")

        if choice == "1":
            speak = False

def cave():
    global boss, key

    while boss:
        clear()
        draw()
        print("Here lies the cave of the dragon. What will you do?")
        draw()
        if key :
            print("1 - USE KEY")
        print("2 - TURN BACK")
        draw()

        choice = input("# ")
        
        if choice == "1":
            if key:
                battle()
        elif choice == "2":
            boss = False

while run:
    while menu:
        clear()
        draw()
        print("1, NEW GAME")
        print("2, LOAD GAME")
        print("3, RULES")
        print("4, QUIT GAME")
        draw()

        if rules:
            print("Rules:\n A # means put the number of the choice you want to make.\
A > means you can put whatever, you just need to hit enter.")
            rules = False
            choice = ""
            input(">")
        else:
            choice = input("# ")

        if choice == "1": #new game
            clear()
            name = input("# What's your name, hero? ")
            menu = False
            play = True
        elif choice == "2": #load game
            try:
                f = open("text_rpg_test/load.txt","r")
                load_list = f.readlines()
                if len(load_list) == 9:
                    name = load_list[0][:-1]
                    HP = int(load_list[1][:-1])
                    ATK = int(load_list[2][:-1])
                    pot = int(load_list[3][:-1])
                    elix = int(load_list[4][:-1])
                    gold = int(load_list[5][:-1])
                    x = int(load_list[6][:-1])
                    y = int(load_list[7][:-1])
                    key = bool(load_list[8][:-1])
                    clear()
                    #print(name, HP, ATK)
                    #input("> ")
                    menu = False
                    play = True
                else:
                    print("Corrupt save file")
                    input("> ")
            except OSError:
                print("No save file found")
                input("> ")
        elif choice == "3":#rules
            rules = True
        elif choice == "4":#quit
            clear()
            quit() 

    while play:
        save()
        clear()

        if not standing:
            if biome[map[y][x]]["e"]:
                if random.randint(0,100) <= 45:
                    fight = True
                    battle()

        if play:

            if x >= 3:
                x = 2
            if y >= 4:
                y = 3
            draw()
            print("LOCATION: " + biome[map [y][x]]["t"])
            print("COORDS: ", x, y)
            draw()
            print("NAME: " + name)
            print("HP: " + str(HP) + "/" + str(MAXHP))
            print("ATK: " + str(ATK))
            print("POTIONS: " + str(pot))
            print("ELIXIRS: " + str(elix))
            print("GOLD: "+ str(gold))
            draw()
            print("0 - SAVE AND QUIT TO MENU")
            if y > 0:
                print("1 - NORTH")
            if x < 2:
                print("2 - EAST")
            if y < y_len:
                print("3 - SOUTH")
            if x > 0:
                print("4 - WEST")
            if pot > 0:
                print("5 - USE POTION (30HP)")
            if elix > 0:
                print("6 - USE ELIXIR (50HP)")
            if map[y][x] == "shop" or map[y][x] == "town" or map[y][x] == "cave":
                print("7 - ENTER")
            draw()

            dest = input("#")

            if dest == "0":
                play = False
                menu = True
                save()
            elif dest == "1":
                if y > 0:
                    y -= 1
                    standing = False
            elif dest == "2":
                if x < 3:
                    x += 1
                    standing = False
            elif dest == "3":
                if y < 4:
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
                else:
                    print("No potions!")
                input("> ")
                standing = True
            elif dest == "6":
                if elix > 0:
                    elix -= 1
                    heal(50)
                else:
                    print("No elixirs!")
                input("> ")
                standing = True
            elif dest == "7":
                if map[y][x] == "shop":
                    buy = True
                    shop()
                if map[y][x] == "town":
                    speak = True
                    mayor()
                if map[y][x] == "cave":
                    boss = True
                    cave()
                    gold += 1000
            else:
                standing = True