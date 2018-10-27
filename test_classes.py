import numpy as np
import random
from moveAlgoritme import moveLeft
import math
import itertools   
from itertools import *


TURNS = 100
DEPTH = 30

class Grid:

    def __init__(self, grid=None):
        self.grid = self.loadGrid() if grid is None else grid
        # self.move = self.makeMove(grid, x)

    def loadGrid(self):
        grid = [[0]*4 for i in range(4)]
        x, y, u, v = random.randint(0, 3), random.randint(0, 3), random.randint(0, 3), random.randint(0, 3)
        if x!=u or y!=v:
            grid[x][y], grid[u][v] = 2, 2
        else:
            self.loadGrid()

        return grid

    @staticmethod
    def playing(grid):
        n = False
        for row in grid:
            for j in range(len(row)-1):
                if row[j] == 0 or row[-1] == 0 or row[j] == row[j+1]:
                    n = True

        # now do the same with the transposed matrix
        grid2 = [[grid[j][i] for j in range(len(grid))] for i in range(len(grid[0]))]
        for i in grid2:
            for j in range(len(i)-1):
                if i[j] == i[j+1]:
                    n = True

        return True if n else False

    def score(self):
        score = 0
        for row in self.grid:
            for ele in row:
                if ele>2:
                    score += ele * (math.log2(ele) - 1) 
        return int(score)

    # False if gridA == gridB
    def compare(self, grid2):
        for i in range(4):
            for j in range(4):
                # print(type(self.grid))
                if self.grid[i][j] != grid2[i][j]:
                    return True
        return False

    def fillTile(self):
        emp = []
        for i in range(4):
            for j in range(4):
                if self.grid[i][j] == 0:
                    emp.append((i,j))
        if len(emp)>0:
            self.grid[random.choice(emp)[0]][random.choice(emp)[1]] = 2

    def move(self, x, inplace=False):
        grid = np.rot90([moveLeft(i) for i in np.rot90(self.grid, x)], (4-x))
        grid = np.rot90([moveLeft(i) for i in np.rot90(grid, x)], (4-x))    # ???

        if inplace:
            self.grid = grid
            return self
        else:
            return Grid(grid)

    def show(self):
        print()
        for row in self.grid:
            print(row)
        print("SCORE: {}".format(self.score()))

grid = Grid()

class Moves:

    def __init__(self):
        grid = Grid()

    def allMoves(self):
        return [ [ int(i[j]) for j in range(len(i)) ] for i in list(set(list(itertools.combinations_with_replacement('0123', DEPTH)) + list(itertools.combinations_with_replacement('3210', DEPTH))))]

    def moveIsPossible(self, x):
        return grid.compare(grid.move(x))

    def movesLeft(self):

        for x in [0,1,2,3]:
            if self.moveIsPossible(x):
                return True

        return False

moves = Moves()

class Solver:

    # def __init__(self):
    #     grid = Grid()
    #     moves = Moves()

    # def depthSearch(self, grid):
    #     best_moves, best_score = [], 0

    #     for moves in moves.allMoves():
    #         score = 0
    #         for move in moves:
    #             score += grid.score(grid.move(move))
    #             grid = move(move)
    #         if score > best_score:
    #             best_score = score
    #             best_moves = moves

    #     return best_moves

    def simpleSolver(self):
        for t in range(TURNS):
            # if moves.movesLeft():
            score = 0
            bestMove = 0
            for m in [0,1,2,3]:
                if grid.move(m).score() > score:
                    score = grid.move(m).score()
                    bestMove = m
            grid.move(bestMove, inplace=True) # make best move
            grid.fillTile()
        
        return grid.score()


    # todo:
    #   depth VS turns:
    #   complexSolver voert nu 'depth' aantal moves uit.
    #   dit is niet de bedoeling. Hij moet alleen een deopth aantakl moves uitvoeren en dan opnieuw kijken. 
    #    hele functie in for loop:
    #       for i in range(turns/depth):
    #       of for i in range turns, en met enige diepte elke eerste zet uit bm. (dus je maakt elke beurt een nieuwe zet, die de eerste zet is van op dat moment berkene de bm.)
    # def complexSolver(self):
    #     mvs = moves.allMoves()

    #     paths = []
    #     for M in mvs:

    #         newObj = Grid()
    #         score=M
    #         s=0
    #         for m in M:
    #             # score.append(newObj.move(m,inplace=True).score())
    #             s+=newObj.move(m,inplace=True).score()
    #             newObj.fillTile()
    #         score.append(s)
    #         paths.append(score)
    #     z, bm = 0, []
    #     for i in paths:
    #         if i[-1] > z:
    #             z=i[-1]
    #             bm = i[:-1]
    #     # er wordt nog geen rekening gehoiuden met meerdere moves met zelfde uitkomst

    #     print(z,bm)

        
        # # excecute the calculated moves

        # for i in bm:
        #     grid.move(i, inplace=True)
        #     grid.fillTile()

        # grid.show()
        # return grid.score()


        # excecute the FIRST calculated moves

        # for i in bm[0]:
        #     grid.move(i, inplace=True)
        #     grid.fillTile()

        # grid.show()

        # return grid.score()


    # @staticmethod
    # NG = Grid()

    def d3(self, newgrid, c):
        # print(NG)
        c += 1
        newgrid = Grid()
        score, bm = 0, 0
        for i in [1,2,3,0]:
            newgrid.move(i, inplace=True)
            for j in [1,2,3,0]:
                newgrid.move(j, inplace=True)
                for k in [1,2,3,0]:
                    if newgrid.move(k).score() > score:
                        score = newgrid.move(k).score()
                        bm = i
                newgrid.move(i, inplace=True)
            newgrid = Grid()

        # excecute bm
        newgrid = grid.move(bm, inplace=True)
        newgrid.fillTile()
     
        if TURNS - c > 0:
            self.d3(newgrid, c)

        grid.show()
        # grid in begin d3() moet worden geupdate met nieuwe grid na move bm, anders kijkt hij steeds vanaf begin grid
        return grid.move(bm)




class Player:

    # def __init__(self):
    #     grid = Grid()
    #     moves = Moves()

    def randomBot(self):
        for t in range(TURNS):
            # if moves.movesLeft():
            m = random.randint(0,3)
            # if moves.moveIsPossible(m):
            grid.move(m, inplace=True)
            grid.fillTile()
            # grid.show()
        return grid.score()
                # grid.show()
                # print(grid.score())
                # print(grid.score())



    def playGame(self):
        for t in turns:
            m = input('make a move! (w, a, s, d) ') 
            if m not in ['w','a','s','d']:
                m = input('please enter a valid move')
            elif m == 'q':
                break
            grid.move(int(m), inplace=True)
            grid.show()
            grid.score()
            grid.fillTile()

        print("\n\n GAME OVER \n\n Your score was {} \n you made {} moves \n".format( grid.score(), turns ))



# decks/stacks and queues


def main():
    return 'please run from main.py'

if __name__ == '__main__':
    main()


