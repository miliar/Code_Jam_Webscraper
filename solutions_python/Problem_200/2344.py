#!/usr/bin/python
# coding=utf8

import sys

nbCases = 0

index = -1
for line in sys.stdin:
    index += 1
    if index == 0:
        nbCases = int(line)
        continue
    
    current = line.strip("\n")
    i = 0
    while i < len(current):
        if i > 0 and int(current[i]) < int(current[i-1]):
            current = str(int(current) - (int(current[i:]) + 1))
            i = 0
            continue
        
        if i == len(current)-1:
            print "Case #" + str(index) + ": " + current
            break
        
        i += 1