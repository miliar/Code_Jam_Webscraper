#!/usr/bin/python
import os, sys
import operator

def lastRowOne(r):
    toReturn = 0
    for (i, v) in enumerate(r):
        if v == 1:
            toReturn = i
    return toReturn

def findRowSwaps(acceptableRows, pos):
    numSwaps = 0
    if len(acceptableRows) == 1:
        return numSwaps
    if pos >= len(acceptableRows):
        return 0
    # Find the first thing that can go in position pos
    firstGoodPos = -1
    for i in range(pos, len(acceptableRows)):
        if acceptableRows[i] <= pos:
            firstGoodPos = i
            break
    #print 'firstgoodpos %d' % firstGoodPos
    if firstGoodPos > pos:
        # Swap firstGoodPos up to pos
        src = pos
        dst = firstGoodPos
        swaps = dst - src
        numSwaps += swaps
        # swap array
        tmp = acceptableRows[dst]
        for i in range(dst-1, src-1, -1):
            acceptableRows[i+1] = acceptableRows[i]
        acceptableRows[src] = tmp
        #print acceptableRows
    return numSwaps + findRowSwaps(acceptableRows, pos+1)
 
    # Find first row that's bad
    #lastBadRow = -1
    #for i in range(len(acceptableRows)-1, -1, -1):
        #if acceptableRows[i] > i:
            #lastBadRow = i
            #break
    #print acceptableRows
    #while lastBadRow != -1:
        #print 'lBR: %d' % lastBadRow
        ## Swap lastBadRow down.
       #lastBadRow = -1
        #print acceptableRows
        #for i in range(len(acceptableRows)-1, -1, -1):
            #if acceptableRows[i] > i:
                #lastBadRow = i
                #break
#
    ## Done!
    #return numSwaps

    # Can ignore stuff before this
    # Need to swap lastBadRow up to an acceptable position.

        


def main(filename):
    fileLines = open(filename, 'r').readlines()
    index = 0
    words = []
    numCases = int(fileLines[index][:-1])
    index += 1
    for caseNum in range(numCases):
        numRows = int(fileLines[index][:-1])
        index += 1
        rows = [[] for x in xrange(numRows)]
        for i in xrange(numRows):
            rows[i] = [int(x) for x in fileLines[index][:-1]]
            index += 1
        #print rows
        # Build up the acceptable rows
        acceptableRows = []
        for i in xrange(numRows):
            acceptableRows.append(lastRowOne(rows[i]))
        #print acceptableRows
        numSwaps = findRowSwaps(acceptableRows, 0)
        print "Case #%d: %d" % (caseNum+1, numSwaps)


if __name__ == '__main__':
    main(sys.argv[1])
