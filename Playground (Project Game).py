import random
print("Welcome to The Torch of Piccolenius Lair. \n ")


# Basic Functions ##################3


random_coin1 = random.randint(0, 1)
random_coin2 = random.randint(0, 1)

random_three = random.randint(0, 2)

random_four = random.randint(0, 3)


def wrap1(txt):
    print("=="*len(txt))
    print(txt)
    print("=="*len(txt))


############### General Categories #####################

class Characters:
    def __init__(self, describe, health, weapon):
        self.describe = describe
        self.health = health
        self.weapon = weapon


class Items:
    def __init__(self, describe):
        self.describe = describe


#################### Weapons ##########################

class Weapon(Items):
    def __init__(self, std_damage, spec_damage):
        self.std_damage = std_damage
        self.spec_damage = spec_damage


sword = Weapon(1, 3)
sword.describe = "Sturdy steel sword. Minimum damage = -1. Special damage = -3"

claw = Weapon(1, 3)
claw.describe = "Long sharp claws that rips into skin. Minimum damage = -1, special damage = -3"

############# Characters #############################


class Goblin(Characters):
    describe = "Fiendish fellows with sinister fidelities"
    health = 10
    weapon = claw

    def hit(toss):
        if toss == 0:
            Warrior.health -= Goblin.weapon.std_damage
            print("Normal hit. You lost {} HP.".format(Goblin.weapon.std_damage))
        if toss == 1:
            Warrior.health -= Goblin.weapon.spec_damage
            print("Special hit. You lost {} HP.".format(
                Goblin.weapon.spec_damage))
        if Warrior.health > 0:
            print("Your health = {} HP.\n".format(Warrior.health))
        elif Warrior.health <= 0:
            print("You are dead!\n")


class Warrior(Characters):
    describe = "Strong and loyal fighters"
    health = 10
    weapon = sword

    def hit(toss):
        if toss == 0:
            Goblin.health -= Warrior.weapon.std_damage
            print("Normal hit. Goblin lost {} HP".format(
                Warrior.weapon.std_damage))
        if toss == 1:
            Goblin.health -= Warrior.weapon.spec_damage
            print("Special hit. Goblin lost {} HP".format(
                Warrior.weapon.spec_damage))
        if Goblin.health > 0:
            print("Goblin's health = {} HP.".format(Goblin.health))
        elif Goblin.health <= 0:
            print("Goblin is dead. Huzzah!\n")

############## Test Game ############################


"""
print(Warrior.describe)
print(claw.describe)

Warrior.hit()

Warrior.hit()
"""

############### Run Game ##############################

print("You are Warrior Leo. \nYou have been commanded to enter the Lair of Piccolenius to slay the Goblin and save the town of Kafirrazin.\n")

see_weapon = input(
    "Would you like to examine your weapon before you leave base? [y/n]: ")
stupid = 1
while see_weapon != "y" and see_weapon != "n" and stupid <= 2:
    print("Unknown response, you peasant!")
    stupid += 1
    see_weapon = input("\nWould you like to examine your weapon? [y/n]: ")
    if see_weapon == "y" or see_weapon == "n":
        break
if see_weapon != "y" and see_weapon != "n" and stupid == 3:
    print("Your incompetence stripped you of your warrior badge! Begone!")
    sys.exit()

while see_weapon == "y":
    print(Warrior.weapon.describe)
    see_weapon = input(
        "\nWould you like to examine your weapon again? [y/n]: ")

leave_base = input("Are you ready to leave base and enter the Lair? [y/n]: ")
while leave_base != "y" and leave_base != "n":
    print("Unknown response, you peasant!")
    leave_base = input("\nWould you like to leave and enter the Lair? [y/n]: ")
    if leave_base == "y" or leave_base == "n":
        break
procrastinate = 1
while leave_base == "n" and procrastinate <= 3:
    print("You took a rest in the base overnight. \nZzzzzz...\n")
    procrastinate += 1
    leave_base = input(
        "\nWould you like to leave and enter the Lair today? [y/n]: ")
if leave_base == "y":
    print("You left the base!")
if leave_base == "n":
    print("You lazy animal! The Mayor of Kafirrazin ordered you to fight now! You have no choice! \nYou were forced to leave base!")
if leave_base != "n" and leave_base != "y":
    print("You incoherant babble is intolerable. The Mayor of Kafirrazin banished you to the Lair")

print("\n.\n.\n.\nYou entered the lair...\n")

take_step = input("Do you want to move forward or run away? [move/run]: ")
bad_resp = 0
while take_step != "move" and take_step != "run":
    print("Unknown response, you peasant!")
    bad_resp += 1
    take_step = input(
        "\nDo you want to move forward or run away? [move/run]: ")
    if take_step == "move" or take_step == "run":
        break
    if bad_resp == 2:
        take_step = "lousy"
        break
steps = 0
step_describe = ["It is dark and quiet in here",
                 "There is a musky smell. The air is growing thicker", "It feels strange. Something is afoot"]
while take_step == "move" and steps <= 2:
    print("You took a step.\n.\n.\n.\n.")
    print(step_describe[steps])
    steps += 1
    take_step = input(
        "\nWould you like to move forward again or run? [move/run]: ")
if take_step == "move" and steps == 3:
    print("Goblin appears in front of you. \nPrepare to fight!")
    print("\n<> <> <> <> <> <> <> <> <>")
if take_step == "run":
    print("Your hasty footsteps caught the attention of the Goblin! \nPrepare to fight!")
    print("\n<> <> <> <> <> <> <> <> <>")
if take_step != "move" and take_step != "run":
    print("Your indecisive response landed you in the snares of the Goblin. \nPrepare to fight!")
    print("\n<> <> <> <> <> <> <> <> <>")

print("\nYou readied your sword and your shield.")
print("\nNOTE:\nHitting the Goblin reduces its health but exposes you to its sharp claws. \nShielding yourself does not harm the Goblin, but keeps you safer")
print("\nNOTE:\nGoblins MAY get fatigued every 2 turns and MAY not strike. You may wish to strike then. \nHowever, if it does strike, there will be severe damage!!")

body_parts = ["thigh", "shoulder", "back", "chest", "neck", "foot", "arm"]
goblin_hits = 1
turn = 1
while Goblin.health > 0 and Warrior.health > 0:
    print("\n==========TURN {}==========".format(turn))
    if goblin_hits % 3 == 0:
        print("The Goblin already had 2 consecutive strikes. It MAY rest. If it does strike, it will be severe!")
    print("\nYour health = {} HP.".format(Warrior.health),
          "Goblin's health = {} HP.".format(Goblin.health))
    fight = input("\nHit Goblin or shield yourself? [hit/shield]: ")
    turn += 1
    if fight == "hit":
        print("\nYou hit the Goblin in the {}.".format(
            body_parts[-(goblin_hits % 5)]))
        Warrior.hit(random.randint(0, 1))
        expose = 1
    elif fight == "shield":
        print("\nYou shielded yourself...")
        expose = 0
    elif fight != "hit" and fight != "shield":
        print("\nYour indecisive response left you without defence...")
        expose = 1
    if turn % 3 == 0 and Goblin.health > 0:
        strike_or_not = random.randint(0, 1)
        if strike_or_not == 0:
            print("\nGoblin decided to rest. \nYou were unharmed.")
        elif strike_or_not == 1:
            print("\nGoblin decided to strike... \n")
            if expose == 1 and Goblin.health > 0:
                print("\nGoblin striked you right in the {}.".format(
                    body_parts[goblin_hits % 5]))
                Goblin.hit(1)
                goblin_hits += 1
            if expose == 0 and Goblin.health > 0:
                print("\nGoblin striked your shield... \nYou were unharmed")
                print("Your health = {} HP.\n".format(Warrior.health))
                goblin_hits += 1
    elif expose == 1 and Goblin.health > 0 and turn % 3 != 0:
        print("\nGoblin striked you right in the {}.".format(
            body_parts[goblin_hits % 5]))
        Goblin.hit(random.randint(0, 1))
        goblin_hits += 1
    elif expose == 0 and Goblin.health > 0 and turn % 3 != 0:
        print("\nGoblin striked your shield... \nYou were unharmed")
        print("Your health = {} HP.\n".format(Warrior.health))
        goblin_hits += 1
if Goblin.health <= 0:
    print("You emerged victorious! \nYou defeated the Goblin that terrorised Kafirrazin.")
if Warrior.health <= 0:
    print("The Goblin devoured your bones. \n<<<<<<THE END>>>>>>>")
