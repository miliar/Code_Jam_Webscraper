#!/usr/bin/python
import os, sys, math

def placeStudents(W, L, reaches):
    # sort with largest reach first
    positions = [None for i in range(len(reaches))]
    sortedReaches = []
    for i in range(len(reaches)):
        sortedReaches.append((reaches[i], i))
    sortedReaches = sorted(sortedReaches)[::-1]
    realPositions = []
    positionsToTry = []
    def addPosition(x, y, r, i):
        positions[i] = (x,y)
        realPositions.append((x,y,r))
        if x+r < W:
            positionsToTry.append((x+r,y,0))
        if y+r < L:
            positionsToTry.append((x,y+r,1))
        if x-r > 0:
            positionsToTry.append((x-r,y,2))
        if y-r > 0:
            positionsToTry.append((x,y-r,3))
    def canPlace(x, y, r):
        if x < 0 or x > W or y < 0 or y > L:
            return False
        for (x1,y1,r1) in realPositions:
            if abs(x - x1) < (r + r1) and abs(y - y1) < (r + r1):
                return False
        return True

    for (r, index) in sortedReaches:
        #print r, index
        if (len(realPositions) == 0):
            addPosition(0,0,r,index)
            continue
        # try some positions
        #print positionsToTry
        for i in range(len(positionsToTry)):
            (x, y, edge) = positionsToTry[i]
            if edge == 0:
                x = x + r
            elif edge == 1:
                y = y + r
            elif edge == 2:
                x = x - r
            elif edge == 3:
                y = y - r
            if (canPlace(x, y, r)):
                positionsToTry = positionsToTry[:i] + positionsToTry[i+1:]
                addPosition(x,y,r,index)
                continue

    # (reach, index)
    #print sortedReaches
    return positions


def main(filename):
    fileLines = open(filename, 'r').readlines()
    index = 0
    numCases = int(fileLines[index][:-1])
    index += 1
    for caseNum in range(numCases):
        N, W, L = [int(x) for x in fileLines[index][:-1].split(' ')]
        index += 1
        reaches = [int(x) for x in fileLines[index][:-1].split(' ')]
        index += 1
        #canDo = canVineCrawl(vines, D, 0, 0)
        positions = placeStudents(W, L, reaches)
        print "Case #%d: %s" % (caseNum + 1, ' '.join([' '.join([str(x[0]), str(x[1])]) for x in positions]))

if __name__ == '__main__':
    main(sys.argv[1])
