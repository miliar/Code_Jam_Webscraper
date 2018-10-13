import sys

def checkRow(m, row, player):
    for k in xrange(4):
        if m[row][k] != player and m[row][k] != 'T':
            return False
    return True

def checkRows(m, player):
    for i in xrange(4):
        if checkRow(m, i, player): 
            return True
    return False

def checkColumn(m, col, player):
    for k in xrange(4):
        if m[k][col] != player and m[k][col] != 'T':
            return False
    return True

def checkColumns(m, player):
    for i in xrange(4):
        if checkColumn(m, i, player):
            return True
    return False


def checkDiagonals(m, player):
    win = True
    for i in xrange(4):
        if m[i][i] != player and m[i][i] != 'T':
            win = False
            break
    if win : return win
    win = True
    for i in xrange(4):
        if m[3-i][i] != player and m[3-i][i] != 'T':
            win = False
            break
    return win

def checkWinner(m, player):
    if checkRows(m, player): 
        return True
    if checkColumns(m, player):
        return True
    if checkDiagonals(m, player): 
        return True
    return False

def isFilled(m):
    for i in xrange(4):
        for j in xrange(4):
            if m[i][j] == '.': return False
    return True

def getState(m):
    if checkWinner(m, 'X'): return 'X won'
    if checkWinner(m, 'O'): return 'O won'
    if isFilled(m): return 'Draw'
    return 'Game has not completed'

T = int(sys.stdin.readline())

for t in xrange(1, T+1):
    m = [sys.stdin.readline().strip() for _ in xrange(4)]
    sys.stdin.readline()
    state = getState(m)
    print("Case #%d: %s" %(t, state))
