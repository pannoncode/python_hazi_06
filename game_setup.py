from random import *


class GameSetup:
    def __init__(self, chance=0, from_num=0, to_num=0):
        self.chance = chance
        self.from_num = from_num
        self.to_num = to_num

    def set_chance(self, inp_chance):
        self.chance = int(inp_chance)

    def set_from_number(self, num_from):
        self.from_num = int(num_from)

    def set_to_number(self, num_to):
        self.to_num = int(num_to)

    def random_number(self):
        return int(randint(self.from_num, self.to_num))
