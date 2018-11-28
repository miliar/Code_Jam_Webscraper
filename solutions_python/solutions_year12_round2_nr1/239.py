#!/bin/env python

from __future__ import print_function



def writeCase(theFile, caseNumber, answer):
    theLine = "Case #%d: %s"%(caseNumber, answer)
    theFile.write(theLine + "\n")
    return

def solveCase(theFile): # Don't forget: readline includes the \n
    theLine = [int(x) for x in theFile.readline().strip().split()]
    totalConts = theLine[0]
    scores = theLine[1:totalConts+1]
    totalScore = sum(scores)
    doubleScore = 2.0*totalScore
    pointsNeeded = doubleScore/totalConts
    altered = False
    for score in scores:
        if score > pointsNeeded:
            totalConts -= 1
            doubleScore -= score
            altered = True
    if altered:
        pointsNeeded = doubleScore/totalConts
    result = []
    for score in scores:
        neededPercentage = 100*(pointsNeeded-score)/totalScore
        if neededPercentage < 0.0:
            neededPercentage = 0.0
        result += [neededPercentage]
    return ' '.join([str(x) for x in result])

        
                


def main(fileName):
    f = open(fileName, "U")
    g = open(fileName+".out", "w")
    cases = int(f.readline())
    for x in xrange(cases):
        writeCase(g, x+1, solveCase(f))
    f.close()
    g.close()
    return

if __name__ == "__main__":
    from sys import argv
    main(argv[1])
