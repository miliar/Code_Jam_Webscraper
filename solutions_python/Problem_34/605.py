#!/usr/bin/env /usr/bin/python
# -*- coding: utf-8 -*-

import sys

def testCaseTokenizer(testCase):
    tokens = []
    partOfComplexToken = False
    for char in testCase:
        if char == "(":
            partOfComplexToken = True
            tokens.append("")
        elif char == ")":
            partOfComplexToken = False
        else:
            if(partOfComplexToken):
                tokens[-1] = tokens[-1] + char
            else:
                tokens.append(char)
    
    return tokens

def testCaseMatch(testCase, word):
    if len(testCase) != len(word):
        sys.stderr.write("! ERR: Test Case mas largo que word\n")
        return False
    
    for i in range(0, len(word)):
        if not word[i] in testCase[i]:
            return False
    
    return True

fileHandle = open(sys.argv[1])

wordLength, testLinesLength, testCasesLength = [int(a) for a in fileHandle.readline().strip().split(" ")]
testLines = list()
actualLine = 0
actualTest = 0

for line in fileHandle:
    line = line.strip()
    if actualLine < testLinesLength:
        actualLine = actualLine + 1
        
        if len(line) != wordLength:
            sys.stderr.write("! ERR: Linea '%s' no coincide con tamaño %s.\n" % (line, wordLength))
            continue
        
        sys.stderr.write("  DBG: Agregue linea '%s'\n" % line)
        testLines.append(line)
    else:
        coincidences = 0
        actualTest = actualTest + 1
        parsedTestCase = testCaseTokenizer(line)
        
        for testLine in testLines:
            if testCaseMatch(parsedTestCase, testLine):
                coincidences = coincidences + 1
        
        print "Case #%d: %d" % (actualTest, coincidences)
    


