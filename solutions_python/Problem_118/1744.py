#!/usr/bin/env python

import sys, fractions, functools

       
def solve(A, B):
    small = [1, 4, 9, 121, 484]
    
    result = 0
    for i in small:
        if (i >= A and i <= B):
            result = result +1
    return result

inputfilename = sys.argv[1]
inputfile = open(inputfilename, "r")

## parse file
## drop first line
line = inputfile.readline()
case = 1

for line in inputfile:
    args = line.split(' ')
    A = int(args[0])
    B = int(args[1])
                
    result = solve(A, B)
    print("Case #%d: %i" % (case, result))
    case = case + 1