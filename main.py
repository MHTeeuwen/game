# main.py

import random
from test_classes import Grid
from test_classes import Moves
from test_classes import Player
from test_classes import Solver



def main():
    grid = Grid()
    move = Moves()
    play = Player()
    solver = Solver()

    solver.d3(grid, 0)
    
    # solver.complexSolver()
    # solver.simpleSolver()
    # play.randomBot()
    # solver.depthSearch()
    # play.randomBot()
    

    # grid.move(1)
    # grid.fillTile()
    # grid.show()

    # moves = Moves()
    # moves.allMoves()
    # moves.moveIsPossible(0)



def evaluateSolver():

    grid = Grid()
    move = Moves()
    play = Player()
    solver = Solver()

    score, n = [], 100

    for i in range(n):
        score.append(solver.simpleSolver())

    # for i in range(n):
    #     score.append(play.randomBot()) 


    print("AVERAGE SCORE: {} \n MAX. SCORE: {} \n MIN SCORE: {}".format(sum(score)/n, max(score), min(score) ) )


if __name__ == '__main__':
    main()
    # evaluateSolver()