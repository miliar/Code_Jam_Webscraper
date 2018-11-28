# Check rows if 3X's/O's and a T
# Check columns if 3X's/O's and a T
# Check diaginals if 3X's/O's and a T
# If there are no dots then draw
# Else Game has no completede

# Split rows: split by /n
# split columns: split by /n and take ith element
# split diaginals: custom indexs



# Returns state of string
def checkString(s):
    if (s.count('X') + s.count('T')) == 4:
        return 'X won'
    elif (s.count('O') + s.count('T')) == 4:
        return 'O won'
    elif s.count('.') > 0:
        return 'Game has not completed'
    else:
        return None

    
# Returns a list of rows
def getRows(s):
    return s.split('\n')

# Returns a list of cloumns
def getColoumns(s):
    cols = ['', '', '', '']
    for row in s.split('\n'):
        cols[0] = cols[0] + row[0]
        cols[1] = cols[1] + row[1]
        cols[2] = cols[2] + row[2]
        cols[3] = cols[3] + row[3]

    return cols

# Returns a list of diagonals
def getDiagonals(s):
    diag = ['', '']
    for i, row in enumerate(s.split('\n')):
        diag[0] = diag[0] + row[i]
        diag[1] = diag[1] + row[3-i]

    return diag

# Checks a grid for win, draw, no complete state
def getStates(g):

    states = []
    
    for row in getRows(g):
        states.append(checkString(row))

    for col in getColoumns(g):
        states.append(checkString(col))

    for diag in getDiagonals(g):
        states.append(checkString(diag))

    return states


# Takes a list of states and determins the overall state
def overallState(s, g):
    winning = []
    notComplete = []
    draw = []

    for state in s:
        if state == 'X won' or state == 'O won':
            winning.append(state)
        elif state == 'Game has not completed':
            notComplete.append(state)
        elif state == None:
            draw.append(state)
        else:
            print('ERROR Unkown state %s returned on grid \n%s' % (state, g))

    if len(winning) == 1:
        return winning[0]
    elif len(winning) == 0 and len(draw) == 10 and len(notComplete) == 0:
        return 'Draw'
    elif len(winning) == 0 and len(notComplete) >= 1:
        return 'Game has not completed'
    elif len(winning) > 1:
        print(winning)
        return winning[0]
    else:
        print('ERROR incorrect count of states [winning: %s, notComplete: %s, draw: %s] on grid \n%s' % (len(winning), len(notComplete), len(draw), g))
        return '-- ERROR --'

def printOutput(out):
    for i, s in enumerate(out):
        print('Case #%s: %s' % (i + 1, s))

def storeOutput(out):
    ouputFile = open('output.txt', 'a')     # MAKE SURE it exsits previously

    for i, s in enumerate(out):
        ouputFile.write('Case #%s: %s\n' % (i + 1, s))

        
def GAMEON():
    inputFile = open('input.txt', 'r')

    output = []

    data = inputFile.read()

    inputFile.close()

    numOfGrids = data.split('\n')[0]

    print('Number of grids #%s' % numOfGrids)

    data = '\n'.join((data.split('\n')[1:]))
    
    for i, grid in enumerate(data.split('\n\n')):
        if len(grid) == 19 or len(grid) == 20:
            states = getStates(grid)
            output.append(overallState(states, grid))
        else:
            print('ERROR incorrectly formated grid %s' % grid)

    if (i + 1) != int(numOfGrids):
        print('ERROR mis matching grids and number of grids')

    printOutput(output)
    storeOutput(output)

GAMEON()
