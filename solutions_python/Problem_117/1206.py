import numpy as np

def reductionStep(board, h):
    # performs a reduction step on the board
    # all grass of height h => h+1
    # returns (newBoard, isSuccessful)
    rows, cols = board.shape
    toAdjust = (board == h)
    for r in xrange(rows):
        curRow = board[r]
        if (curRow == h).all():
            toAdjust[r] = 0
    for c in xrange(cols):
        curCol = board[:,c]
        if (curCol == h).all():
            toAdjust[:,c] = 0
    if not (toAdjust == 0).all():
        return (board, False)
    else:
        board[board == h] = h+1
        return (board, True)

def solveBoard(board):
    minH = board.min()
    maxH = board.max()
    for h in xrange(minH, maxH):
        board, success = reductionStep(board, h)
        if not success:
            return "NO"
    return "YES"

def solveCase(lines):
    rows, cols = [int(x) for x in lines.pop(0).split(' ')]
    lawn = np.zeros((rows, cols), dtype=int)
    for i in xrange(rows):
        curLine = [int(x) for x in lines.pop(0).split(' ')]
        lawn[i] = curLine
    return solveBoard(lawn)

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
