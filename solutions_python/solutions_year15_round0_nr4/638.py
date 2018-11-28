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

inputFile = "D-small-attempt1.in"

outputFile = "output.txt"
outFile = open(outputFile, mode='w')

def runSolution(inFile):
    
    lines = open(inFile, mode='r').readlines()
    ln = 0 #ln = line number
    
    cases = int(lines[ln])
    ln += 1
    for i in range(0, cases):
        caseInput = []
        linesInCase = 1
        
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
    x = int(splitln[0])
    r = int(splitln[1])
    c = int(splitln[2])

    case = []
    case.append(x)
    case.append(r)
    case.append(c)
    #print case
    return case

def getCaseOutput(case):
    val = doCase(case)
    return str(val)

def doCase(stuff):
    # we lazy so let's special case this
    # richard means player cannot win
    x = stuff[0]
    r = stuff[1]
    c = stuff[2]
    #print str(x)
    if x == 1:
        #print str(r) + " " + str(c)
        return "GABRIEL"
    if x == 2:
        #print str(r) + " " + str(c)
        if (r * c) % 2 == 1:
            return "RICHARD"
        return "GABRIEL"
    if x == 3:
        #print str(r) + " " + str(c)
        if (r < 3 and c < 3):
            return "RICHARD"
        if (r > c):
            c2 = c;
            c = r;
            r = c2 #swap em
        if c == 4:
            if r == 1 or r == 2 or r == 4:
                return "RICHARD" 
        if c == 3:
            if r == 1:
                return "RICHARD"
        return "GABRIEL"
    if x == 4:
        if (r < 4 and c < 4):
            print str(r) + " " + str(c)
            return "RICHARD";
        # logic time
        if (r > c):
            c2 = c;
            c = r;
            r = c2 #swap em
        print str(r) + " " + str(c)
        if r == 1:
            return "RICHARD" #square
        if r == 2:
            return "RICHARD"
        if r == 3:
            return "GABRIEL"
        if r == 4:
            return "GABRIEL"
        return "???"
    return "???"
    
runSolution(inputFile)
