# -*- coding: utf-8 -*-
"""
Created on Sat Apr 14 00:41:30 2012

@author: Elite
"""

import math;

def bestUnsurprisingScore(scoreTripletTotal):
    if scoreTripletTotal%3 == 0:
        return scoreTripletTotal/3;
    else:
        return scoreTripletTotal/3 + 1;
        
def bestSurprisingScore(scoreTripletTotal):
    if scoreTripletTotal == 0:
        return scoreTripletTotal;
        
    scoreMod = scoreTripletTotal%3;
    if scoreMod == 0:
        return min(scoreTripletTotal/3 + 1, 10);
    else:
        return min(scoreTripletTotal/3 + scoreMod, 10);

debug = False;

inFile = open("B-large.in");
outFile = open("B-large.out", "w");

numTests = int(inFile.readline());

for testNum in range(numTests):
    testCase = inFile.readline().rstrip("\n");
    params = testCase.split();
    
    numValues = int(params[0]);
    numSurprises = int(params[1]);
    threshold = int(params[2]);
    surprisingPassedThreshold = [];
    unsurprisingPassedThreshold = [];
    
    for i in range(3, 3+numValues):
        if (bestSurprisingScore(int(params[i])) >= threshold):
            surprisingPassedThreshold.append(1);
        else:
            surprisingPassedThreshold.append(0);
            
        if (bestUnsurprisingScore(int(params[i])) >= threshold):
            unsurprisingPassedThreshold.append(1);
        else:
            unsurprisingPassedThreshold.append(0);
            
    if debug: print "Surprising: " + str(surprisingPassedThreshold);
    if debug: print "Unsurprising: " + str(unsurprisingPassedThreshold);
    
    maxPassed = sum(unsurprisingPassedThreshold);
    idx = 0;    
    while (idx < numValues and numSurprises > 0):
        if unsurprisingPassedThreshold[idx] > 0:
            idx += 1;
            continue;
        if surprisingPassedThreshold[idx] > 0:
            maxPassed += 1;
            numSurprises -= 1;        
        idx += 1;
                            
    if debug: print testCase;
    outFile.write("Case #" + str(testNum+1) + ": " + str(maxPassed) + "\n");

outFile.close();