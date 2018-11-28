import io
from itertools import chain

input_stream = io.StringIO('''6
XXXT
....
OO..
....

XOXT
XXOO
OXOX
XXOO

XOX.
OX..
....
....

OOXX
OXXX
OX.T
O..O

XXXO
..O.
.O..
T...

OXXX
XO..
..O.
...O
''')

def read_board(f):
    board = []
    for i in range(4):
        line = f.readline()
        board.append(list(line.strip()))
    f.readline()
    return board

def process_board(board):
    contains_empty_square = False
    for array in chain(board, get_columns(board), get_diagonals(board)):
        result = checkarray(array)
        if result == 'emptysquare':
            contains_empty_square = True
        elif result == 'mixed':
            pass
        else:
            return result
    
    return 'notcompleted' if contains_empty_square else 'draw'

def checkarray(arr):
    winner = None
    array_set = set(arr) - {'T'}
    if '.' in array_set:
        return 'emptysquare'
    if len(array_set) > 1:
        return 'mixed'
    else:
        return array_set.pop()


def get_columns(board):
    edgesize = len(board)
    for i in range(edgesize):
        column = []
        for j in range(edgesize):
            column.append(board[j][i])
        yield column

def get_diagonals(board):
    edgesize = len(board)
    diagonal1 = []
    diagonal2 = []
    for i in range(edgesize):
        diagonal1.append(board[i][i])
        diagonal2.append(board[edgesize - i - 1][i])
    yield diagonal1
    yield diagonal2

def main(input_stream):
    
    for i in range(int(input_stream.readline())):
        board = read_board(input_stream)
        result = process_board(board)
        message = {
            'notcompleted': 'Game has not completed',
            'draw': 'Draw',
            'X': 'X won',
            'O': 'O won'
        }[result]
        print('Case #%d: %s' %(i+1, message))
    
    

if __name__ == '__main__':
    #main(input_stream)
    import sys
    main(open(sys.argv[1]))