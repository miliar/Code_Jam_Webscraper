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
import operator
import math

inputFile = "B-large.in"

outputFile = "output.txt"
outFile = open(outputFile, mode='w')

def runSolution(inFile):
    
    lines = open(inFile, mode='r').readlines()
    ln = 0 #ln = line number
    
    cases = int(lines[ln])
    ln += 1
    for i in range(0, cases):
        caseInput = []

        line = lines[ln]
        ln += 1
        index = line.index(" ")
        val1 = long(line[:index].strip())
        val2 = long(line[index+1:].strip())
        
        for j in range(0, val1):
            caseInput.append(lines[ln].strip())
            ln += 1
        
        case = formatCaseInput(caseInput, val2)
        output = getCaseOutput(case)
        
        print "Case #" + str(i+1) + ": " + output
        outFile.write("Case #" + str(i+1) + ": " + output + '\n')
        
    outFile.close()
        

def formatCaseInput(caseInput, val2):
    case = [] 
    for i in range(0, len(caseInput)):
        row = []
        line = caseInput[i]
        for i in range(0, val2):
            if (i != val2 - 1):
                index = line.index(" ")
                val1 = int(line[:index].strip())
                line = line[index+1:]
                row.append(val1)
            else:
                row.append(int(line))
        case.append(row)

    return case

def getCaseOutput(case):
    for row in range(0,len(case)):
        for col in range(0,len(case[row])):
            val = case[row][col]

            rowValid = True
            #check row for validity
            for col2 in range(0, len(case[row])):
                if (case[row][col2] > val):
                    rowValid = False

            colValid = True
            #check col for validity
            for row2 in range(0, len(case)):
                if (case[row2][col] > val):
                    colValid = False

            if not rowValid and not colValid:
                return "NO"
    
    return "YES"
            
runSolution(inputFile)
