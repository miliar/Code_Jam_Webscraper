'''
Created on 13.04.2013

@author: MrCube
'''
import sys

input = open(sys.argv[1], "r").read()
input = input.splitlines()
numOfTests = int(input[0])
input = input[1:]

tmp = input
input = []
for line in tmp:
    if len(line) > 0:
        row = []
        for c in line:
            row.append(c)
        input.append(row)

tests = []

i = 1
while i < numOfTests + 1:
    line = 0
    board = []
    while line < 4:
        row = []
        for pos in input[(i - 1) * 4 + line]:
            row.append(pos)
        board.append(row)
        line = line + 1
        
    # for each tests
    xRow = [0, 0, 0, 0]
    xCol = [0, 0, 0, 0]
    oRow = [0, 0, 0, 0]
    oCol = [0, 0, 0, 0]
    tRow = [0, 0, 0, 0]
    tCol = [0, 0, 0, 0]
    xDiag = [0, 0]
    oDiag = [0, 0]
    tDiag = [0, 0]
    containsDot = False
    gameOver = False
    
    for row in range(0, 4):
        for col in range(0, 4):
            if board[row][col] == "X":
                xRow[col] = xRow[col] + 1
                xCol[row] = xCol[row] + 1 
                if col == row:
                    xDiag[0] = xDiag[0] + 1
                if (col + row) == 3:
                    xDiag[1] = xDiag[1] + 1
            elif board[row][col] == "O":
                oRow[col] = oRow[col] + 1
                oCol[row] = oCol[row] + 1
                if col == row:
                    oDiag[0] = oDiag[0] + 1 
                if (col + row) == 3:
                    oDiag[1] = oDiag[1] + 1
            elif board[row][col] == "T":
                tRow[col] = tRow[col] + 1
                tCol[row] = tCol[row] + 1
                if col == row:
                    tDiag[0] = tDiag[0] + 1
                if (col + row) == 3:
                    tDiag[1] = tDiag[1] + 1
            elif board[row][col] == ".":
                containsDot = True

    for row in range(0, 4):
        if (xCol[row] + tCol[row]) == 4:
            print "Case #" + str(i) + ": X won"
            gameOver = True
        elif (oCol[row] + tCol[row]) == 4:
            print "Case #" + str(i) + ": O won"
            gameOver = True
            
    if not gameOver:            
        for col in range(0, 4):
            if (xRow[col] + tRow[col]) == 4:
                print "Case #" + str(i) + ": X won"
                gameOver = True
            elif (oRow[col] + tRow[col]) == 4:
                print "Case #" + str(i) + ": O won"
                gameOver = True
          
    if not gameOver:  
    # diagonal
        if (xDiag[0] + tDiag[0]) == 4:
            print "Case #" + str(i) + ": X won"
            gameOver = True
        elif (oDiag[0] + tDiag[0]) == 4:
            print "Case #" + str(i) + ": O won"
            gameOver = True
    
    if not gameOver:
        if (xDiag[1] + tDiag[1]) == 4:
            print "Case #" + str(i) + ": X won"
            gameOver = True
        elif (oDiag[1] + tDiag[1]) == 4:
            print "Case #" + str(i) + ": O won"
            gameOver = True
            
    if not gameOver:
        if not containsDot:
            print "Case #" + str(i) + ": Draw"
        else:            
            print "Case #" + str(i) + ": Game has not completed"
        
    i = i + 1