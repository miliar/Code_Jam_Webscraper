#!/usr/bin/env python

import sys

def solve(convert, opposites, input):
    out = []
    for x in list(input):
        out.append(x)
        if len(out) >= 2:
            if convert.has_key(out[-2] + out[-1]):
                out[-2] = convert[out[-2] + out[-1]]
                del out[-1]
                continue
        
        if opposites.has_key(x):
            if opposites[x] in out:
                out = []
    
    return out

def lprint(list):
    sys.stdout.write("[")
    x = 0
    for y in list:
        x += 1
        if x < len(list):
            sys.stdout.write(y + ", ")
        else:
            sys.stdout.write(y)
    
    sys.stdout.write("]\n")

T = int(raw_input().strip())

for t in range(T):
    line = raw_input().strip().split()
    C = int(line[0])
    del line[0]
    convert = {}
    opposites = {}
    for c in range(C):
        input = line[0]
        convert[input[0] + input[1]] = input[2]
        convert[input[1] + input[0]] = input[2]
        del line[0]

    D = int(line[0])
    del line[0]
    for d in range(D):
        input = line[0]
        opposites[input[0]] = input[1]
        opposites[input[1]] = input[0]
        del line[0]

    N = line[0]
    input = line[1]

    #print convert, opposites, input
    s = solve(convert, opposites, input)
    sys.stdout.write("Case #%d: " % (t+1))
    lprint(s)
