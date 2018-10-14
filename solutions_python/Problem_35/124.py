"""
Author: Greg Harfst (gharfst@gmail.com)
Date:   9/3/2009
Notes:

Problem

Geologists sometimes divide an area of land into different regions based on where rainfall flows down to. These regions are called drainage basins.

Given an elevation map (a 2-dimensional array of altitudes), label the map such that locations in the same drainage basin have the same label, subject to the following rules.

    * From each cell, water flows down to at most one of its 4 neighboring cells.
    * For each cell, if none of its 4 neighboring cells has a lower altitude than the current cell's, then the water does not flow, and the current cell is called a sink.
    * Otherwise, water flows from the current cell to the neighbor with the lowest altitude.
    * In case of a tie, water will choose the first direction with the lowest altitude from this list: North, West, East, South.

Every cell that drains directly or indirectly to the same sink is part of the same drainage basin. Each basin is labeled by a unique lower-case letter, in such a way that, when the rows of the map are concatenated from top to bottom, the resulting string is lexicographically smallest. (In particular, the basin of the most North-Western cell is always labeled 'a'.)

Input

The first line of the input file will contain the number of maps, T. T maps will follow, each starting with two integers on a line -- H and W -- the height and width of the map, in cells. The next H lines will each contain a row of the map, from north to south, each containing W integers, from west to east, specifying the altitudes of the cells.

Output

For each test case, output 1+H lines. The first line must be of the form

Case #X:

where X is the test case number, starting from 1. The next H lines must list the basin labels for each of the cells, in the same order as they appear in the input. 

"""

import sys

def chooseNeighbor(topMap, rowNum, colNum):
    """
    
    Arguments:
    - `topMap`:
    - `rowNum`:
    - `colNum`:
    """
    lowRow, lowCol = rowNum, colNum
    if (rowNum > 0) and (topMap[lowRow][lowCol] > topMap[rowNum-1][colNum]):
        lowRow, lowCol = rowNum-1, colNum
    if (colNum > 0) and (topMap[lowRow][lowCol] > topMap[rowNum][colNum-1]):
        lowRow, lowCol = rowNum, colNum-1
    if (colNum < len(topMap[0]) - 1) and (topMap[lowRow][lowCol] > topMap[rowNum][colNum+1]):
        lowRow, lowCol = rowNum, colNum+1
    if (rowNum < len(topMap) - 1) and (topMap[lowRow][lowCol] > topMap[rowNum+1][colNum]):
        lowRow, lowCol = rowNum+1, colNum
    return lowRow, lowCol

def flowWater(topMap, labeledMap, rowNum, colNum, label):
    """
    
    Arguments:
    - `topMap`:
    - `labeledMap`:
    - `rowNum`:
    - `colNum`:
    - `label`:
    """
    if labeledMap[rowNum][colNum] != '-':
        return False, labeledMap[rowNum][colNum]

    lowRow, lowCol = chooseNeighbor(topMap, rowNum, colNum)
    if (lowRow, lowCol) == (rowNum, colNum):
        labeledMap[rowNum][colNum] = label
        return True, labeledMap[rowNum][colNum]
    else:
        foundSink, newLabel = flowWater(topMap, labeledMap, lowRow, lowCol, label)
        labeledMap[rowNum][colNum] = labeledMap[lowRow][lowCol]
        return foundSink, labeledMap[rowNum][colNum]

def main():
    input = [l.strip() for l in sys.stdin.readlines()]
    numMaps = int(input[0])
    mapOffset = 1
    for i in range(numMaps):
        h, w = map(int, input[mapOffset].split())
        topMap = []
        for rowNum in range(h):
            topMap.append(map(int, input[mapOffset+1+rowNum].split()))
        mapOffset += h + 1

        labeledMap = []
        for row in topMap:
            labeledMap.append(['-' for x in row])
        label = 'a'
        for rowNum in range(h):
            for colNum in range(w):
                foundSink, _ = flowWater(topMap, labeledMap, rowNum, colNum, label)
                if foundSink:
                    label = str(chr(ord(label) + 1))

        print "Case #%d:" % (i+1)
        for row in labeledMap:
            print " ".join(row)

if __name__ == "__main__":
    main()
