#!/usr/bin/python

import sys, math

# Figures if a thang is a palindrome. 
def isPal(num):
    x = str(num)
    if x == x[::-1]:
        return True
    return False

def doInterval(start, end, caseNum):
    outStr = 'Case #{}: '.format(caseNum)
    realStart = int(math.sqrt(start))
    if realStart * realStart < start:
        realStart += 1

    realEnd = int(math.sqrt(end))
    counter = 0
    for num in range(realStart, realEnd + 1):
        if isPal(num):
            if isPal(num * num):
                counter += 1
    print outStr + str(counter)

fName = sys.argv[1]
ff = open(fName)
allLines = ff.readlines()
numCases = int(allLines[0])

for case in range(numCases):
    splitCase = allLines[case + 1].split()
    doInterval(int(splitCase[0]), int(splitCase[1]), case + 1)
