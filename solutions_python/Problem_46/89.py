#!/usr/bin/env python2.6
import sys
from itertools import takewhile

def final_zeroes(r):
    return len(list(takewhile(lambda x: x == "0", reversed(r))))

def bubble_steps(x):
    changed = True
    steps = 0
    while changed:
        changed = False
        for i in range(len(x)):
            if x[i] > i+1:
                changed = True
                for j in range(i+1, len(x)):
                    if x[j] <= i+1:
                        v = x[j]
                        del x[j]
                        x.insert(i, v)
                        steps += (j - i)
                        break
                break
            
    return steps

with open(sys.argv[1], "r") as f:
    tests = int(f.readline().strip())
    for i in range(tests):
        s = int(f.readline().strip())
        m = [s - final_zeroes(f.readline().strip()) for _ in range(s)]
        v = bubble_steps(m)
        print "Case #%d: %i" % (i+1, v)

        
