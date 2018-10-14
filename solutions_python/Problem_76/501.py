#!/usr/bin/env python

import sys

def solve(N, C):
    xor_sum = 0
    for x in C:
        xor_sum = xor_sum ^ x
    if (xor_sum != 0):
        return "NO"
    else:
        return sum(C)-min(C)

inputfilename = sys.argv[1]
inputfile = open(inputfilename, "r")

# parse file
# drop first line
line = inputfile.readline()
case = 1

for line in inputfile:
    args = line.split(' ')
    N = int(args[0])
    line = inputfile.readline()
    C = [int(x) for x in line.split(' ')]
    result = solve(N,C)
    print("Case #%d: %s" % (case, result))
    case = case + 1
