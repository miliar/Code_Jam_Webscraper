#!/usr/bin/env python
# encoding: utf-8
"""
aCodeJam-Problem1.py

Created by Ganesh Venkatesh on 2010-05-22.
Copyright (c) 2010 __MyCompanyName__. All rights reserved.
"""

import sys
import getopt
import re
import commands

def insertDirectory(currStructure, dirArray):
    if((len(dirArray)<1) or (dirArray[0] == "")):
        return
    currDir = dirArray[0]
    if(currDir in currStructure):
        insertDirectory(currStructure[currDir], dirArray[1:])
    else:
        newSubDir = {}
        currStructure[currDir] = newSubDir
        insertDirectory(newSubDir, dirArray[1:])

def mkdirCount(currDirStructure, subDirList):
    if(len(subDirList)<1):
        return(0)
    currDir = subDirList[0]
    if(currDir in currDirStructure):
        subDirStructure = currDirStructure[currDir]
        return(mkdirCount(subDirStructure, subDirList[1:]))
    else:
        return(len(subDirList))

def findReqMkdir(caseId, inp):
    firstLine = inp.readline()
    firstLine = firstLine.strip()
    tempArr = re.split("\s+", firstLine)
    dirCount = int(tempArr[0])
    newDirCount = int(tempArr[1])
    currDirStructure = {}
    for iter in range(dirCount):
        currline = inp.readline()
        currline = currline.strip()
        tempArr = re.split("/",currline)
        for index, tempDir in enumerate(tempArr):
            if(tempDir == ""):
                continue
            newSubDir = {}
            if(currDirStructure.has_key(tempDir)):
                newSubDir = currDirStructure[tempDir]
            else:
                currDirStructure[tempDir] = newSubDir
            insertDirectory(newSubDir, tempArr[index+1:])
            break
    #end while
    totalMkdirCount = 0
    for iter in range(newDirCount):
        currline = inp.readline()
        currline = currline.strip()
        tempArr = re.split("/", currline)
        subDirList = []
        for subDir in tempArr:
            if(subDir != ""):
                subDirList.append(subDir)
        #end for
        count = mkdirCount(currDirStructure, subDirList)
        totalMkdirCount += count
        insertDirectory(currDirStructure, subDirList)
    #end for
    print "Case #"+str(caseId)+": "+str(totalMkdirCount)
    

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
        findReqMkdir(currCaseCount, inp)
        currCaseCount += 1


if __name__ == "__main__":
	main()
