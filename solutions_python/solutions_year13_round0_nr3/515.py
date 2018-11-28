#!/usr/bin/python

from __future__ import print_function
import math

def getPal(aStr, numZeroes):
    if (numZeroes == 0):
        return aStr
    else:
        return long(aStr[:-numZeroes] + ''.join(reversed(aStr[:numZeroes])))

def isPal(aNum):
    theStr = str(aNum)
    theLen = len(theStr)
    for ind, char in enumerate(theStr[:(theLen/2)]):
        if (char != theStr[-ind-1]):
            return False
    return True

T = int(raw_input())

for x in xrange(T):
    theRange = raw_input().split()
    A = long(theRange[0])
    B = long(theRange[1])
    sqrtA = long(math.sqrt(A))
    if (sqrtA * sqrtA) < A:
        sqrtA += 1
    sqrtB = long(math.sqrt(B))
    zeroes = len(str(sqrtA))/2
    if (zeroes == 0):
        halfNumCtr = long(str(sqrtA))
    else:
        halfNumCtr = long(str(sqrtA)[:-zeroes])
    checkStr = str(halfNumCtr) + ('0' * zeroes)
    numMatches = 0

    #First check the first one:

    thePal = long(getPal(checkStr, zeroes))

    if thePal >= sqrtA:
        if isPal(thePal * thePal):
            numMatches += 1
    halfNumCtr += 1

    #Now check up until zeroes should be incremented:

    while (halfNumCtr < (10**(zeroes+1))):
        checkStr = str(halfNumCtr) + ('0' * zeroes)
        thePal = long(getPal(checkStr, zeroes))
        if thePal > sqrtB:
            break
        if isPal(thePal * thePal):
            numMatches += 1
        halfNumCtr += 1
            
    #Now check everything else

    while (True):
        zeroes += 1
        halfNumCtr = 10**(zeroes-1)
        breakout = False
        while (halfNumCtr < (10**(zeroes+1))):
            checkStr = str(halfNumCtr) + ('0' * zeroes)
            thePal = long(getPal(checkStr, zeroes))
            if thePal > sqrtB:
                breakout = True
                break
            if isPal(thePal * thePal):
                numMatches += 1
            halfNumCtr += 1
        if breakout:
            break

    print("Case #%d: %d"%(x+1, numMatches))
