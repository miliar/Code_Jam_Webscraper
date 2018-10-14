#!/usr/local/bin/python3.0

import sys

def rollerCoasterEarnings(rides, capacity, groups):
    totalRiders = sum(groups)
    if capacity >= totalRiders:
        # Everyone can ride on every time
        return rides * totalRiders
    
    groupCount = len(groups)
    
    ridesSoFar = 0
    earningsSoFar = 0
    nextGroup = 0
    previousStates = [ None ] * groupCount
    
    while ridesSoFar < rides:
        if previousStates:
            if previousStates[nextGroup] is None:
                previousStates[nextGroup] = (ridesSoFar, earningsSoFar)
            else:
                # We're back to the same queue of riders as a previous time.
                # That means that from this time on, the same pattern of riders
                # will repeat.
                (ridesLastTime, earningsLastTime) = previousStates[nextGroup]
                ridesInCycle = ridesSoFar - ridesLastTime
                earningsInCycle = earningsSoFar - earningsLastTime
                cyclesLeft = (rides - ridesSoFar) // ridesInCycle
                
                ridesSoFar += cyclesLeft * ridesInCycle
                earningsSoFar += cyclesLeft * earningsInCycle
                
                if ridesSoFar == rides:
                    break
                
                # No longer check previous states
                previousStates = None
        
        ridersOnThisRide = 0
        while ridersOnThisRide + groups[nextGroup] <= capacity:
            ridersOnThisRide += groups[nextGroup]
            nextGroup += 1
            if nextGroup == groupCount:
                nextGroup = 0
        
        earningsSoFar += ridersOnThisRide
        ridesSoFar += 1
    
    return earningsSoFar


def assertFormat(pred):
    if not pred:
        sys.exit('Illegal input')

firstLine = next(sys.stdin)
numbers = tuple( int(s) for s in firstLine.split() )
assertFormat(len(numbers) == 1)
T = numbers[0]

for caseNumber in range(1, T+1):
    line = next(sys.stdin)
    numbers = tuple( int(s) for s in line.split() )
    assertFormat(len(numbers) == 3)
    R,k,N = numbers
    assertFormat(R > 0)
    assertFormat(k > 0)
    assertFormat(N > 0)
    
    line = next(sys.stdin)
    gArray = [ int(s) for s in line.split() ]
    assertFormat(len(gArray) == N)
    assertFormat(all( g > 0 for g in gArray))
    assertFormat(all( g <= k for g in gArray))
    
    result = rollerCoasterEarnings(R, k, gArray)
    
    print( 'Case #{0}: {1}'.format(caseNumber, result) )

