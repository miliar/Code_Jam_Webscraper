#!/usr/bin/env python3
from sys import argv

    
def processCase(inFile, caseNum):
    params = inFile.readline().strip().split()
    maxNum = int(params[0]) #why is this here... isn't it simply the length of the audience string?
    audience = params[1]
    runningTotal = 0
    friends = 0
    for sFactor in range(0, maxNum + 1):
        if runningTotal + friends < sFactor:
            friends += sFactor - (runningTotal + friends)
        runningTotal += int(audience[sFactor])
    print("Case #%s: %d" % (caseNum, friends))



def processFile(filename):
    infile = open(filename, "r")

    caseCount = int(infile.readline())
    i = 0
    while(i < caseCount):
        i += 1
        processCase(infile, i)


if __name__ == "__main__":
    if len(argv) < 2:
        exit()

    processFile(argv[1])

