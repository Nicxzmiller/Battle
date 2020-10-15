from classes.game import Person, bcolors

magic = [
    {"name": "Fire", "cost": 10, "dmg": 40},
    {"name": "Thunder", "cost": 7, "dmg": 30},
    {"name": "Stone", "cost": 4, "dmg": 15},
    {"name": "Blizzard", "cost": 9, "dmg": 35}
]

player = Person(460, 65, 60, 34, magic)
enemy = Person(1200, 65, 45, 25, magic)

running = True
i = 0

print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACKS!" + bcolors.ENDC)

while running:
    print("===================")
    player.choose_action()
    choice = input("Choose Action:")
    index = int(choice) - 1

    print("You chose", index)

    running = False
