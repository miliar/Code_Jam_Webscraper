#!/usr/bin/python
import os, sys

def testConfiguration(locations, speeds, barnLocation, targetTime, targetNumChicks):
    i = 0
    while i < targetNumChicks:
        # Test the ith one
        timeToBarn = float(barnLocation - locations[i]) / speeds[i]
        # Return the first one that fails
        if (timeToBarn > targetTime):
            # Can't make it.
            return i
        i += 1
    return -1

def chickCanMakeIt(location, speed, barnLocation, targetTime):
    return (float(barnLocation-location) / speed) <= targetTime

def doCase(locations, speeds, barnLocation, targetTime, targetNumChicks):
    # Put the front ones at beginning of array
    locations.reverse()
    speeds.reverse()
    numSwaps = 0

    # find which chicks can possibly make it.
    canMakeIt = [chickCanMakeIt(locations[i], speeds[i], barnLocation, targetTime) for i in range(len(locations))]
    numTrues = 0
    for i in range(len(canMakeIt)):
        if canMakeIt[i]:
            numTrues += 1
    if numTrues < targetNumChicks:
        return -1
    # Swap what we need.
    for i in range(targetNumChicks):
        if not canMakeIt[i]:
            # find the next good one and swap
            for j in range(i+1, len(canMakeIt)):
                if canMakeIt[j]:
                    # Swap
                    numSwaps += j-i
                    canMakeIt[i] = True
                    canMakeIt[j] = False
                    break
    return numSwaps


def blah():
    return
    while True:
        firstFail = testConfiguration(locations, speeds, barnLocation, targetTime, targetNumChicks)
        if firstFail == -1:
            return numSwaps
        # Fix the last one that isn't fast enough.
        for i in range(targetNumChicks-1, firstFail-1, -1):
            requiredSpeed = float(barnLocation - locations[i]) / targetTime
            if (speeds[i] < requiredSpeed):
                firstFail = i
                break
        #firstFail = targetNumChicks-1
        # See what speed firstFail needs.
        requiredSpeed = float(barnLocation - locations[firstFail]) / targetTime
        # See if there's a candidate.
        foundCandidate = False
        for i in range(firstFail+1, len(locations)):
            if not foundCandidate and (speeds[i] >= requiredSpeed):
                # Do the swaps.
                numSwaps += (i - firstFail)
                temp = speeds[i]
                for j in range(firstFail+1, i+1):
                    speeds[j] = speeds[j-1]
                speeds[firstFail] = temp
                #temp = speeds[i]
                #speeds[i] = speeds[firstFail]
                #speeds[firstFail] = temp
                foundCandidate = True
                break
        if not foundCandidate:
            # Can't be done
            return -1

def main(filename):
    fileLines = open(filename, 'r').readlines()
    index = 0
    numCases = int(fileLines[index][:-1])
    index += 1
    for caseNum in range(numCases):
        (n, k, b, t) = [int(x) for x in fileLines[index][:-1].split(' ')]
        index += 1
        initialLocations = [int(x) for x in fileLines[index][:-1].split(' ')]
        index += 1
        speeds = [int(x) for x in fileLines[index][:-1].split(' ')]
        index += 1
        answer = doCase(initialLocations, speeds, b, t, k)
        print "Case #%d: %s" % (caseNum + 1, 'IMPOSSIBLE' if answer == -1 else answer)

if __name__ == '__main__':
    main(sys.argv[1])
