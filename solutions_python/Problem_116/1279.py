import sys

def isxwin(string):
    if string == "XXXX" or string == "XXXT" or string == "XXTX" or string == "XTXX" or string == "TXXX":
        return True
    return False
    
def isowin(string):
    if string == "OOOO" or string == "OOOT" or string == "OOTO" or string == "OTOO" or string == "TOOO":
        return True
    return False

def returnStatus(board):
    emptyFound = 0
    for i in range(0, 4):
        ups = ""
        acrosses = ""
        for j in range(0, 4):       
            ups += board[i][j]
            acrosses += board[j][i]
            if board[i][j] == ".":
                emptyFound = 1
        if isxwin(ups):
            return "X won"
        if isowin(ups):
            return "O won"
        if isxwin(acrosses):
            return "X won"
        if isowin(acrosses):
            return "O won"
    first = ""
    second = ""
    for i in range(0, 4):
        first += board[i][i]
        second += board[i][3-i]
    if isxwin(first):
        return "X won"
    if isowin(first):
        return "O won"
    if isxwin(second):
        return "X won"
    if isowin(second):
        return "O won"
    if emptyFound == 0:
        return "Draw"
    return "Game has not completed"

fileName = sys.argv[1]
inPipe = open(fileName, "r")
initValue = inPipe.readline()
numberOfStrings = int(initValue)
finalString = ""

board = [0, 0, 0, 0]
outstring = ""

for i in range(0, numberOfStrings):
    board[0] = inPipe.readline()
    board[1] = inPipe.readline()
    board[2] = inPipe.readline()
    board[3] = inPipe.readline()
    dummy = inPipe.readline()
    nextVal = returnStatus(board)
    outstring += "Case #" + str(i+1) + ": " + nextVal + "\n"

outstring = outstring[:-1]
outPipe = open("tttt.txt", "w")
outPipe.write(outstring)
outPipe.close()
