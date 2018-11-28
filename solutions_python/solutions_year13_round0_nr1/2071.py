__author__ = 'krzsza'
import linecache

#function reading specific 4x4 board in a file's sequence

def readBoard(inputfile, boardno):
    arrboard = []
    for i in xrange(startPointBoard(boardno),startPointBoard(boardno) + 4):
        arrboard.append(''.join((map (str, linecache.getline(inputfile, i).split()))))
    return arrboard

#starting line for nth board
def startPointBoard(boardno):
    if boardno == 1:
        return 2
    else:
        return 2 + ((boardno - 1) * 5)

def transformBoard(board):
    transformedBoard = []

    for i in range(0, len(board)):
        transformedBoard.append(board[i])

    for i in range(0, len(board)):
        stringToAppend = ''
        for y in range(0, len(board[i])):
            stringToAppend += (board[y][i])
        transformedBoard.append(stringToAppend)

    stringToAppend = ''

    for i in range(0, len(board)):
        stringToAppend += board[i][i]

    transformedBoard.append(stringToAppend)

    stringToAppend = ''

    for i in range(0, len(board)):
        y = len(board[i]) - 1
        stringToAppend += board[i][(y-i)]

    transformedBoard.append(stringToAppend)

    return transformedBoard

def isLineWin(line, player):
    charCount = 0
    for i in range(0,len(line)):
        if line[i] == player:
            charCount += 1
        elif line[i] == 'T':
            charCount += 1
    if charCount == 4:
        return True
    else:
        return False

def isGameFinished(line):
    charCount = 0
    for i in range(0,len(line)):
        if line[i] == '.':
            return False
    return True

def showWinner(board):
    for i in range(0,len(board)):
        if isLineWin(board[i], 'X') == True:
            return 'X won'
        elif isLineWin(board[i], 'O') == True:
            return 'O won'

    for i in range(0,len(board)):
        if isGameFinished(board[i]) == False:
            return 'Game has not completed'

    return 'Draw'

inputfile = 'A-large.in'
resultsarr = []
testcasesno = int(linecache.getline(inputfile, 1)) + 1

for i in range(1, testcasesno):
    board = transformBoard((readBoard(inputfile, i)))
    print"Case #%d: %s" % (i, showWinner(board))