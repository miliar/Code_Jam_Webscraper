# -*- coding: utf-8 -*-

# just copy a whole bunch of these just in case
import time
import sys, traceback, ast
import fileinput
import os
import re
import codecs
import math
import operator

inputFile = "A-small-attempt0.in"

outputFile = "output.txt"
outFile = open(outputFile, mode='w')

def runSolution(inFile):
    
    lines = open(inFile, mode='r').readlines()
    ln = 0 #ln = line number
    
    cases = int(lines[ln])
    ln += 1
    for i in range(0, cases):
        caseInput = []
        linesInCase = 10
        
        for j in range(0, linesInCase):
            caseInput.append(lines[ln].strip())
            ln += 1
        #ln += 1 #skip blank line in input
        
        case = formatCaseInput(caseInput)
        output = getCaseOutput(case)


        
        print ("Case #" + str(i+1) + ": " + output)
        outFile.write("Case #" + str(i+1) + ": " + output + '\n')
        
    outFile.close()
        

def formatCaseInput(caseInput):
    question1 = int(caseInput[0])
    board1 = []
    for i in range(1,5):
        line = caseInput[i]
        numbers = line.split(" ")
        for w in range(0,4):
            numbers[w] = int(numbers[w])
        board1.append(numbers)
        
    question2 = int(caseInput[5])
    board2 = []
    for j in range(6,10):
        line = caseInput[j]
        numbers = line.split(" ")
        for w in range(0,4):
            numbers[w] = int(numbers[w])
        board2.append(numbers)

    case = [question1, board1, question2, board2]
    return case

def getCaseOutput(case):
    output = doCase(case[0], case[1], case[2], case[3])
    if (output == -1):
        output = "Bad magician!"
    elif (output == -2):
        output = "Volunteer cheated!"
    return str(output)

def doCase(q1, b1, q2, b2):
    row1 = b1[q1-1]
    row2 = b2[q2-1]
    intersection = list(set(row1) & set(row2)) #cool
    if (len(intersection) == 0):
        return -2
    elif (len(intersection) == 1):
        return intersection[0]
    return -1;

runSolution(inputFile)
