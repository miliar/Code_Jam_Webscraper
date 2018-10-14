#!/usr/bin/env python

import sys

def runtest(inf, testno):
    result = 0
    line = inf.readline().split()
    n = int(line[0])
    orangepos = 1
    bluepos = 1
    lastcolor = '-'
    lasttime = 1
    distance = 0
    for i in xrange(n):
        color = line[2*i+1]
        position = int(line[2*i+2])
        # Find the distance traveled
        if color == 'B':
            distance = abs(bluepos-position)
            bluepos = position
        else: 
            distance = abs(orangepos-position)
            orangepos = position
        # Find the amount the time can overlap other color
        time = 1 + distance
        overlap = 0
        if lastcolor == color:
            lasttime += time
        else:
            if lastcolor != '-':
                overlap = lasttime
                if overlap > distance:
                    overlap = distance
            lasttime = time-overlap

        result += time - overlap
        # Set values for next time
        lastcolor = color
    print 'Case #' + str(testno+1) + ': ' + str(result)

inf = open(sys.argv[1], 'r')
numtests = int(inf.readline().strip())
for i in xrange(numtests):
    runtest(inf, i)
inf.close()
