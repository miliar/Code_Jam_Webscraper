#!/usr/bin/env python
from __future__ import with_statement
#from collections import defaultdict

def _gcd(ds):
    if len(ds) == 1:
        return ds[0]
    x = 0
    y = 0
    while (ds):
        if (x == 0): x = ds.pop()
        if (y == 0): y = ds.pop()
        if (x == 1) or (y == 1):
            return 1
        while (x!=0 and y!=0):
            if (x > y):
                x -= y
            else: y -= x
    return x+y

def gcd(ds):
    if len(ds) == 1:
        return ds[0]
    x = 0
    y = 0
    while (ds):
        if (x == 0): x = ds.pop()
        if (y == 0): y = ds.pop()
        #if (x == 1) or (y == 1):
        #    return 1
        while (x!=0 and y!= 0):
            t = x
            x = y % x
            y = t
    return x + y

def processFile(fname):
    def processCase(f):
        n = f.readline().strip("\n").split(" ")
        n = n[1:]
        n = [int(x) for x in n]
        ds = []
        for i,x in enumerate(n):
            for j, y in enumerate(n[i+1:]):
                nd = abs(x - y)
                ds.append(nd)
        d = gcd(ds)
        if (d == 1):
            return 0
        return -n[0] % d
    
    with open(fname, "r") as f:
        cases = int(f.readline().strip("\n"))
        output = ""
        for case in range(cases):
            a = processCase(f)
            output += "Case #%d: %s\n" % (case + 1, a)
        print output
    with open("ans"+fname, "w") as f:
        f.write(output)

#processFile("qual2.in")
#processFile("qual2.test")
#processFile("sample.txt")
#processFile("B-small-attempt2.in")
processFile("B-large.in")
