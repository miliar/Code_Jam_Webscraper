import sys
line = sys.stdin.readline()
numTests = int(line)
for test in xrange(1, numTests+1):
    board = []
    if (test > 1):
        sys.stdin.readline()
    for i in xrange(4):
        boardCol = sys.stdin.readline()
        boardCol = [x for x in boardCol]
        board.append(boardCol)

    xCountCol = [0,0,0,0]
    oCountCol = [0,0,0,0]
    tCountCol = [0,0,0,0]

    xCountRow = [0,0,0,0]
    oCountRow = [0,0,0,0]
    tCountRow = [0,0,0,0]

    xDiagCountD = 0
    oDiagCountD = 0
    tDiagCountD = 0

    xDiagCountU = 0
    oDiagCountU = 0
    tDiagCountU = 0

    dotPresence = False
    xWon = False
    oWon = False
    
    for i in xrange(4):
        for j in xrange(4):
            if (board[i][j] == 'X'):
                xCountCol[i] = xCountCol[i] + 1
                xCountRow[j] = xCountRow[j] + 1
                if (i == j):
                    xDiagCountD = xDiagCountD + 1
                if (3 == i+j):
                    xDiagCountU = xDiagCountU + 1
            elif (board[i][j] == 'O'):
                oCountCol[i] = oCountCol[i] + 1
                oCountRow[j] = oCountRow[j] + 1
                if (i == j):
                    oDiagCountD = oDiagCountD + 1
                if (3 == i+j):
                    oDiagCountU = oDiagCountU + 1
            elif (board[i][j] == 'T'):
                tCountCol[i] = tCountCol[i] + 1
                tCountRow[j] = tCountRow[j] + 1
                if (i == j):
                    tDiagCountD = tDiagCountD + 1
                if (3 == i+j):
                    tDiagCountU = tDiagCountU + 1
            elif (board[i][j] == '.'):
                dotPresence = True 
    
    if ((xDiagCountD + tDiagCountD == 4) or (xDiagCountU + tDiagCountU == 4)):
        xWon = True
    if ((oDiagCountD + tDiagCountD == 4) or (oDiagCountU + tDiagCountU == 4)):
        oWon = True

    for i in xrange(4):
        if (((xCountCol[i] + tCountCol[i]) == 4) or ((xCountRow[i] + tCountRow[i]) == 4)):
            xWon = True
        if (((oCountCol[i] + tCountCol[i]) == 4) or ((oCountRow[i] + tCountRow[i]) == 4)):
            oWon = True

    if (xWon):
        print 'Case #%d: X won' %test
    elif (oWon):
        print 'Case #%d: O won' %test
    elif (dotPresence):
        print 'Case #%d: Game has not completed' %test
    else:
        print 'Case #%d: Draw' %test    

