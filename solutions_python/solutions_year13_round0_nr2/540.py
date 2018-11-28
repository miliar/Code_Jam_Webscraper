#!/usr/bin/python
import os, sys, math

def checkDone(curLawn, desiredLawn):
    for i in range(len(desiredLawn)):
        for j in range(len(desiredLawn[i])):
            if (desiredLawn[i][j] != curLawn[i][j]):
                return False
    return True

def checkImpossible(curLawn, desiredLawn):
    for i in range(len(desiredLawn)):
        for j in range(len(desiredLawn[i])):
            if (desiredLawn[i][j] > curLawn[i][j]):
                return True
    return False

def copyLawn(lawn):
    return [row[:] for row in lawn]

def findDesiredSquare(curLawn, desiredLawn):
    for i in range(len(desiredLawn)):
        for j in range(len(desiredLawn[i])):
            if (desiredLawn[i][j] < curLawn[i][j]):
                return i, j
    return -1, -1

def solveIter(curLawn, desiredLawn):
    if checkDone(curLawn, desiredLawn):
        return True
    if checkImpossible(curLawn, desiredLawn):
        return False
    # Find the first square that's not the right height and try to cut it
    i, j = findDesiredSquare(curLawn, desiredLawn)
    cutTo = desiredLawn[i][j]
    # Cut horizontal
    tempLawn = copyLawn(curLawn)
    for k in range(len(tempLawn[i])):
        tempLawn[i][k] = cutTo
    if solveIter(tempLawn, desiredLawn):
        return True
    # Cut vertical
    tempLawn = copyLawn(curLawn)
    for k in range(len(tempLawn)):
        tempLawn[k][j] = cutTo
    return solveIter(tempLawn, desiredLawn)

def solve(desiredLawn):
    maxHeight = max([max(row) for row in desiredLawn])
    curLawn = [[maxHeight for col in row] for row in desiredLawn]
    #print maxHeight
    return solveIter(curLawn, desiredLawn)

def main(filename):
    fileLines = open(filename, 'r').readlines()
    index = 0
    numCases = int(fileLines[index][:-1])
    index += 1
    for caseNum in range(numCases):
        n, m = [int(x) for x in fileLines[index][:-1].split(' ')]
        index += 1
        case = []
        for i in range(n):
            case.append([int(x) for x in fileLines[index+i][:-1].split(' ')])
        # blank line
        index += n
        #print case
        answer = solve(case)
        #print caseStr
        print "Case #%d: %s" % (caseNum + 1, 'YES' if answer else 'NO')

if __name__ == '__main__':
    main(sys.argv[1])
