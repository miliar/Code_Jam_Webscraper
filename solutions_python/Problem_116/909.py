# This program uses the common NumPy library
# see http://www.numpy.org/

# Python 2.7

import sys
import numpy

antidiag = numpy.array([[False, False, False, True ],
                        [False, False, True , False],
                        [False, True , False, False],
                        [True , False, False, False]])

def won(board, player):
    mine = numpy.logical_or(board == player, board == 'T')

    # row?    
    for r in range(4):
        if numpy.all(mine[r]):
            return True
    
    # col?
    for c in range(4):
        if numpy.all(mine[:,c]):
            return True
            
    # diag?
    if numpy.all(mine.diagonal()):
        return True
    
    # antidiag?
    if numpy.all(mine[antidiag]):
        return True
    
    return False



f = sys.stdin

count = int(f.readline())

for index in range(1, count+1):
    board = numpy.zeros(shape=(4, 4), dtype=(str, 1))
    row = 0
    
    while row < 4:
        line = f.readline().strip()
        if len(line) == 4:
            board[row] = [c for c in line]
            row += 1
        elif len(line) == 0:
            pass
        else:
            raise Exception("Error: " + lin)
    
    prefix = "Case #{}: ".format(index)
    
    for player in ['O', 'X']:
        if won(board, player):
            print(prefix + player + " won")
            break
    else:
        if numpy.any(board == '.'):
            print(prefix + "Game has not completed")
        else:
            print(prefix + "Draw")