# CodeJam 2015 Problem B
# Nicholas Sharp - nsharp33@gmail.com

import fileinput

from math import *

nCases = int(raw_input())

for iCase in range(nCases):

    nDiners = int(raw_input())
    dVals = map(int,raw_input().split(" "))

    #print("dVals = " + str(dVals))
    
    maxVal = max(dVals)

    bestScore = maxVal

    for hMax in range(1,maxVal+1):

        spreadIters = 0

        for val in dVals:

            if(val > hMax):

                toSpread = val - hMax
                thisIters = (toSpread+hMax-1) / hMax
                spreadIters += thisIters

        thisScore = hMax + spreadIters
        bestScore = min((thisScore, bestScore))

    print("Case #%d: %d"%(iCase+1, bestScore))
