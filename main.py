from random import randint
import time
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from itertools import count
import pandas as pd

plt.style.use('fivethirtyeight')

'''
cls = attribute of the class
self = attribute of the object
Classes are instantiated as objects
'''

class Ant():
    species = "Formica rufa"

    def __init__(self, size):
        self.x = randint(0, size)
        self.y = randint(0, size)
        self.food = 0
        self.infected = False
        self.age = 0
        self.alive =True
        self.colour = 'go'

    def move(self, speed, size):
        self.x += randint(0, speed) - speed
        self.y += randint(0, speed) - speed
        self.x %= size # periodic boundary conditions
        self.y %= size # periodic boundary conditions

    def recover(self, recovery_rate):
        recovery_rate += self.age
        if self.infected and randint(0, 100) > recovery_rate:
            self.infected = False
        elif self.infected and randint(0,100) < recovery_rate:
            self.alive = False

    def infect(self,infect_chance):
        numbs = 100 - self.age
        if self.infected == False and randint(0, numbs) > infect_chance:
            self.infected = True

    def update(self, speed, recovery_rate, size):
        self.infect(50)
        self.move(speed, size)
        self.age += 1
        self.recover(recovery_rate)
        if self.alive == False:
            del(self)

class World():
    def __init__(self, size, population):
        self.members = []
        self.size = size
        for i in range(population):
            self.members.append(Ant(self.size))


    # def animate(self,i):
    #     xs = []
    #     ys = []
    #     colours = []
    #     for member in self.members:
    #         member.update(5, 40, self.size)
    #         xs.append(member.x)
    #         ys.append(member.y)
    #         if member.infected == True:
    #             colours.append('ro')  # orange for infected
    #         elif member.infected == False:
    #             colours.append('go')  # green for healthy
    #     plt.cla()
    #     plt.plot(xs,ys,colours)

    def run(self):
        plt.cla()
        for member in self.members:
            member.update(5, 40, self.size)
            if member.infected == True:
                plt.plot([member.x],[member.y],'ro') # orange for infected
            elif member.infected == False:
                plt.plot([member.x],[member.y],'go') # green for healthy
            plt.axis([0,50,0,50])
            if member.alive == False:
                self.members.remove(member)
        plt.show()



if __name__ == "__main__":
    this_world = World(50, 10)
    while True:
        this_world.run()
        time.sleep(0.1)

