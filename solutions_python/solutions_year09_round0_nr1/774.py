#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
# Google Code Jam 2009: Task A

file = open("input.txt", 'r')

words = []
cases = []

lineNumb = 0
for line in file:
    if lineNumb == 0:
        wordLength, wordCount, caseCount = line.split()
    elif int(wordCount) >= lineNumb:
        words.append(line.strip())
    else:
        cases.append(re.compile(line.strip().replace("(","[").replace(")","]")))
    lineNumb = lineNumb + 1
    
caseNumb = 1
for case in cases:
    matchCount = 0
    for word in words:
        if case.match(word):
            matchCount = matchCount + 1
    print "Case #" + str(caseNumb) + ": " + str(matchCount)
    caseNumb = caseNumb + 1