def readBoard(boardFile):
    board=[[]]*4
    for i in xrange(4):
        board[i]=list(boardFile.readline().rstrip())
    boardFile.readline() #Extraline
    return board

def checkBoard(x):

    fullBoard = True;

    winner = 0
    #Checking rows and columns
    for firstCoord in xrange(4):
        row=[]
        column=[]
        for secondCoord in xrange(4):
            row.append(x[firstCoord][secondCoord])
            column.append(x[secondCoord][firstCoord])

        if any([i=='.' for i in row]):
            fullBoard=False;
        
        for player in ['X','O']:
            if all([(i==player or i=='T') for i in row]) or all([(i==player or i=='T') for i in column]):
                return '{} won'.format(player)
    
    #Checking diagonals
    diagonalSame=[]
    diagonalOpposite=[]
    for coord in xrange(4):
        diagonalSame.append(x[coord][coord])
        diagonalOpposite.append(x[coord][3-coord])

    for player in ['X','O']:
        if all([(i==player or i=='T') for i in diagonalSame]) or all([(i==player or i=='T') for i in diagonalOpposite]):
            return '{} won'.format(player)

    #No winners
    if fullBoard:
        return 'Draw'
    else:
        return 'Game has not completed'
    
# import

import sys
            
# MAIN

inFile=open(sys.argv[1],'r')
outFile = open(sys.argv[2],'w')

numCases = int(inFile.readline())

for i in xrange(numCases):
    board=readBoard(inFile)
    outFile.write('Case #{}: {}\n'.format(i+1,checkBoard(board)))
