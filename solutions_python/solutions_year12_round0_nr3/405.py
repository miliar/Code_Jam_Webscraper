# -*- coding: utf-8 -*-
"""
Created on Sat Apr 14 05:04:38 2012

@author: Elite
"""

import sets;
        
debug = False;

def leftDecShift(num, shift):
    return num*(10**shift);
    
def rightDecShift(num, shift):
    ret = num;
    for i in range(shift):
        ret /= 10;
    return ret;

def generateRecycledNumbers(num):
    recycled = set();
    cycles = len(str(num));    
    for i in range(1, cycles):
        newNum = num%(10**i);
        newNum = leftDecShift(newNum,cycles-i) + rightDecShift(num,i);
        recycled.add(newNum);
        
    return recycled;

inFile = open("C-large.in");
outFile = open("C-large.out", "w");

numTests = int(inFile.readline());

for testNum in range(numTests):
    testCase = inFile.readline().rstrip("\n");
    params = testCase.split();
    
    valMin = int(params[0]);
    valMax = int(params[1]);
    numPairs = 0;
    
    for i in range(valMin, valMax+1):
        recycled = generateRecycledNumbers(i);
        if debug: print "Found cycled pairs for <"+str(i)+">: " + str(recycled);
        for num in recycled:
            if (num > i and num <= valMax):
                numPairs += 1;
                                        
    if debug: print testCase;
    outFile.write("Case #" + str(testNum+1) + ": " + str(numPairs) + "\n");

inFile.close();
outFile.close();