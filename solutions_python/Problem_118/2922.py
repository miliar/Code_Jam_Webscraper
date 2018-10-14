#!/usr/bin/env python

import math
import sys

def is_pal(x):
    return str(x) == ''.join(reversed(str(x)))

def solve(a,b):
    count = 0
    i = int(math.sqrt(a))-1
    while True:
        i += 1
        sq = i**2
        if sq > b:
            break
        else:
            if sq >= a and is_pal(i) and is_pal(sq):
                count += 1
            else:
                pass
    return count

def run(fn):
    with open(fn) as f:
        lines = [map(int, line.strip().split()) for line in f.readlines() if line]
    for case, (a,b) in enumerate(lines[1:], start=1):
        print "Case #{}: {}".format(case, solve(a,b))
        
run(sys.argv[1])
