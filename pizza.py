#!/usr/bin/pythona

from pprint import pprint

class Node:
    x = None
    y = None
    ingredient = None

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "Node: (%s, %s): %s" % (self.x, self.y, self.ingredient)

    def set_ingredient(self, ingredient):
        self.ingredient = ingredient

class Main:
    pizzaheight = None
    pizzawidth = None
    minperslice = None
    maxslicesize = None
    grid = None

    def read_file(self, filename):
        with open(filename) as f:
            # Stiamo leggendo la prima riga
            (self.pizzaheight, self.pizzawidth, self.minperslice, self.maxslicesize) = map(int, f.readline().split())
            #print pizzaheight, pizzawidth, minperslice, maxslicesize
            self.grid = [[Node(j, i) for j in range(self.pizzawidth)] for i in range(self.pizzaheight)]

            numrow = 0
            for line in f:
                row = list(line.strip())
                for numcol in range(0, len(row)):
                    self.grid[numrow][numcol].set_ingredient(row[numcol])
                numrow += 1

    def run(self):
        fname = "sample_input.txt"
        self.read_file(fname)
        pprint(self.grid)

if __name__ == "__main__":
    program = Main()
    program.run()
