#!/usr/bin/python
# -*- coding: utf-8 -*-

from sys import stdin

def solveCase():
    _, people = stdin.readline().split()    
    up, needed = 0, 0
    for level, x in enumerate(people):
        if level > up:
            needed += level - up
            up += level - up
        up += int(x)
        
    print needed

caseCnt = int(stdin.readline())

for caseNr in range(1, caseCnt + 1):
    print "Case #" + str(caseNr) + ":",
    solveCase()
