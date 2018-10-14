#!/usr/bin/python
import sys
from math import *

def nextLine():
    line = sys.stdin.readline()
    line = line.replace("\n", "")
    return line

def findBest(entrySets, maxDineTime):
    if len(entrySets) == 0:
        return 0 
#    print (("entrySets:%s:maxDinerTime:%s") %(entrySets, maxDineTime))
    currentEntrySet = entrySets[0]
    nextEntrySets = entrySets[1:]
    currentAttemptMaxDineTime = sys.maxint
    for currentEntry in currentEntrySet:
        attemptMaxDineTime = max(maxDineTime, currentEntry[0])
        attemptDineTime = 0
        if attemptMaxDineTime > maxDineTime:
            attemptDineTime += attemptMaxDineTime - maxDineTime
        attemptDineTime += currentEntry[1]
        attemptDineTime += findBest(nextEntrySets, attemptMaxDineTime)
        currentAttemptMaxDineTime = min(currentAttemptMaxDineTime, attemptDineTime)
        #print (("currentEntry:%s:currentAttemptMaxDineTime:%s:attemptMaxDineTime:%s:attemptDineTime:%s") %(currentEntry, currentAttemptMaxDineTime, attemptMaxDineTime, attemptDineTime))
    return currentAttemptMaxDineTime

line = nextLine()
testCases = int(line)
for i in range(0,testCases):
    nextLine()
    initialState = nextLine()
    dinerState = [int(x) for x in initialState.split(" ")]
    possibleSet = []
    entrySets = []
    for entry in dinerState:
        entrySet = [[entry,0]]
        sqrtEntry = int(ceil(sqrt(entry)))
        sqrtEntry = max(1, sqrtEntry)
        for x in range(1, sqrtEntry +1):
            entrySet.append([int(ceil(entry/(x+1.0))), x])
        entrySets.append(entrySet)
    currentBest = findBest(entrySets, 0)
    print (("Case #%s: %s") %(i+1,currentBest))
