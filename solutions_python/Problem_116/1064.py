from sys import stdin

import re


def readboard():
    board = []
    for i in range(4):
        board.append(stdin.readline()[:4])
    stdin.readline()    # Empty line
    return board


def winner_of(s):
    if re.match('^[XT]{4}$', s):
        return 'X won'
    elif re.match('^[OT]{4}$', s):
        return 'O won'
    else:
        return None

def state_of(board):
    #print "Board is:"
    #for i in range(4): print board[i]

    for i in range(4):
        row = board[i]
        #print "Row %s is "%i + row
        winner = winner_of(row)
        if winner is not None:
            return winner

        column = ''.join([board[j][i] for j in range(4)])
        #print "Column %s is "%i + column
        winner = winner_of(column)
        if winner is not None:
            return winner

    downdiagonal = ''.join(board[j][j] for j in range(4))
    #print "Downdiagonal is " + downdiagonal
    winner = winner_of(downdiagonal)
    if winner is not None:
        return winner

    updiagonal = ''.join(board[3-j][j] for j in range(4))
    #print "Updiagonal is " + updiagonal
    winner = winner_of(updiagonal)
    if winner is not None:
        return winner

    if '.' in ''.join(board):
        return 'Game has not completed'
    return 'Draw'


cases = int(stdin.readline())

for case in range(1, cases+1):
    board = readboard()
    print "Case #%s: %s" % (case, state_of(board))
