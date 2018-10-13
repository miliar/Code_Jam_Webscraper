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

inputFile = "A-large.in"

outputFile = "output.txt"
outFile = open(outputFile, mode='w')

def runSolution(inFile):
    
    lines = open(inFile, mode='r').readlines()
    ln = 0 #ln = line number
    
    cases = int(lines[ln])
    ln += 1
    for i in range(0, cases):
        caseInput = []
        linesInCase = 4
        
        for j in range(0, linesInCase):
            caseInput.append(lines[ln].strip())
            ln += 1
        ln += 1 #skip blank line in input
        
        case = formatCaseInput(caseInput)
        output = getCaseOutput(case)
        
        #print "Case #" + str(i+1) + ": " + output
        outFile.write("Case #" + str(i+1) + ": " + output + '\n')
        
    outFile.close()
        

def formatCaseInput(caseInput):
    case = [['','','',''], ['','','',''], ['','','',''], ['','','','']]
    for lineNum in range(0, len(caseInput)):
        line = caseInput[lineNum]
        for j in range(0, len(line)):
            case[lineNum][j] = line[j]
    return case

def getCaseOutput(case):
    playerList = ['X', 'O']
    wild = 'T'
    for i in range(0, len(playerList)):
        player = playerList[i]

        # check horizontals
        for row in range(0,4):
            win = True
            for col in range(0,4):
                if case[row][col] != player and case[row][col] != wild:
                    win = False
            if win:
                return player + " won"

        # check verticals
        for col in range(0,4):
            win = True
            for row in range(0,4):
                if case[row][col] != player and case[row][col] != wild:
                    win = False
            if win:
                return player + " won"

        # check diagonal 1
        win = True
        for row in range(0,4):
            if case[row][row] != player and case[row][row] != wild:
                win = False
        if win:
            return player + " won"

        # check diagonal 2
        win = True
        for row in range(0,4):
            if case[3-row][row] != player and case[3-row][row] != wild:
                win = False
        if win:
            return player + " won"

    # if no one won
    # check if board is full
    for row in range(0,4):
        for col in range(0,4):
            if case[row][col] == '.':
                return "Game has not completed"

    return "Draw"
            
runSolution(inputFile)
