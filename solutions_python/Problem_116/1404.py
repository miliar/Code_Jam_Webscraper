import sys

def readTestCase(fileContents, startIndex, numRows):
    grid = []
    for r in range(numRows):
        grid.append(fileContents[startIndex])
        startIndex += 1

    return (startIndex, grid)

def checkWinner(checkSide, checkStr):
    requiredCount = len(checkStr)
    filteredStr = [x for x in checkStr if x == checkSide or x == 'T']
    return len(filteredStr) == requiredCount

# Get the input file name
inputFileName = sys.argv[1]

# Read file contents
with open(inputFileName) as f:
    contents = [line.strip() for line in f.readlines()]

# Get number of inputs
lineNum = 0;
numInputs = int(contents[lineNum])
lineNum += 1

# Fixed grid size
GRIDSIZE = 4

for i in range(numInputs):
    testNum = i+1

    # Read in input
    (lineNum, grid) = readTestCase(contents, lineNum, GRIDSIZE)
    lineNum += 1    # Skip over empty line

    # Check rows and cols
    isFinished = False
    for r in range(GRIDSIZE):
        rowStr = grid[r]

        checkSide = 'X'
        if checkWinner(checkSide, rowStr):
            print "Case #%d: %s won" % (testNum, checkSide)
            isFinished = True
            break

        checkSide = 'O'
        if checkWinner(checkSide, rowStr):
            print "Case #%d: %s won" % (testNum, checkSide)
            isFinished = True
            break

    if isFinished:
        continue

    for c in range(GRIDSIZE):
        colStr = ''.join([row[c] for row in grid])

        checkSide = 'X'
        if checkWinner(checkSide, colStr):
            print "Case #%d: %s won" % (testNum, checkSide)
            isFinished = True
            break

        checkSide = 'O'
        if checkWinner(checkSide, colStr):
            print "Case #%d: %s won" % (testNum, checkSide)
            isFinished = True
            break

    if isFinished:
        continue

    # Check diagonals
    majorDiagStr = ''
    minorDiagStr = ''
    for i in range(GRIDSIZE):
        majorDiagStr += grid[i][i]
        minorDiagStr += grid[i][GRIDSIZE-i-1]

    checkSide = 'X'
    if checkWinner(checkSide, majorDiagStr):
        print "Case #%d: %s won" % (testNum, checkSide)
        continue
    if checkWinner(checkSide, minorDiagStr):
        print "Case #%d: %s won" % (testNum, checkSide)
        continue

    checkSide = 'O'
    if checkWinner(checkSide, majorDiagStr):
        print "Case #%d: %s won" % (testNum, checkSide)
        continue
    if checkWinner(checkSide, minorDiagStr):
        print "Case #%d: %s won" % (testNum, checkSide)
        continue


    # No one has one, so see if the game's over (i.e. there exist any '.').
    # If so, game hasn't finished yet
    for r in range(GRIDSIZE):
        if '.' in grid[r]:
            print "Case #%d: Game has not completed" % testNum
            isFinished = True
            break
            
    if isFinished:
        continue

    # Else: draw
    print "Case #%d: Draw" % testNum

