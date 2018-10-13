#!/bin/env python

from __future__ import print_function



def writeCase(theFile, caseNumber, answer):
    theFile.write("Case #%d: %s\n"%(caseNumber, answer))
    return
    

def solveCase(theFile): # Don't forget: readline includes the \n
    numClasses = int(theFile.readline().strip())
    inheritances = []
    for x in xrange(numClasses):
        inheritances += [[int(x) for x in theFile.readline().strip().split()][1:]]
    print(len(inheritances))
    for inheritanceList in inheritances:
        allParents = inheritanceList[:]
        for parent in allParents:
            parentParents = inheritances[parent-1]
            for parentParent in parentParents:
                if parentParent in allParents:
                    return "Yes"
                else:
                    allParents += [parentParent]
    return "No"


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
