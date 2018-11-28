#!/usr/bin/python
# gg code jam 2013.
# Input: a file with lines and stuff.  

# There are only 10 ways of getting a win.
# 4 hor's
# 4 vert's
# 2 diags.

# Change all the free spaces to 100.
# All the X's to 1
# All the O's to -1
# All the T's to 0
# Then we can just do the sum of each of these things. 
import sys

def evalBoard(boardArr, caseNum):
    result = ''

    rowSums = dict()
    colSums = dict()
    diagSums = dict()
    bigsum = 0

    for x in range(4):
        rowSums[x] = 0
        colSums[x] = 0
        diagSums[x] = 0

    for row in range(4):
        diagSums[0] += boardArr[row][row]
        diagSums[1] += boardArr[row][3 - row]
        for col in range(4):
            rowSums[row] += boardArr[row][col]
            colSums[col] += boardArr[row][col]
            bigsum += boardArr[row][col]

    #print rowSums
    #print colSums
    #print diagSums
    for x in range(4):
        if (rowSums[x] > 2 and rowSums[x] < 10) or (colSums[x] >2 and colSums[x] < 10) or (diagSums[x] > 2 and diagSums[x] < 10):
            print 'Case #{}: X won'.format(caseNum)
            return
        elif (rowSums[x] < -2 and rowSums[x] > -10) or (colSums[x] < -2 and colSums[x] > -10) or (diagSums[x] < -2 and diagSums[x] > -10):
            print 'Case #{}: O won'.format(caseNum)
            return
    if bigsum > 50:
        print 'Case #{}: Game has not completed'.format(caseNum)
    else:
        print 'Case #{}: Draw'.format(caseNum)

fName = sys.argv[1]
ff = open(fName)
allLines = ff.readlines()
numCases = int(allLines[0])
mapping = {'.': 100, 'T':0, 'X':1, 'O':-1}

for case in range(numCases):
    startLine = 1 + 5 * case
    endLine   = 4 + 5 * case
    boardArr = list()
    for x in range(4):
        newCol = list()
        for y in range(4):
            newCol.append(mapping[allLines[startLine + x][y]])
        boardArr.append(newCol)
    evalBoard(boardArr, case + 1)

