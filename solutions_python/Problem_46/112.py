"""
Author: Greg Harfst (gharfst@gmail.com)
Date:   9/26/2009
Notes:

"""

import sys
import re
import numpy as NP

def generateTestCases(lines):
    while lines:
        numLines = int(lines.pop(0))
        matrix = []
        for i in range(numLines):
            matrix.append(NP.array(map(int, lines.pop(0))))
        yield NP.array(matrix)

def makeTest(size):
    m = []
    for i in range(size):
        row = [(1 if x > i else 0) for x in range(size)]
        m.append(row)
    return NP.array(m)

def isDiagonal(m, test):
    return NP.max(NP.multiply(m, test)) == 0

def findWorstRow(m):
    worstRow = 0
    worstAmount = 0
    for rowNum in range(m.shape[0]):
        bads = [i for i,x in enumerate(m[rowNum]) if x > 0 and i > rowNum]
        if bads:
            badAmount = bads[-1] - rowNum
            if badAmount > worstAmount:
                worstRow = rowNum
            elif badAmount == worstAmount and NP.sum(m[rowNum]) > NP.sum(m[worstRow]):
                worstRow = rowNum
    return worstRow

def findFirstRowToMoveUp(m, r):
    for rowNum in range(r, m.shape[0]):
        bads = [i for i,x in enumerate(m[rowNum]) if x > 0 and i > r]
        if not bads:
            return rowNum

def swap(m, r1, r2):
    t = m[r2].copy()
    m[r2] = m[r1]
    m[r1] = t
    return m

def countSwaps(matrix):
    test = makeTest(matrix.shape[0])
    count = 0
#    print "============="
    while not isDiagonal(matrix, test):
#        print matrix
        worstRow = findWorstRow(matrix)
        goodRow = findFirstRowToMoveUp(matrix, worstRow)
        swap(matrix, goodRow, goodRow-1)
        count += 1
#    print matrix
    return count

def main():
    input = [l.strip() for l in sys.stdin.readlines()]
    for testNum, matrix in enumerate(generateTestCases(input[1:])):
        numSwaps = countSwaps(matrix)
        print "Case #%d: %d" % (testNum+1, numSwaps)

if __name__ == "__main__":
    main()
