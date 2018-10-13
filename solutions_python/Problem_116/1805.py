def getCol(col, board):
    r = ''
    for row in board:
        r += row[col]
    return r.strip()

def getDiag(backwards, board):
    r = ''
    if backwards:
        pos = 0
        for row in board:
            r += row[pos]
            pos += 1
    else:
        pos = 3
        for row in board:
            r += row[pos]
            pos -= 1
    return r.strip()

def checkDraw(board):
    draw = True
    for row in board:
        if row.count('.') > 0:
            draw = False
    return draw

def check(quartet, outputFile):
    print 'checking', quartet
    if quartet.count('.') > 0:
        return False
    if quartet.count('X') == 4 or (quartet.count('X') == 3 and quartet.count('T') == 1):
        outputFile.write("X won")
        return True
    if quartet.count('O') == 4 or (quartet.count('O') == 3 and quartet.count('T') == 1):
        outputFile.write("O won")
        return True
    return False

def solve(cases, inFile, outputFile):
    for c in xrange(1, cases + 1):
        outputFile.write("Case #" + str(c) + ": ")
        board = []
        for n in xrange(0, 4):
            board.append(inFile.readline())
        skip = inFile.readline()
        print 'NEW BOARD', board

        unsolved = True
        # Check rows
        for row in board:
            if check(row, outputFile):
                unsolved = False
                break
        if not unsolved:
            outputFile.write('\n')
            continue
        # Check cols
        for n in xrange(0, 4):
            if check(getCol(n, board), outputFile):
                unsolved = False
                break
        if not unsolved:
            outputFile.write('\n')
            continue
        # Check diags
        if check(getDiag(True, board), outputFile):
            unsolved = False
        if not unsolved:
            outputFile.write('\n')
            continue
        if check(getDiag(False, board), outputFile):
            unsolved = False
        if not unsolved:
            outputFile.write('\n')
            continue
        if unsolved:
            if checkDraw(board):
                outputFile.write("Draw")
            else:
                outputFile.write("Game has not completed")
        outputFile.write('\n')


inFile = open('A-large.in')
outputFile = open('output.txt', 'w')

cases = int(inFile.readline())
print cases, ' cases read'

solve(cases, inFile, outputFile)
print 'done'

inFile.close()
outputFile.close()