#/bin/python
import sys

def checkH(board, player):
    for x in [0, 4, 8, 12]:
        if board[x] == player and board[x] == board[x+1] and board[x+1] == board[x+2] and board[x+2] == board[x+3]:
            return True
    return False

def checkV(board, player):
    for x in [0, 1, 2, 3]:
        if board[x] == player and board[x] == board[x+4] and board[x+4] == board[x+8] and board[x+8] == board[x+12]:
            return True
    return False

def checkD(board, player):
    if board[0] == player and board[0] == board[5] and board[5] == board[10] and board[10] == board[15]:
        return  True
    if board[3] == player and board[3] == board[6] and board[6] == board[9] and board[9] == board[12]:
        return  True
    return False

def checkBoard(board):
    xboard = board.replace("T", "X")
    res = checkH(xboard, "X")
    if res == False:
        res = checkV(xboard, "X")
        if res == False:
            res = checkD(xboard, "X")
    if res == True:
        return "X won"
    
    oboard = board.replace("T", "O")
    res = checkH(oboard, "O")
    if res == False:
        res = checkV(oboard, "O")
        if res == False:
            res = checkD(oboard, "O")
    if res == True:
        return "O won"
        
    if board.find(".") >= 0:
        return "Game has not completed"
    return "Draw"


num = int(sys.stdin.readline())

count = 1

while num > 0:
    board = ""
    for i in xrange(0,4):
        line = sys.stdin.readline()
        board += line.strip()
    result = "Case #" + str(count) + ": " + checkBoard(board)
    print result
    sys.stdin.readline()
    num = num - 1
    count = count + 1

