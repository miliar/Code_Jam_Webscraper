def getCol(col, field):
    r = []
    for row in field:
        r.append(row[col])
    return r

def allOfValue(line, value):
    r = True
    for level in line:
        if level != value:
            r = False
            break
    return r

def allOfSameValue(line):
    return allOfValue(line, line[0])

def isRowValid(row, field):
    valid = True
    if not allOfSameValue(row):
        for valNum in xrange(0, len(row)):
            if row[valNum] == 1 and not allOfSameValue(getCol(valNum, field)):
                valid = False
                break
    return valid

def solve(cases, inFile, outputFile):
    for c in xrange(1, cases + 1):
        outputFile.write("Case #" + str(c) + ": ")

        dimensions = map(int, inFile.readline().split())
        print "DIMENSIONS", dimensions

        field = []
        for row in xrange(0, dimensions[0]):
            field.append(map(int, inFile.readline().split()))
        print "FIELD", field

        possible = True
        for row in field:
            if not isRowValid(row, field):
                possible = False
                break
        if possible:
            outputFile.write('YES')
        else:
            outputFile.write('NO')
        outputFile.write('\n')


inFile = open('B-small-attempt1.in')
outputFile = open('output.txt', 'w')

cases = int(inFile.readline())
print cases, ' cases read'

solve(cases, inFile, outputFile)
print 'done'

inFile.close()
outputFile.close()