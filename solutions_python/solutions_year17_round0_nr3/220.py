from __future__ import print_function
import sys
from collections import defaultdict

# print to stderr for debugging
enableDebug = False
def printe(*stuff):
    if enableDebug:
        print(*stuff, file=sys.stderr) 


# Open file for processing
filename = sys.argv[1]
inputFile = open(filename, 'r')
lines = [l.rstrip('\n') for l in inputFile]
linesIter = iter(lines)
nCases = int(linesIter.next())


# Process each case
for iCase in range(1,nCases+1):
    printe("\nProcessing case " + str(iCase))

    # Solve problem
    vals = linesIter.next().split(" ")
    nStalls = int(vals[0])
    nPeople = int(vals[1])

    intervals = defaultdict(lambda : 0)

    intervals[nStalls] = 1

    while True:

        # Check for completion
        if nPeople <= 0:
            break

        # Find biggest
        maxSize = 0
        for (iSize, iCount) in intervals.iteritems():
            if iSize > maxSize:
                maxSize = iSize
                intSize = iSize
                intCount = iCount
        del intervals[maxSize]
        
        printe(len(intervals))

        nPeople -= intCount

        # Add new intervals
        if intSize % 2 == 0:

            intervals[intSize / 2 - 1] += intCount
            intervals[intSize / 2] += intCount
            smaller = intSize / 2 - 1
            larger = intSize / 2

        else:

            intervals[intSize / 2] += 2*intCount
            smaller = intSize / 2
            larger = intSize / 2


    print("Case #{}: {} {}".format(iCase, larger, smaller))

