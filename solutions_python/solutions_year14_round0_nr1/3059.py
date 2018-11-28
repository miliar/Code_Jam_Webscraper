#!/usr/bin/env python

import sys, fractions, functools

inputfilename = sys.argv[1]
inputfile = open(inputfilename, "r")

## parse file
## drop first line
line = inputfile.readline()
case = 1

for line in inputfile:
    i = int(line) - 1
    j = 0
    while i != j:
        line = inputfile.readline()
        j = j+1
    line = inputfile.readline()
    set0 = set(line.split(' '))
    set1 = {int(x) for x in set0}
    
    while j != 3:
        line = inputfile.readline()
        j = j+1
    
    line = inputfile.readline()
    i = int(line) - 1
    j = 0
    while i != j:
        inputfile.readline()
        j = j+1
    line = inputfile.readline()
    set0 = set(line.split(' '))
    set2 = {int(x) for x in set0}
    
    inter = set.intersection(*[set1, set2])
    
    while j != 3:
        line = inputfile.readline()
        j = j+1
    
    if len(inter) == 0:
        print("Case #%d: Volunteer cheated!" % (case))
    elif len(inter) > 1:
        print("Case #%d: Bad magician!" % (case))
    else:
        res = list(inter)
        print("Case #%d: %d" % (case, res[0]))
    case = case + 1