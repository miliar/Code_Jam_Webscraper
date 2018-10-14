#!/usr/bin/python
import sys

def winCheck(gameBoard, piece):

    # check horizontal rows
    for row in range(0,4):
        if isWinPiece(gameBoard[row][0],piece):
            if isWinPiece(gameBoard[row][1],piece):
                if isWinPiece(gameBoard[row][2],piece):
                    if isWinPiece(gameBoard[row][3],piece):
                        return True

    # check vertical columns
    for column in range(0,4):
        if isWinPiece(gameBoard[0][column],piece):
            if isWinPiece(gameBoard[1][column],piece):
                if isWinPiece(gameBoard[2][column],piece):
                    if isWinPiece(gameBoard[3][column],piece):
                        return True
                        
    # check diagonal (top left to bottom right)
    if isWinPiece(gameBoard[0][0],piece):
        if isWinPiece(gameBoard[1][1],piece):
            if isWinPiece(gameBoard[2][2],piece):
                if isWinPiece(gameBoard[3][3],piece):
                    return True
                    
    # check diagonal (top right to bottom left)
    if isWinPiece(gameBoard[3][0],piece):
        if isWinPiece(gameBoard[2][1],piece):
            if isWinPiece(gameBoard[1][2],piece):
                if isWinPiece(gameBoard[0][3],piece):
                    return True
    return False
    
def isWinPiece(piece, winPiece):
    if piece == winPiece or piece == 'T':
        return True
    return False
    
def drawCheck(gameBoard):
    for i in range(4):
        for j in range(4):
            if gameBoard[i][j] == '.':
                return False
    return True

def solveCase(gameBoard):
    if winCheck(gameBoard, 'X') == True:
        return "X won"
    if winCheck(gameBoard, 'O') == True:
        return "O won"
    if drawCheck(gameBoard) == True:
        return "Draw"
    return "Game has not completed"

inputFile = open(sys.argv[1], 'r')

outputFile = open(sys.argv[2], 'w')
outputString = ""

caseAmount = int(inputFile.readline())

lines=inputFile.readlines()

#print caseAmount
gameBoard = [[0 for i in range(4)] for j in range(4)]


for case in range(0,caseAmount):
    gameBoard[0] = lines[(case * 4)+case].rstrip('\n')
    gameBoard[1] = lines[(case * 4)+case + 1].rstrip('\n')
    gameBoard[2] = lines[(case * 4)+case + 2].rstrip('\n')
    gameBoard[3] = lines[(case * 4)+case + 3].rstrip('\n')
    #print case,gameBoard
    result = solveCase(gameBoard)
    print "Case #" + str(case+1) + ": " + result
    outputString = outputString + "Case #" + str(case+1) + ": " + result + "\n"

outputFile.write(outputString)


    
    