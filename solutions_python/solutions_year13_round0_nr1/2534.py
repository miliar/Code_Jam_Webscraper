import numpy

lines = 4

def won(listValues, player):
    res = False
    i = 0
        
    while (not res) and i<len(listValues):
        if (not '.' in listValues[i]):
            if (listValues[i].count(player)==lines or (listValues[i].count(player)==(lines-1) and 'T' in listValues[i])):
                res = True
        i+=1
    return res

cases = int(raw_input())
for c in xrange(cases):
    listOfH = []
    for i in xrange(lines):
        listOfH.append(list(raw_input()))
    
    # reshape to vertical
    listOfV = []
    for i in xrange(lines):
        lineAux = []
        for j in xrange(lines):
            lineAux.append(listOfH[j][i])
        listOfV.append(lineAux)
        
    # diagonal
    listOfDiagonal = []
    listAux = []
    for i in xrange(lines):
        listAux.append(listOfH[i][i])
    listOfDiagonal.append(listAux)
    listAux = []
    for i in xrange(lines):
        listAux.append(listOfH[i][lines-i-1])
    listOfDiagonal.append(listAux)
    
    # results:
    # 1 - "X won" (the game is over, and X won)
    # 2 - "O won" (the game is over, and O won)
    # 3 - "Draw" (the game is over, and it ended in a draw)
    # 4 - "Game has not completed" (the game is not over yet)
    
    result = ''
    
    # 'X' won?
    if won(listOfH, 'X') or won(listOfV, 'X') or won(listOfDiagonal, 'X'):
        result = 'X won'
    # 'O' won?
    elif won(listOfH, 'O') or won(listOfV, 'O') or won(listOfDiagonal, 'O'):
        result = 'O won'
    elif not '.' in [item for sublist in listOfH for item in sublist]:
        result = 'Draw'
    else:
        result = 'Game has not completed'
    
        
    if c<cases-1:
        rubbish = raw_input() # last line
    # output answer
    print "Case #%d:" % (c+1), result