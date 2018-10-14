#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Google Code Jam 2010: Round 1 - Task A

file = open("A-large.in", 'r')


lineNumb = 0
cases = []
for line in file:
    if lineNumb > 0:
        cases.append(line.strip())
    lineNumb += 1

caseNumb = 1
for case in cases:
    
    do = case.split(" ")
    binary = []
    binstring = ""
    for n in range(0, int(do[0])):
        binstring += "1"

    if (int(do[1]) +1) % (int(binstring, 2) +1) == 0:
        print "Case #" + str(caseNumb) + ": ON"
    else:
        print "Case #" + str(caseNumb) + ": OFF"
    caseNumb += 1   