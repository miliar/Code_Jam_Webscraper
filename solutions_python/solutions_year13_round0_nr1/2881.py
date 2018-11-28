import sys
from collections import Counter

def t_replace(gameBoard, c):
    out = []
    for r in gameBoard:
        out.append(r.replace('T', c))
    return out

def to_o(gameBoard):
    return t_replace(gameBoard, 'O')
def to_x(gameBoard):
    return t_replace(gameBoard, 'X')

def split_rows(gameBoard):
    out = []
    for r in gameBoard:
        out.append(list(r))
    return out

def join_rows(gameBoard):
    out = []
    for r in gameBoard:
        out.append(''.join(r))
    return out

def transform(gameBoard):
    out = []
    numRows = len(gameBoard)
    numCols = len(gameBoard[0])
    for i in range(numCols):
        newCol = []
        for j in range(numRows):
            newCol.append(gameBoard[j][i])
        out.append(newCol)
    return join_rows(out)

def check_row(r, c):
    counter = Counter(r)
    cWon = False
    if counter.get(c, 0) == 4:
        cWon = True
    return cWon

def check_diagonal(gameBoard, c):
    winner = True
    for i in range(len(gameBoard)):
        if gameBoard[i][i] != c:
            winner = False
            break

    if winner:
        return winner, '%c won' % c
   
    winner = True
 
    for i in range(len(gameBoard)):
        if gameBoard[i][len(gameBoard) - i - 1] != c:
            winner = False
            break
    if winner:
        return winner, '%c won' % c

    return False, ''
    

   
def check_board(gameBoard, c): 
    winner = False
    out = ''
    for r in gameBoard:
        if check_row(r, c):
            winner = True
            out = '%c won' % c
            break

    if not winner:
         winner, out = check_diagonal(gameBoard, c)
    return winner, out

def check_X(board):
    return check_board(board, 'X')

def check_O(board):
    return check_board(board, 'O')

def full_board(board):
    for r in board:
        c = Counter(r)
        if c.get('.', 0) > 0:
            return False

    return True
        
def do_test(row1, row2, row3, row4):
    gameBoard = split_rows([row1, row2, row3, row4])
    j_gameBoard = join_rows(gameBoard)

    winner, out = check_X(to_x(j_gameBoard))
    if not winner:
        winner, out = check_O(to_o(j_gameBoard))

    if not winner:
        gameBoard = transform(gameBoard)
        j_gameBoard = join_rows(gameBoard)
        x_gameBoard = to_x(j_gameBoard)

        winner, out = check_X(x_gameBoard)
        if not winner:
            winner, out = check_O(to_o(j_gameBoard))

    if not winner:
        if full_board(gameBoard):
            out = 'Draw'
        else:
            out = 'Game has not completed'

    return out        

inlines = open(sys.argv[1]).readlines()
numcases = int(inlines[0])
idx = 1
for case in range(numcases):
    row1 = inlines[idx]
    row2 = inlines[idx+1]
    row3 = inlines[idx+2]
    row4 = inlines[idx+3]
    out = do_test(row1.rstrip('\n'), row2.rstrip('\n'), row3.rstrip('\n'), row4.rstrip('\n'))
    print "Case #%d: %s" % (case + 1, out)
    idx += 5

