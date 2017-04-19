import random

class Spell:
    def __init__(self,
                 name,
                 cost,
                 dmg,
                 type):

        self.name = name
        self.cost = cost
        self.dmg = dmg
        self.type = type

    def generate_spell_dmg(self):
        mgl = self.dmg - 15
        mgh = self.dmg + 15
        return random.randrange(mgl, mgh)

    def get_spell_name(self):
        return self.name

    def get_spell_cost(self):
        return self.cost
