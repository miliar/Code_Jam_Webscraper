#!/usr/bin/env python
#from collections import defaultdict
from __future__ import with_statement
import psyco
psyco.full()

def range_recycle(a,b):
    count = 0
    for i in xrange(a, b):
        s = str(i) * 2
        l = len(s) / 2
        this_time = []
        for j in range(1, l):
            z = int(s[j:j+l])
            if i < z <= b and z not in this_time:
                this_time.append(z)
                count += 1
    return count
        
        
def processFile(fname):
    def processCase(f):
        a, b= f.readline().strip("\n").split(" ")
        return range_recycle(int(a), int(b))
    
    with open(fname, "r") as f:
        cases = int(f.readline().strip("\n"))
        output = ""
        for case in range(cases):
            a = processCase(f)
            output += "Case #%d: %s\n" % (case + 1, a)
        print output
    with open("ans"+fname, "w") as f:
        f.write(output)

#processFile("sample.txt")
#processFile("C-small-attempt1.in")
processFile("C-large.in")