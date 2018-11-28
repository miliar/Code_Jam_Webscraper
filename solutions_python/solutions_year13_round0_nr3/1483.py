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

inputFile = "C-small-attempt0.in"

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
        
        case = formatCaseInput(caseInput)
        output = getCaseOutput(case)
        
        print "Case #" + str(i+1) + ": " + output
        outFile.write("Case #" + str(i+1) + ": " + output + '\n')
        
    outFile.close()
        

def formatCaseInput(caseInput):
    line = caseInput[0]

    index = line.index(" ")
    val1 = long(line[:index].strip())
    val2 = long(line[index+1:].strip())
    
    case = [val1, val2]
    return case

def findNextPalindrome(i):
    i += 1
    while (isPalindrome(i) == False):
        i += 1
    return i

def findNextPalindromeNaive(i):
    i += 1
    while (isPalindrome(i) == False):
        i += 1
    return i 

# thanks http://stackoverflow.com/questions/2489435/how-could-i-check-if-a-number-is-a-perfect-square
def isPerfectSquare(integer):
    root = long(math.sqrt(integer))

    if long(root + 0.5) ** 2 == integer:
        return True
    else:
        return False

def isPalindrome(i):
    # check if this is an int the roundabout way
    if isPerfectSquare(i*i) == False:
        return False
    
    numStr = str(long(i))

    numStrRev = numStr[::-1]
    if (numStr == numStrRev):
        return True
    else:
        return False
    
def getCaseOutput(case):
    lower = case[0]
    upper = case[1]

    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    output = 0
    
    i = lower
    while (i <= upper):
        # check if it's valid
        sqrt = math.sqrt(i)
        if isPalindrome(sqrt):
            #print str(i) + "!!"
            output += 1
        
        i = findNextPalindrome(i)
        #print i
    
    return str(output)
            
runSolution(inputFile)
