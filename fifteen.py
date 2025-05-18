#author: Hafsah Mahmood
#class: CSE 30
#date: 12/08/23
#non-gui (text) version
import numpy as np
from random import choice, randint
from graph import Graph
import pdb


class Fifteen:
    #construct fifteen object
    def __init__(self, size=4):
        self.tiles = np.array([i for i in range(1, size ** 2)] + [0])
        self.solution = str(self)
        #create graph for game
        self.graph = Graph()
        for i in self.tiles:
            #create vertex for each element in the graph
            self.graph.addVertex(i)
            #add combinations that the user could use
        self.graph.addEdge(0, 12)
        self.graph.addEdge(0, 15)

    #update tile vectors
    def update(self, move):
        if self.is_valid_move(move):
            #find where zero and move are in self.tiles
            index_zero = -1
            index_move = -1
            for i in range(0, 16):
                if self.tiles[i] == 0:
                    index_zero = i
                if self.tiles[i] == move:
                    index_move = i
            #exchange zero with move in self.tiles
            self.transpose(index_zero, index_move)
            #add vertices to graph
            self.graph.addVertex(0)
            #check which move is made to put on grid
            up = index_move - 4
            left = index_move - 1
            right = index_move + 1
            down = index_move + 4
            #check move
            if index_move % 4 == 0:
                left = -1
            if (index_move + 1) % 4 == 0:
                right = -1
            #define indices
            indices = [up, left, right, down]
            for index in indices:
                if index >= 0 and index <= 15:  # if index is within the grid then it is a valid neighbor of zero
                    self.graph.addEdge(0, self.tiles[index])

    #exchange i-tile with j-tile, tiles are numbered 1-15
    def transpose(self, i, j):
        temp = self.tiles[i]
        self.tiles[i] = self.tiles[j]
        self.tiles[j] = temp

    #shuffle tiles
    def shuffle(self, steps=100):
        for i in range(steps):
            move = randint(1, 16)
            if self.is_valid_move(move):
                self.update(move)

    #check if move is valid: one tile is 0 and another tile is its neighbor
    def is_valid_move(self, move):
        zero = self.graph.getVertex(0)
        vertex = self.graph.getVertex(move)
        return vertex in zero.getConnections()  #valid move if move is a neighbor of 0

    #return if program is solved
    def is_solved(self):
        return self.solution == str(self)  #game is solved

    #create layout
    def draw(self):
        tiles = self.tiles.reshape(4, 4)  #4x4 matrix
        print('+---+---+---+---+')
        for row in tiles:
            tostr = ''
            for num in row:
                tostr += '|'
                if num:
                    tostr += '{:^3}'.format(num)  # print each number centered in three spaces
                else:
                    tostr += '   '  #0
            tostr += '|'  #print bar after each number
            print(tostr)
            #create bottom of each row
            print('+---+---+---+---+')
            #return string of array

    def __str__(self):
        tostr = ''
        tiles = self.tiles.reshape(4, 4)
        for row in tiles:
            for num in row:
                if num:
                    #print each number centered
                    tostr += '{:^3}'.format(num)
                else:
                    tostr += '   '
            tostr += '\n'
        return tostr



if __name__ == '__main__':
    game = Fifteen()
    game.shuffle()
    game.draw()
    #allows
    while True:
        move = input('Enter your move or q to quit: ')
        if move == 'q':
            break
        elif not move.isdigit():
            continue
        game.update(int(move))
        game.draw()
        if game.is_solved():
            break
    #print "game over" if game is solved
    print('Game over!')
