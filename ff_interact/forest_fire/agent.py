from mesa import Agent
import random
import numpy as np
from numpy.random import uniform
from numpy import multiply

def surf_function(dim=(100,100), low=500, high=1000):
    r = uniform(low, high, size=multiply(*dim)).reshape(dim)
surf=surf_function()

class TreeCell(Agent):

    def __init__(self, pos, model):

        Agent.__init__(self, pos, model)
        self.pos = pos
        self.condition = "Fine"
        self.hght = surf[pos]

    def step(self):

        if self.condition == "On Fire":
            for neighbor in self.model.grid.neighbor_iter(self.pos):
                if neighbor.condition == "Fine" and neighbor.hght>=self.hght:
                    neighbor.condition = "On Fire"
            self.condition = "Burned Out"
        
    def get_pos(self):
        return self.pos