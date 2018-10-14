import sys

def getLine(): 
    return sys.stdin.readline()

def getIntLine():
    return int(getLine().strip())

def walkCells(board, x0, y0, dx, dy, cnt):
    result = []
    for _ in range(cnt):
        result.append(board[y0][x0])
        x0 += dx
        y0 += dy
    return result

def getDiag1(board):
    return walkCells(board, 0, 0, 1, 1, 4)

def getDiag2(board):
    return walkCells(board, 3, 0, -1, 1, 4)

def getRow(board, r):
    return walkCells(board, 0, r, 1, 0, 4)

def getCol(board, c):
    return walkCells(board, c, 0, 0, 1, 4)

def getAllRelaventLines(board):
    lines = []
    for i in range(4):
        lines.append(getRow(board, i))
        lines.append(getCol(board, i))
    lines.append(getDiag1(board))
    lines.append(getDiag2(board))
    return lines

def lineWinFor(line, player):
    def count(c):
        return len([el for el in line if el == c])

    if 'T' in line:
        if count(player) == 3:
            return True
    else:
        if count(player) == 4:
            return True

    return False

def determinBoardState(board):
    relLines = getAllRelaventLines(board)
    hasDots = False
    for l in relLines:
        if lineWinFor(l, 'X'):
            return 'X won'
        if lineWinFor(l, 'O'):
            return 'O won'
        if '.' in l:
            hasDots = True
    if hasDots:
        return 'Game has not completed'
    else:
        return 'Draw'


def solveCase(testNr):
    board = []
    for _ in range(4):
        board.append(getLine())
    getLine() # last line

    print 'Case #%d: %s' % (testNr + 1, determinBoardState(board))

for testNr in range(getIntLine()):
    solveCase(testNr)
