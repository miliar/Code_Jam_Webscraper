#!/usr/bin/env python
# encoding: utf-8
"""
untitled.py

Created by Ganesh Venkatesh on 2010-05-22.
Copyright (c) 2010 __MyCompanyName__. All rights reserved.
"""

import sys
import os
import commands
import re

def findReachableChicSet(velocityArr, startingPointArr, distance, timeAvai):
    reachableChicSet = set()
    for index in range(len(velocityArr)):
        timeReq = (distance - int(startingPointArr[index]))/float(velocityArr[index])
        if(timeReq <= timeAvai):
            reachableChicSet.add(index)
    #end for
    return(reachableChicSet)

def buildObstructionMap(reachableChicSet, startingPointArr):
    chicObstructionMap = {}
    for index in range(len(startingPointArr)):
        if(index not in reachableChicSet):
            continue        
        chicObstructionMap[index] = 0
    #end for
    for index in range(len(startingPointArr)):
        if(index not in reachableChicSet):
            continue
        for index2 in range(len(startingPointArr)):
            if(index == index2):
                continue
            if(index2 in reachableChicSet):
                continue
            if(int(startingPointArr[index]) < int(startingPointArr[index2])):
                chicObstructionMap[index] += 1
    #end for
    return(chicObstructionMap)

def findChicSwaps(caseId, inp):
    firstLine = inp.readline()
    firstLine = firstLine.strip()
    tempArr = re.split("\s+", firstLine)
    chicCount = int(tempArr[0])
    chicGoal = int(tempArr[1])
    distance = int(tempArr[2])
    timeAvai = int(tempArr[3])
    chicStartingPointStr = inp.readline()
    chicVelocityStr = inp.readline()
    chicStartingPointStr = chicStartingPointStr.strip()
    chicVelocityStr = chicVelocityStr.strip()
    startingPointArr = re.split("\s+", chicStartingPointStr)
    velocityArr = re.split("\s+", chicVelocityStr)
    assert len(startingPointArr) == len(velocityArr)
    reachableChicSet = findReachableChicSet(velocityArr, startingPointArr, distance, timeAvai)
    if(len(reachableChicSet)<chicGoal):
        print "Case #"+str(caseId)+": IMPOSSIBLE"
        return
    chicObstructionMap = buildObstructionMap(reachableChicSet, startingPointArr)
    valueList = chicObstructionMap.values()
    valueList.sort()
    totalSwaps = 0
    for index in range(chicGoal):
        totalSwaps += valueList[index]
    print "Case #"+str(caseId)+": "+str(totalSwaps)
    

def main():
    if(len(sys.argv)<2):
        usage()
        sys.exit()
    inputFile = sys.argv[1]
    try:
        inp = open(inputFile, "r")
    except IOError, err:
        print "Cannot open inputfile:"+inputFile
        sys.exit(1)
    firstLine = inp.readline()
    firstLine = firstLine.strip()
    nVal = int(firstLine)
    currCaseCount = 1
    while(currCaseCount <= nVal):
        findChicSwaps(currCaseCount, inp)
        currCaseCount += 1
    


if __name__ == '__main__':
    main()

