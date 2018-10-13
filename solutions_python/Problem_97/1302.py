#!/usr/bin/python
import sys

infile = open(sys.argv[1], 'r')

numCases = int(infile.readline())

for k in range(numCases):
    line = infile.readline().split()
    A = int(line[0])
    B = int(line[1])
    numDigits = len(line[0])
    pairDict = {}
    if numDigits != 1:
        for i in range(A,B+1):
            rotatedNumber = i
            for j in range(numDigits-1):
                blob = rotatedNumber % 10**(numDigits-1)
                rotatedNumber = int((rotatedNumber - blob) / 10**(numDigits-1) +
                        blob*10)
                if (rotatedNumber > i and rotatedNumber <= B and
                        (i,rotatedNumber) not in pairDict):
                    pairDict[(i,rotatedNumber)] = 1
    print "Case #%d: %d" % (k+1, len(pairDict))

