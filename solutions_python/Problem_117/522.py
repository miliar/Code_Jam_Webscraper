
import string, os, time, sys

# Count # instances of value on the lawn
def LawnCount(lawn, M, N, value):
    lawnCount = 0
    for i in range(0,M):
        lawnCount += lawn[i].count(value)
    return lawnCount

# Replace all instances of value on lawn with newValue
def ReplaceOnLawn(lawn, M, N, value, newValue):
    for i in range(0,M):
        for j in range(0,N):
            if (lawn[i][j] == value):
                lawn[i][j] = newValue

# Can the entire row be unmowed (i.e. is it all the current value)?
def CanUnmowRow(lawn, row, N, value):
    for i in range(0,N):
        if (abs(lawn[row][i]) != value):
            return False;
    return True

# Unmow the row (set its value to negative).
def UnmowRow(lawn, row, N, value):
    for i in range(0,N):
        lawn[row][i] = value * -1
    
# Can the entire column be unmowed (i.e. is it all the current value)?
def CanUnmowCol(lawn, M, col, value):
    for i in range(0,M):
        if (abs(lawn[i][col]) != value):
            return False;
    return True

# Unmow the column (set its value to negative).
def UnmowCol(lawn, M, col, value):
    for i in range(0,M):
        lawn[i][col] = value * -1
    
def RunCase(f):
    caseline = f.readline().rstrip("\r\n")
    splitline = caseline.split(" ")
    M = int(splitline[0])
    N = int(splitline[1])

    lawn = []
    heights = set()
    for i in range(0,M):
        lawn.append([])
        caseline = f.readline().rstrip("\r\n")
        splitline = caseline.split(" ")
        for j in range(0,N):
            lawn[i].append(int(splitline[j]))
            heights.add(int(splitline[j]))

    heightList = list(heights)
    heightList.sort()

    for i in range(0,len(heightList)-1):
        thisHeight = heightList[i]
        nextHeight = heightList[i+1]
        for m in range(0,M):
            if CanUnmowRow(lawn, m, N, thisHeight):
                UnmowRow(lawn, m, N, thisHeight)
        for n in range(0,N):
            if CanUnmowCol(lawn, M, n, thisHeight):
                UnmowCol(lawn, M, n, thisHeight)
        ReplaceOnLawn(lawn, M, N, thisHeight*-1, nextHeight)
        if LawnCount(lawn, M, N, thisHeight) != 0:
            return False

    highestHeight = heightList[len(heightList)-1]
    if LawnCount(lawn, M, N, highestHeight) == M*N:
        return True

    return False



def HandleCase(f, caseIndex):

    if (RunCase(f)):
        print "Case #%(count)d: YES" % {"count":caseIndex}
    else:
        print "Case #%(count)d: NO" % {"count":caseIndex}

 

inputFile = sys.argv[1]
f = open(inputFile, "r")
numCases = int(f.readline())
for i in range(0, numCases):
    HandleCase(f, i+1)

