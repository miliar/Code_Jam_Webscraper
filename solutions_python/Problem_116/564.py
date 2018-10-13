
def readFile(file):
    f = open(file, 'r')
    totalStates = f.readline()
    lines = f.readlines()
    f.close()
    gamestates = []
    state = []
    for line in lines:
        if line == '\n':
            gamestates.append(state)
            state = []
            continue
        state.append(line)
    if len(state) > 0:
        gamestates.append(state)
    return totalStates, gamestates

def getQuads(state):
    quads = ()
    rows = [r[:-1] for r in state]
    columns = []
    for cI in range(len(state[0]) - 1):
        column = ''
        for rI in range(len(state)):
            column += state[rI][cI]
        columns.append(column)
    diagonals = []
    diagonals.append( ''.join([state[i][i] for i in range(len(state)) ]) )
    diagonals.append( ''.join([ state[i][len(state) - i - 1] for i in range(len(state)) ]) )
    quads = rows + columns + diagonals
    return quads

def isFull(state):
    for row in state:
        if '.' in row: return False
    return True
    
def wins(quads):
    xwins = ('XXXX', 'XXXT', 'XXTX', 'XTXX', 'TXXX')
    owins = ('OOOO', 'OOOT', 'OOTO', 'OTOO', 'TOOO')
    for quad in quads:
        if quad in xwins:
            return 'X'
        elif quad in owins:
            return 'O'
    return None

def checkGameState(input, outfile):
    totalStates, gamestates = readFile(input)
    output = []
    for index, state in enumerate(gamestates):
        #for word1,word2 in ((w1,w2) for w1 in buf1 for w2 in buf2):
        quads = getQuads(state)
        result = wins(quads)
        if result != None:
            output.append("Case #" + str(index + 1) + ": " + result + " won")
        elif isFull(state):
            output.append("Case #" + str(index + 1) + ": Draw")
        else:
            output.append("Case #" + str(index + 1) + ": Game has not completed")
    output = '\n'.join(output)
    f = open(outfile, 'w')
    f.write(output)
#inputFile = 'A-small-attempt2.in'
inputFile = 'A-large.in'
outputFile = 'output.txt'
checkGameState(inputFile, outputFile)
