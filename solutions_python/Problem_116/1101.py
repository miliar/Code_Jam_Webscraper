# Google Code Jam (2013): Qualification Round

# Code Jam Utils
# Can be found on Github's Gist at:
# https://gist.github.com/Zren/5376385
from codejamutils import *

problem_id = 'A'

#problem_size = 'sample'
#problem_size = 'small'
problem_size = 'large'

opt_args = {
    #'practice': True,
    'log_level': DEBUG,
    'filename': 'A-large',
}

T = 'T'
X = 'X'
O = 'O'
EMPTY = '.'

from itertools import chain
def hasEmptySpace(board):
    for cell in chain(*board):
        if cell == EMPTY:
            return True
    return False

def row(board, y):
    for x in xrange(4):
        yield board[y][x]

def col(board, x):
    for y in xrange(4):
        yield board[y][x]

def downright(board):
    for i in xrange(4):
        yield board[i][i]

def upright(board):
    for i in xrange(4):
        yield board[3-i][i]

def countPieces(p, iterable):
    count = 0
    for cell in iterable:
        if cell == p or cell == T:
            count += 1
    return count

def findWinners(board):
    # Horz
    for y in range(4):
        for p in [X, O]:
            count = countPieces(p, row(board, y))
            if count == 4:
                return p
    # Vert
    for x in range(4):
        for p in [X, O]:
            count = countPieces(p, col(board, x))
            if count == 4:
                return p
    # downright
    for x in range(4):
        for p in [X, O]:
            count = countPieces(p, downright(board))
            if count == 4:
                return p
    # upright
    for x in range(4):
        for p in [X, O]:
            count = countPieces(p, upright(board))
            if count == 4:
                return p
    # No winners
    return None
                    


with Problem(problem_id, problem_size, **opt_args) as p:
    for case in p:
        info('Case', case.case)
        board = [[c for c in case.readline()] for y in range(4)]
        
        case.readline() # spacer

        winner = findWinners(board)
        if winner is None:
            if hasEmptySpace(board):
                case.writecase('Game has not completed')
            else:
                case.writecase('Draw')
        else:
            case.writecase(winner + ' won')
