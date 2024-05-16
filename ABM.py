import numpy as np
import pandas as pd

class Agent():
    def __init__(self, world, color, x, y):
        self.color = color
        self.x = x
        self.y = y
        self.world = world.grid[self.x, self.y]
        world.grid[self.x, self.y].open = False #occupies space
    def am_i_happy(self):
        neighbors = [[self.x+1, self.y], [self.x+1, self.y+1], [self.x, self.y+1], [self.x-1, self.y+1], [self.x-1, self.y], [self.x-1, self.y-1], [self.x, self.y-1]]
        likeme = 0
        for n in neighbors:
            if n.color == self.color:
                likeme += 1/8
        if likeme >= 0.4: return True
        elif likeme < 0.4: return False
    def move(self):
        happiness = self.am_i_happy()
        if not happiness:
            self.world.grid[x, y].open = True #leaves space open
            #iterate through open spaces here
                if self.am_i_happy() == True:
                    break #break loop if happy
        
class World():
    def __init(self, width, height, agents):
        self.width = width
        self.height = height
        self.agents = agents
    def build_grid(self):
        self.grid = pd.DataFrame(np.zeros([self.height,self.width])) #Source: https://stackoverflow.com/a/69634965
        
#incomplete as of 5/16