import numpy as np
import sys

def num(slice, char):
    raw = np.size(np.where(slice == char))
    if raw == 3:
        if np.size(np.where(slice == 'T')) == 1:
            return 4
        else:
            return 3
    return raw

def won(char, board):
    if num(board[0], char) == 4 or num(board[1], char) == 4 or num(board[2], char) == 4 or \
        num(board[3], char) == 4 or num(board[:, 0], char) == 4 or num(board[:, 1], char) == 4 or \
        num(board[:, 2], char) == 4 or num(board[:, 3], char) == 4 or \
        num(np.diagonal(board), char) == 4 or num(np.diagonal(np.fliplr(board)), char) == 4:
        return True
    else:
        return False

def draw(board):
    if np.size(np.where(board == '.')[0]) > 0:
        return False
    else:
        return True

data = [line.strip() for line in file(sys.argv[1])]

cases = int(data[0])
for i in range(0, cases):
    index = (i * 5) + 1
    board = np.array([list(data[index]), list(data[index + 1]), list(data[index + 2]), list(data[index + 3])])
    
    case = i + 1
    output = None
    if won('X', board):
        output = 'X won'
    elif won('O', board):
        output = 'O won'
    elif draw(board):
        output = 'Draw'
    else:
        output = 'Game has not completed'

    print 'Case #%s: %s' % (case, output)
