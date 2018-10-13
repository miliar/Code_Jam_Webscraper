#!/usr/bin/env python
from __future__ import with_statement
import sys
import array

def readFile(inFileName):
    cases = []
    inFile = file(inFileName)
    numCases = int(inFile.readline().strip())
    for case in range(1,numCases+1):
        #Case-specific
        (P, K, L) = map(lambda x: int(x), inFile.readline().strip().split(' '))
        freqs = map(lambda x: int(x), inFile.readline().strip().split(' '))
        cases.append({"P": P, "K": K, "L": L, "freqs" : freqs[0:L]})
    return cases


cases = readFile(sys.argv[1])
caseNum = 0
for case in cases:
    caseNum += 1
    lettersAvail = []
    lettersAvail = case["L"]
    maxPerKey = case["P"]
    numKeys = case["K"]
    freqs = case["freqs"]
    freqs.sort(reverse = True)
    currLetter = 0
    pressTotal = 0
    keyMap = dict()
    impossible = False
    for freq in freqs:
        keyAssigned = currLetter % numKeys
        if(keyMap.has_key(keyAssigned)):
            keyMap[keyAssigned] += 1
        else:
            keyMap[keyAssigned] = 1
        if keyMap[keyAssigned] > maxPerKey:
            impossible = True
            break
        pressesForOne = currLetter / numKeys + 1
        pressesForAll = pressesForOne * freq
        pressTotal += pressesForAll
        currLetter+= 1
    if not impossible: 
        print "Case #" + str(caseNum) + ": " + str(pressTotal)
    else:
        print "Case #" + str(caseNum) + ": Impossible"
