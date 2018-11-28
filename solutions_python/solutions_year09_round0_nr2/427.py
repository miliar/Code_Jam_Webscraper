#!/usr/bin/python

import sys

# returns tuple of form (x, y)
def flowsTo(x, y, eMap, height, width):
    lowest, lowestX, lowestY = eMap[y][x], x, y
    for i, j in [(y-1, x), (y, x - 1), (y, x), (y, x+1), (y+1, x)]:
        if i >= height or i < 0 or j >= width or j < 0:
            continue
        if eMap[i][j] < lowest:
            lowest, lowestX, lowestY = eMap[i][j], j, i
    if lowest == eMap[y][x]:
        return (x, y)
    return flowsTo(lowestX, lowestY, eMap, height, width)
    
def isSink(x, y, eMap, height, width):
    return (x, y) == flowsTo(x, y, eMap, height, width)

def processMap(eMap, height, width, caseNo):
    print "Case #" + str(caseNo) + ':'
    l = []
    for y in xrange(height):
        l.append([])
        for x in xrange(width):
            l[y].append(flowsTo(x, y, eMap, height, width))
    letters = 'abcdefghijklmnopqrstuvwxyz'
    letterIndex = 0
    mapDict = {}
    for y in range(height):
        for x in range(width):
            sink = l[y][x]
            if sink not in mapDict:
                mapDict[sink] = letters[letterIndex]
                letterIndex += 1
            print mapDict[sink],
        print
    
def main():
    f = open(sys.argv[1], 'r')
    cases = int(f.readline())
    for i in range(cases):
        height, width = [int(n) for n in f.readline().split()]
        eMap = []
        for j in range(height):
            eMap.append([int(n) for n in f.readline().split()])
        processMap(eMap, height, width, i + 1)
    f.close()

main()
