def getLines(filename):
    with open(filename) as f:
        return f.readlines()


def appendToFile(filename, text):
    with open(filename,'a') as f:
        f.write(text + '\n')

def isArrangementPossible(x,r,c):
    if x >= 7:
        return False
    if x == 1:
        return True
    if x==2:
        if r%2 == 0 or c%2 == 0:
            return True
        return False
    if x == 3:
        if r==1 or c==1:
            return False
        if r ==2 and c == 2:
            return False
        if (r*c) % 3 == 0:
            return True
        return False
    if x == 4:
        if r < 3 or c < 3:
            return False
        if r == 3 and c == 3:
            return False
        if (r*c) % 4 == 0:
            return True
        return False
    if x==5:
        return False
    if x == 6:
        return False

lines = getLines('D-small-attempt0.in')
testsNum = int(lines[0])

for lineNum in xrange(1,testsNum + 1):
    line = lines[lineNum].split()
    x = int(line[0])
    r = int(line[1])
    c = int(line[2])

    if isArrangementPossible(x,r,c):
        appendToFile('output.txt', "Case #"+str(lineNum) + ": GABRIEL" )
    else:
        appendToFile('output.txt', "Case #"+str(lineNum) + ": RICHARD" )


