#!/usr/bin/env python
from __future__ import with_statement
#from collections import defaultdict


def processFile(fname):
    def processCase(f):
        n = f.readline().strip("\n").split(" ")
        case = f.readline().strip("\n").split(" ")
        bitbucket = {}
        ns = []
        for i in case:
            i = int(i)
            ns.append(i)
        if reduce(lambda x, y: x ^ y, ns) != 0:
            return "NO"
        else:
            return sum(ns) - min(ns)
        
    
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
#processFile("C-small-attempt0.in")
processFile("C-large.in")