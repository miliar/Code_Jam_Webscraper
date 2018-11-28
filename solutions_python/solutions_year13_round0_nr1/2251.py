import sys

def sortKey(foo):
    bar = foo.split('#')
    return int(bar[1])

def checkNotFull(foo):
    hasDot = False
    for elem in foo:
        if elem.find('.') != -1:
            hasDot = True
    return hasDot

def checkWinner(foo,XorO):
    checks = []
    for i in range(4):
        checks.append(checkRowForChar(foo[i],XorO))
        checks.append(checkColForChar(foo,XorO,i))
    checks.append(checkDiagForChar(foo,XorO,'top'))
    checks.append(checkDiagForChar(foo,XorO,'bot'))
    return True in checks

def checkRowForChar(row,XorO):
    rowFull = True
    for elem in row:
        if elem != XorO:
            if elem != 'T':
                return False
    return rowFull

def checkColForChar(foo,XorO,col):
    colFull = True
    test = foo[0][col] + foo[1][col] + foo[2][col] + foo[3][col]
    return checkRowForChar(test,XorO)

def checkDiagForChar(foo,XorO,switchVar):
    diagFull = True
    if switchVar == 'top':
        test = foo[0][0] + foo[1][1] + foo[2][2] + foo[3][3]
        return checkRowForChar(test,XorO)
    elif switchVar == 'bot':
        test = foo[3][0] + foo[2][1] + foo[1][2] + foo[0][3]
        return checkRowForChar(test,XorO)
    else:
        print 'WhatTheF'

def checkGameStatus(foo):
    """
    "X won" (the game is over, and X won)
    "O won" (the game is over, and O won)
    "Draw" (the game is over, and it ended in a draw)
    "Game has not completed" (the game is not over yet)
    """
    isNotFull = checkNotFull(foo)
    xWon = checkWinner(foo,'X')
    oWon = checkWinner(foo,'O')
    if not xWon and not oWon and isNotFull:
        return "Game has not completed"
    elif not xWon and not oWon and not isNotFull:
        return "Draw"
    elif xWon and oWon:
        return "Draw"
    elif xWon:
        return "X won"
    elif oWon:
        return "O won"
    else:
        print 'Forgot something in checking status'


fh = open(sys.argv[1]).readlines()
numCases = int(fh[0])

fh = [x.strip() for x in fh]
cases = {}

for i in range(numCases):
    foo = fh[1+(i*5):(1+(i*5)+4)]
    temp = 'Case #'+str(i+1)
    cases[temp] = foo

foobar = sorted(cases,key=sortKey)
results = open('results.txt','w')
for k in foobar:
    results.write(k+": "+checkGameStatus(cases[k]) + '\n')

results.close()
