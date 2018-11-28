#!/usr/bin/python
import os, sys

def coaster(R, k, gs):
    money = 0
    gSpot = 0
    l = len(gs)
    # quick check - if all can fit, don't loop
    if sum(gs) <= k:
        return R * sum(gs)
    for i in range(R):
        #print 'round %d' % i
        freeSpaces = k
        while freeSpaces >= gs[gSpot]:
            #print 'spot %d gets on' % gSpot
            # Let the next people on
            money += gs[gSpot]
            freeSpaces -= gs[gSpot]
            gSpot += 1
            if gSpot == l:
                gSpot = 0
    return money

def main(filename):
    fileLines = open(filename, 'r').readlines()
    index = 0
    numCases = int(fileLines[index][:-1])
    index += 1
    for caseNum in range(numCases):
        (R, k, N) = [int(x) for x in fileLines[index][:-1].split(' ')]
        index += 1
        gs = [int(x) for x in fileLines[index][:-1].split(' ')]
        index += 1
        #print caseStr
        answer = coaster(R, k, gs)
        print "Case #%d: %d" % (caseNum+1, answer)

if __name__ == '__main__':
    main(sys.argv[1])
