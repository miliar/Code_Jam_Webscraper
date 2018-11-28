import numpy as np

def checkWin(rowColDiag):
    # if X won rowColDiag, return 2
    # if Y won rowColDiag, return 3
    # else, return None
    # does this by multiplying
    theProd = np.prod(rowColDiag)
    if theProd == 16 or theProd == 8:
        # 2*2*2*2 or 2*2*2*1
        return "X won"
    elif theProd == 81 or theProd == 27:
        # 3*3*3*3 or 3*3*3*1
        return "O won"
    return None

def solveCase(lines):
    ourLines = []
    ourLines.append(lines.pop(0))
    ourLines.append(lines.pop(0))
    ourLines.append(lines.pop(0))
    ourLines.append(lines.pop(0))
    if len(lines) > 0:
        lines.pop(0) # remove blank
    # translate . => 0, T => 1, X => 2, O => 3
    board = np.zeros((4,4), dtype=int)
    for r, line in enumerate(ourLines):
        for c, char in enumerate(line):
            if char == '.':
                board[r,c] = 0 # technically unnecessary
            elif char == 'T':
                board[r,c] = 1
            elif char == 'X':
                board[r,c] = 2
            elif char == 'O':
                board[r,c] = 3
    # check rows and cols:
    for r in xrange(4):
        rowCheck = checkWin(board[r])
        if rowCheck is not None:
            return rowCheck
        colCheck = checkWin(board[:,r])
        if colCheck is not None:
            return colCheck
    # check main diagonal:
    diagCheck = checkWin(np.diag(board))
    if diagCheck is not None:
        return diagCheck
    # check antidiagonal by flipping the board:
    board = board[:,::-1]
    antiDiagCheck = checkWin(np.diag(board))
    if antiDiagCheck is not None:
        return antiDiagCheck
    # no win:
    if np.any(board == 0):
        return "Game has not completed"
    return "Draw"

def solve(fil):
    fOut = open("out.txt", mode = "wb")
    lNum = 0
    lines = []
    with open(fil) as f:
        for line in f:
            if lNum > 0:
                lines.append(line)
            lNum += 1

    currentCase = 1
    while len(lines) > 0:
        print "Working on Case #%d" % currentCase
        solution = solveCase(lines)
        fOut.write("Case #%d: %s\r\n" % (currentCase, solution))
        currentCase += 1
    fOut.close()
