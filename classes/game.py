import random

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING ='\033[93m'
    FAIL ='\033[91m'
    ENDC ='\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Person:
    def __init__(self,
                 hp,
                 mp,
                 atk,
                 df,
                 spells,
                 items):

        self.max_hp = hp
        self.hp = hp
        self.max_mp = mp
        self.mp = mp
        self.atk_low = atk - 10
        self.atk_high = atk + 10
        self.df = df
        self.spell_list = spells
        self.inventory = items
        self.actions = ["Attack", "Magic", "Items"]

    #Get methods
    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.max_hp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.max_mp


    #Get action values

    def generate_damage(self):
        return random.randrange(self.atk_low, self.atk_high)

    def choose_action(self):
        i = 1
        print("\n" + bcolors.OKBLUE + bcolors.BOLD + "ACTIONS" + bcolors.ENDC)
        for action in self.actions:
            print(str(i) + ":", action)
            i +=1

    def choose_spell(self):
        i = 1
        print("\nPress 0 to go to previous menu.")
        print(bcolors.OKBLUE + bcolors.BOLD + "SPELLS" + bcolors.ENDC)
        print("{0:4} | {1:11} | {2:4} | {3:4} | {4:4}  |".format("Num", "Name", "Cost", "Dmg", "Type"))
        for spell in self.spell_list:
            print("{0:4} | {1:11} | {2:4} | {3:4} | {4:4} |".format(str(i), spell.name, str(spell.cost), str(spell.dmg), spell.type))
            i += 1

    def choose_item(self):
        i = 1
        print("\nPress 0 to go to previous menu.")
        print(bcolors.OKBLUE + bcolors.BOLD + "ITEMS" + bcolors.ENDC)
        print("{0:4} | {1:20} | {2:16} | {3:16} | {4:8} |".format("Num", "Name", "Type", "Desc", "Quantity"))
        for item in self.inventory:
            print("{0:4} | {1:20} | {2:16} | {3:16} | {4:8} |".format(str(i), item["Item"].name, item["Item"].type, item["Item"].description, str(item["Quantity"])))
            i += 1

    #Set methods

    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def increase_hp(self, value):
        if self.hp + value > self.max_hp:
            self.hp = self.max_hp
        else:
            self.hp += value

    def reduce_mp(self, cost):
        self.mp -= cost

    def increase_mp(self, value):
        if self.mp + value > self.max_mp:
            self.mp = self.max_mp
        else:
            self.mp += value

    def increase_item_count(self, value):
        self.inventory["Item"]["Quantity"] += 1




