#!/bin/env python

import sys
import string

def process(numTestCase, altList, numRow, numCol):
    numCells = (numRow * numCol)
    flowList = [10001] * numCells
    outList = ['A'] * numCells
    for cellNo, alt in enumerate(altList):
        flowList[cellNo] = cellNo
        neighbors = []
        north = cellNo - numCol
        if north >= 0:
            neighbors.append(north)
        west = cellNo - 1
        if west >= 0 and west/numCol == cellNo/numCol:
            neighbors.append(west)
        east = cellNo + 1
        if east < numCells and east/numCol == cellNo/numCol:
            neighbors.append(east)
        south = cellNo + numCol
        if south < numCells:
            neighbors.append(south)
        for cell in neighbors:
            if cell >= 0 and cell < numCells  and altList[cell] < altList[flowList[cellNo]]: flowList[cellNo] = cell
    basinCounter = 0
    processedCells = 0
    pCell = 0
    while processedCells < numCells:
        while outList[pCell] != 'A':
            pCell += 1
        tmp = []
        curCell = pCell
        while curCell != flowList[curCell]:
            tmp.append(curCell)
            curCell = flowList[curCell]
        tmp.append(curCell)
        for t in tmp:
            basin = outList[tmp[-1]]
            if basin == 'A':
                basin = string.lowercase[basinCounter]
                outList[tmp[-1]] = basin
                processedCells += 1
                basinCounter += 1
            if outList[t] == 'A':
                outList[t] = basin
                processedCells += 1
    print "Case #" + str(numTestCase) + ":"
    for i, c in enumerate(outList):
        print c,
        if not (i + 1) % numCol:
            print


def testcase(fileName):
    T = None
    numCol = None
    numRow = None
    numTestCase = 0
    altList = []
    for line in open(fileName):
        if T is None:
            T = int(line)
            continue
        if numRow is None:
            numRow = int(line.split()[0])
            numCol = int(line.split()[1])
            readRows = 0
            continue
        if readRows < numRow:
            readRows += 1
            cells = line.split()
            for cell in cells:
                altList.append(int(cell))
            continue
        numTestCase += 1
        process(numTestCase, altList, numRow, numCol)
        numRow = int(line.split()[0])
        numCol = int(line.split()[1])
        readRows = 0
        altList = []
    numTestCase += 1
    process(numTestCase, altList, numRow, numCol)


if __name__ == '__main__':
    testcase(sys.argv[1])

