#!/usr/bin/env python
from __future__ import with_statement
import sys

def genCombinations(items, n):
    if n==0: yield []
    else:
        for i in xrange(len(items)):
            for cc in genCombinations(items[i+1:],n-1):
                yield [items[i]]+cc


def readFile(inFileName):
    cases = []
    inFile = file(inFileName)
    numCases = int(inFile.readline().strip())
    for case in range(1,numCases+1):
        #Case-specific
        (n, A,B,C,D,x0,y0, M) = map(lambda x: int(x), inFile.readline().strip().split(' '))
        treepoints = []
       
        X= x0
        Y= y0
        treepoints.append({"x": X, "y":Y})
        for i in range(1,n):
            X = (A * X + B) % M
            Y = (C * Y + D) % M
            
            treepoints.append({"x": X, "y":Y})
        cases.append({"points": treepoints})
    return cases


cases = readFile(sys.argv[1])
caseNum = 0
for case in cases:
    caseNum += 1
    triCount = 0
    for triangle in genCombinations(case["points"], 3):
        v1 = triangle[0]
        v2 = triangle[1]
        v3 = triangle[2]
        centreX = (v1["x"]+v2["x"]+v3["x"])/3.0
        centreY = (v1["y"]+v2["y"]+v3["y"])/3.0
        if(centreX == int(centreX) and centreY == int(centreY)):
            triCount += 1
    print "Case #"+str(caseNum) + ": " + str(triCount)
    