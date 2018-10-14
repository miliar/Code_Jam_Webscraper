#!/usr/bin/env python

import sys, fractions, functools

inputfilename = sys.argv[1]
inputfile = open(inputfilename, "r")

## parse file
## drop first line
line = inputfile.readline()
case = 1

def solve(C,F,X):
    n = int( X/C - 2/F)
    if n<0:
        n = 0
    
    if n == 0:
        res = X/2
    else:
        farms = {C/(2+x*F) for x in range(n)}
        s = sum(farms)
        res  = s + X / (2+n*F)
    
    return res


for line in inputfile:
    args = line.split(' ')
    C = float(args[0])
    F = float(args[1])
    X = float(args[2])
    
    res = solve(C,F,X)
    
    print("Case #%d: %f" % (case, res))
    case = case + 1