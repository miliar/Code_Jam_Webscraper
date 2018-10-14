#!/usr/bin/env python
from __future__ import with_statement
#from collections import defaultdict

def processFile(fname):
    def processCase(f):
        f.readline().strip("\n").split(" ")
        case = f.readline().strip("\n").split(" ")
        xs = [int(i) for i in case]
        n = 0
        for i, x in enumerate(xs):
            if x != (i+1):
                n += 1
        return n
        
    with open(fname, "r") as f:
        cases = int(f.readline().strip("\n"))
        output = ""
        for case in range(cases):
            a = processCase(f)
            output += "Case #%d: %6f\n" % (case + 1, a)
        print output
    with open("ans"+fname, "w") as f:
        f.write(output)
        
#processFile("sample.txt")
#processFile("D-small-attempt0.in")
processFile("D-large.in")