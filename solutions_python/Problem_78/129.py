#!/usr/bin/env python

import sys, fractions, functools

def solve(N, pd, pg):
    if pg == 100 and pd < 100:
        return "Broken"
    elif pg == 0 and pd > 0:
        return "Broken"
    elif 100/fractions.gcd(100,pd) > N:
        return "Broken"
    else:
        return "Possible"

inputfilename = sys.argv[1]
inputfile = open(inputfilename, "r")

## parse file
## drop first line
line = inputfile.readline()
case = 1

for line in inputfile:
    args = line.split(' ')
    N = int(args[0])
    pd = int(args[1])
    pg = int(args[2])
    
    result = solve(N, pd, pg)
    print("Case #%d: %s" % (case, result))
    case = case + 1