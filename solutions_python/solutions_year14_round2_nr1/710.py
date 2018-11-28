#!/usr/bin/env python

import math

def remRepeated(s1):
    res = []
    sizeS1 = len(s1)
    for i in range(sizeS1):
        if i+1 < sizeS1:
            if s1[i] != s1[i+1]:
                res += [s1[i]]
        else:
            res += [s1[i]]

    return "".join(res)

def findNeededChangesForPosition(allChars):
    #print("findNeededChangesForPosition", allChars)
    lengths = [len(i) for i in allChars]
    media = int(sum(lengths)/len(lengths))
    #media = math.ceil(media)

    neededChanges = 0

    for c in allChars:
        neededChanges += abs(len(c)-media)
    return neededChanges


def getSubStrings(allStrings):
    res = []

    for s1 in allStrings:
        import itertools
        res += [[''.join(value) for key,value in itertools.groupby(s1)]]

    return res

def countPositions(allStrings):
    return len(remRepeated(allStrings[0]))

def calculate(allStrings):
    #is possible?
    for s1 in allStrings:
        for s2 in allStrings:
            if set(s1) != set(s2):
                return "Fegla Won"

    #check order
    for s1 in allStrings:
        for s2 in allStrings:
            if remRepeated(s1) != remRepeated(s2):
                return "Fegla Won"

    #it is possible
    #are they all equal?
    allEqual = True
    for s1 in allStrings:
        for s2 in allStrings:
            if s1 != s2:
                allEqual = False
                break
        if not allEqual:
            break

    if allEqual:
        return "0"


    allSubStrings = getSubStrings(allStrings)
    totalPositions = countPositions(allStrings)
    #print(len(allSubStrings[0]), len(allStrings))
    counter = 0

    for pos in range(len(allSubStrings[0])):
        actualRow = []
        for subPos in range(len(allStrings)):
            #print(allSubStrings[pos])
            actualRow += [allSubStrings[subPos][pos]]

        counter = counter + findNeededChangesForPosition(actualRow)

    return str(counter)

T = int(input())

for t in range(1, T+1):
    print("Case #"+str(t)+": ", end="")
    res = "Fegla Won"

    N = int(input())

    allStrings = []
    for n in range(N):
        allStrings += [input()]

    res = calculate(allStrings)
    
    print(res)