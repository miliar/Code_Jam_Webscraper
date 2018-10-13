inputFile = open("B-large.in")

line = inputFile.readline()[:-1]
number = int(line)

def validCut(mow, lawn):
    for i in range(len(lawn)):
        theseCuts = []
        for cutLength in lawn[i]:
            if cutLength not in theseCuts:
                theseCuts.append(cutLength)
        theseCuts.sort()
        for thisCut in theseCuts:
            cols = []
            for j in range(len(lawn[i])):
                if lawn[i][j] == thisCut:
                    cols.append(j)
            if (not checkRow(thisCut, i, lawn)) and (not checkCol(thisCut, cols, lawn)):
                print "Case #" + str(mow + 1) + ": NO"
                return
    print "Case #" + str(mow + 1) + ": YES"
    return

def checkRow(cut, row, lawn):
    if len(lawn[row]) == 0:
        return True
    for j in range(len(lawn[row])):
        if lawn[row][j] > cut:
            return False
    return True

def checkCol(cut, cols, lawn):
    if len(lawn) == 1:
        return True
    for col in cols:
        for i in range(len(lawn)):
            if lawn[i][col] > cut:
                return False
    return True

for mow in range(number):
    line = inputFile.readline()[:-1]
    dimensions = line.split(" ")
    rows = int(dimensions[0])
    cols = int(dimensions[1])
    lawn = []
    for row in range(rows):
        line = inputFile.readline()[:-1]
        thisRow = line.split(" ")
        lawn.append(thisRow)
    for row in range(rows):
        for col in range(cols):
            lawn[row][col] = int(lawn[row][col])
    validCut(mow, lawn)
