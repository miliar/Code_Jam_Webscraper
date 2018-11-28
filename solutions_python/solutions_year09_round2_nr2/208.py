#!/usr/bin/python
import sys
import itertools

def getNumberList(numberString):
    numberList = []
    for c in numberString:
        i = int(c)
        numberList.append(i)
    return numberList

def findAllPermutations(numberList):
    allPermTuples = list( itertools.permutations(numberList, len(numberList)) )

    allPermInts = []
    for permTuple in allPermTuples:
        asString = ""

        for i in permTuple:
            asString = asString + str(i)

        if asString[0] == "0":
            continue

        asInt = int(asString)
        allPermInts.append(asInt)

    allPermInts.sort()

    allPermIntsNoDup = []
    for i in range(len(allPermInts)):
        if i == 0:
            allPermIntsNoDup.append(allPermInts[i])
        else:
            if allPermInts[i - 1] != allPermInts[i]:
                allPermIntsNoDup.append(allPermInts[i])

    return allPermIntsNoDup

def findNextNumber(numberList):
    number = int( "".join(str(i) for i in numberList) )
    allPermutations = findAllPermutations(numberList)

    i = 0
    for i in range(len(allPermutations)):
        if allPermutations[i] == number:
            break

    if (i + 1) >= len(allPermutations):
        allPermutations = findAllPermutations(numberList + [0])
        return allPermutations[0]
    else:
        return allPermutations[i + 1]

filename = sys.argv[1]
file = open(filename, 'r')

numCases = int(file.readline())
for i in range(numCases):
    numberString = file.readline().strip()
    numberList = getNumberList(numberString)
    nextNumber = findNextNumber(numberList)
    print "Case #" + str(i + 1) + ":", nextNumber

file.close()
