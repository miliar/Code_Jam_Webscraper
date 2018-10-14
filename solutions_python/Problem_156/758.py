# -*- coding: utf-8 -*-

# just copy a whole bunch of these just in case
import time
import sys, traceback, ast
import fileinput
import os
import re
import httplib
import codecs
import HTMLParser
import math
import operator

inputFile = "B-small-attempt1.in"

outputFile = "output.txt"
outFile = open(outputFile, mode='w')

def runSolution(inFile):
    
    lines = open(inFile, mode='r').readlines()
    ln = 0 #ln = line number
    
    cases = int(lines[ln])
    ln += 1
    for i in range(0, cases):
        caseInput = []
        linesInCase = 2
        
        for j in range(0, linesInCase):
            caseInput.append(lines[ln].strip())
            ln += 1
        #ln += 1 #skip blank line in input
        
        case = formatCaseInput(caseInput)
        output = getCaseOutput(case)
        
        print "Case #" + str(i+1) + ": " + output
        outFile.write("Case #" + str(i+1) + ": " + output + '\n')
        
    outFile.close()
        

def formatCaseInput(caseInput):
    line = caseInput[0]
    splitln = line.split(" ")
    people = int(splitln[0])
    pancakeArray = caseInput[1].split(" ")

    newPancakeArray = [];
    for item in pancakeArray:
        newPancakeArray.append(int(item));

    case = []
    case.append(newPancakeArray)
    return case

def getCaseOutput(case):
    print case;
    val = doCase(case[0])
    return str(val)

solutionTable = {};

def getHash(pancakes):
    theString = "";
    for i in pancakes:
        theString = theString + "." + str(i); #TODO: lol
    return theString;

def doCase(pancakes):
    # filter out 0
    newPancakes = [];
    everyoneEatsOne = [];
    for person in pancakes:
        if person != 0:
            newPancakes.append(person);
            everyoneEatsOne.append(person - 1);
    pancakes = newPancakes;

    # sort by highest
    pancakes = sorted(pancakes);
    pancakes.reverse();

    if len(pancakes) == 0: # we done
        return 0;

    if getHash(pancakes) in solutionTable:
        return solutionTable[getHash(pancakes)];

    # keep thinging
    doNothing = 1 + doCase(everyoneEatsOne);

    highestPancake = pancakes[0];
    bestSwitchTime = 999999;
    for i in range(2, highestPancake): # TODO: cut in half 
        dupePancakes = [];
        for person in pancakes:
            dupePancakes.append(person);
        dupePancakes[0] -= i; #do the switch
        dupePancakes.append(i); 
        thisTime = 1 + doCase(dupePancakes);
        if thisTime < bestSwitchTime:
            bestSwitchTime = thisTime;

    solutionTable[getHash(pancakes)] = min(doNothing, bestSwitchTime);
    return min(doNothing, bestSwitchTime);
    
runSolution(inputFile)
