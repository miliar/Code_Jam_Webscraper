# aSpeakingInToungues.py
# https://code.google.com/codejam/contest/1460488/dashboard
# by John Shaffstall aka double051
#!/usr/bin/env python

import sys
import io

outputFile = open('A-small-attempt1.out', 'r+')

def printSolution(caseNumber, solution):
    outputFile.write('Case #%d: %s\n'%(caseNumber, solution))

charMap = {' ': ' ', 'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v',
           'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g',
           'o': 'k', 'n': 'b', 'q': 'z', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j',
           't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'z': 'q'}

with open('A-small-attempt1.in') as inputFile:
    inputCount = int(inputFile.readline())
    caseNumber = 1
    inputLine = inputFile.readline().rstrip()
    outputLine = []
    while inputLine:
        for char in inputLine:
            outputLine.append(charMap[char])
        printSolution(caseNumber, ''.join(outputLine))
        caseNumber = caseNumber + 1
        outputLine = []
        inputLine = inputFile.readline().rstrip()
outputFile.close