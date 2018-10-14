
import string, os, time, sys

XVAL = 0
OVAL = 1
TVAL = 2
DOTVAL = 3

NOWINS = 0
XWINS = 1
OWINS = 2
DRAW = 3

def GetResultString(result):
    if result == NOWINS:
        return "Game has not completed"
    elif result == DRAW:
        return "Draw"
    elif result == XWINS:
        return "X won"
    elif result == OWINS:
        return "O won"

def GetVal(character):
    if character == "X":
        return XVAL
    elif character == "O":
        return OVAL
    elif character == "T":
        return TVAL
    elif character == ".":
        return DOTVAL

    print "EROR -- UNEXPECTED CHARACTER: '%s'" % character
    sys.exit(1)

def CheckLine(v1, v2, v3, v4):
    if ((v1 == XVAL or v1 == TVAL) and
        (v2 == XVAL or v2 == TVAL) and
        (v3 == XVAL or v3 == TVAL) and
        (v4 == XVAL or v4 == TVAL)):
        return XWINS
    if ((v1 == OVAL or v1 == TVAL) and
        (v2 == OVAL or v2 == TVAL) and
        (v3 == OVAL or v3 == TVAL) and
        (v4 == OVAL or v4 == TVAL)):
        return OWINS
    return NOWINS

def FindWinner(board):
    for i in range(0,4):
        winner = CheckLine(board[0][i], board[1][i], board[2][i], board[3][i])
        if winner != NOWINS:
            return winner
        winner = CheckLine(board[i][0], board[i][1], board[i][2], board[i][3])
        if winner != NOWINS:
            return winner

    winner = CheckLine(board[0][0], board[1][1], board[2][2], board[3][3])
    if winner != NOWINS:
        return winner

    winner = CheckLine(board[0][3], board[1][2], board[2][1], board[3][0])
    return winner
    
    
def HandleCase(f, caseIndex):
    # Read board
    board = []
    boardFull = True
    for i in range(0,4):
        caseline = f.readline().rstrip("\r\n")
        board.append([])
        for a in caseline:
            board[i].append(GetVal(a))
            if a == ".":
                boardFull = False

    # Skip extra newline
    f.readline().rstrip("\r\n")

    winner = FindWinner(board)
    if winner == NOWINS and boardFull:
        winner = DRAW

    result = GetResultString(winner)
    header = "Case #%(count)d: %(r)s" % {"count":caseIndex, "r":result}
    print header
    #sys.exit(1)

    """
    result = ""
    #splitline = caseline.split(" ")
    for c in caseline:
        result += gDict[c]

    header = "Case #%(count)d: %(r)s" % {"count":caseIndex, "r":result}
    print header
    #PrintCharList(result)
    """


inputFile = sys.argv[1]
f = open(inputFile, "r")
numCases = int(f.readline())
for i in range(0, numCases):
    HandleCase(f, i+1)

