#inputFileName = "test.in"
inputFileName = "A-small-attempt0.in"
#inputFileName = "A-large.in"
outputFileName = inputFileName[:-3] + ".out"

N = 4
XWon = "X won"
OWon = "O won"
Draw = "Draw"
NotCompleted = "Game has not completed"

def getXLine(data, x):
    for line in data:
        yield line[x]


def getD1Line(data):
    x = 0
    for line in data:
        yield line[x]
        x += 1


def getD2Line(data):
    x = 0
    l = len(data)
    for line in data:
        x += 1
        yield line[l - x]


def checkLine(line, player):
    for c in line:
        if c != 'T' and c != player:
            return False
    return True


def checkWin(data, player):
    for line in data:
        if checkLine(line, player):
            return True

    for x in xrange(N):
        if checkLine(getXLine(data, x), player):
            return True

    if checkLine(getD1Line(data), player):
        return True

    if checkLine(getD2Line(data), player):
        return True

    return False


def calcSingleTest(f):
    data = []
    completed = True
    line = f.readline()
    a1 = int(line)
    c1 = []
    for y in range(4):
        line = f.readline()
        c1.append(map(int, line.split()))

    line = f.readline()
    a2 = int(line)
    c2 = []
    for y in range(4):
        line = f.readline()
        c2.append(map(int, line.split()))

    g1 = c1[a1-1]
    g2 = c2[a2-1]
    print g1
    print g2
    answ = set(g1) & set(g2)
    print answ
    l = len(answ)
    if l == 1:
        return list(answ)[0]
    elif l == 0:
        return "Volunteer cheated!"
    else:
        return "Bad magician!"


with open(inputFileName) as inpF:
    with open(outputFileName, 'w') as outF:
        line = inpF.readline()
        testsCount = int(line)
        for i in xrange(1, testsCount + 1):
            print '--------------------------------------------'
            res = calcSingleTest(inpF)
            outF.write('Case #{0}: {1}\n'.format(i, res))




