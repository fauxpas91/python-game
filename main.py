from classes.game import bcolors, Person
from classes.magic import Spell
from classes.inventory import Item

#Black magic spells
fire = Spell("Fire", 10, 100, "Black")
lightening = Spell("Lightening", 30, 300, "Black")
ice = Spell("Ice", 5, 50, "Black")
meteor = Spell("Meteor", 20, 200, "Black")
quake = Spell("Quake", 14, 140, "Black")

#White magic spells
heal = Spell("Minor Heal", 10, -100, "White")
great_heal = Spell("Major Heal", 20, -250, "White")


#Items
small_health_potion = Item("Small health potion", "Health Potion", "Heals 50 HP", 50)
medium_health_potion = Item("Medium health potion", "Health Potion", "Heals 100 HP", 100)
large_health_potion = Item("Large health potion", "Health Potion", "Heals 200 HP", 200)
extreme_health_potion = Item("Extreme health potion", "Health Potion", "Heals all HP", 9999)

small_mana_potion = Item("Small mana potion", "Mana Potion", "Restores 50 MP", 50)
medium_mana_potion = Item("Medium mana potion", "Mana Potion", "Restores 100 MP", 100)
large_mana_potion = Item("Large mana potion", "Mana Potion", "Restores 200 MP", 200)
extreme_mana_potion = Item("Extreme mana potion", "Mana Potion", "Restores all MP", 9999)

small_grenade = Item("Small grenade", "Throwable weapon", "Deals 250 damage", 250)

player_spells = [fire, lightening, ice, meteor, quake, heal, great_heal]
player_items = [{"Item": small_health_potion, "Quantity": 5}, {"Item": medium_health_potion, "Quantity": 5},
                {"Item": small_mana_potion, "Quantity": 5}, {"Item": medium_mana_potion, "Quantity": 5},
                {"Item": small_grenade, "Quantity": 5}]


#Instantiate characters
player = Person(460, 65, 60, 34, player_spells, player_items)
enemy = Person(1200, 65, 45, 25, [ice], [])

game_run = True
print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACKS!" + bcolors.ENDC)

#Game loop
while game_run:
    print("=======================")
    print("Player Health:", player.get_hp(),
          "\nPlayer MP:", player.get_mp())
    print("=======================")
    print("Enemy Health:", enemy.get_hp(),
          "\nEnemy MP:", enemy.get_mp())

    player.choose_action()
    choice = input("Choose action: ")

    if choice == '1':
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print(bcolors.OKGREEN + "You attack for: " + str(dmg) + " points of damage. Enemy HP: " + str(enemy.get_hp()) + bcolors.ENDC)

    elif choice == '2':
        player.choose_spell()
        choice = int(input("Choose a spell: ")) - 1

        spell = player.spell_list[choice]
        magic_dmg = spell.generate_spell_dmg()

        if choice == -1:
            continue

        elif player.get_mp() >= spell.get_spell_cost():
            player.reduce_mp(spell.get_spell_cost())

            if spell.type == "Black":
                enemy.take_damage(magic_dmg)
                print(bcolors.OKBLUE + "You cast " + spell.get_spell_name() + " and do " +
                      str(magic_dmg) + " points of damage." + bcolors.ENDC )
            elif spell.type == "White":
                player.hp -= magic_dmg
                print(bcolors.OKGREEN + "You cast " + spell.get_spell_name() + " and heal for " +
                      str(magic_dmg) + " points of health." + bcolors.ENDC )

        else:
            print(bcolors.FAIL + "You try to cast " + spell.get_spell_name() +
                  ", but you don't have enough Mana" + bcolors.ENDC)
            continue

    elif choice == '3':
        player.choose_item()
        choice = int(input("Choose an Item: ")) - 1

        item = player.inventory[choice]["Item"]
        value = item.property

        if choice == -1:
            continue
        elif player.inventory[choice]["Quantity"] >= 1:
            if item.type == "Health Potion":
                print(bcolors.OKGREEN + "You use a " + item.name + " on yourself and it " + item.description + bcolors.ENDC)
                player.increase_hp(value)
            elif item.type == "Mana Potion":
                print(bcolors.OKBLUE + "You use a " + item.name + " on yourself and it " + item.description + bcolors.ENDC)
                player.increase_mp(value)
            elif item.type == "Throwable weapon":
                print(bcolors.OKGREEN + "You throw a " + item.name + " at the enemy and it " + item.description + bcolors.ENDC)
                enemy.take_damage(value)
            player.inventory[choice]["Quantity"] -= 1
        else:
            print(bcolors.FAIL + "You don't have any " + item.name + "'s" + bcolors.ENDC)
            continue



    if enemy.get_hp() == 0:
        print(bcolors.OKGREEN + "You win!" + bcolors.ENDC)
        game_run = False

    enemy_choice = 1
    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print("Enemy attacks for", enemy_dmg, "points of damage.")

    if player.get_hp() == 0:
        print(bcolors.FAIL + "You Lose! You have been killed!" + bcolors.ENDC)
        game_run = False