#!/usr/bin/env python
from itertools import *
import re, sys

def solve(invoke, good, bad):
    good = sorted(good, key=len, reverse=True)
    bad = sorted(bad, key=len, reverse=True)

    current = ""
    for c in invoke:
        current += c
        for g in good:
            current = current.replace(g[:2], g[2])
            current = current.replace(g[:2][::-1], g[2])
        for b in bad:
            if b[0] in current and b[1] in current:
                current = ""
                break
    return current

input_file = sys.argv[1]
with open(input_file) as file:
    for i,line in enumerate(map(lambda ln: ln.strip(), islice(file, 1, None))):
        fields = line.split(" ")[1:]
        indices = [j for j,f in enumerate(fields) if f.isdigit()]
        good = fields[0:indices[0]]
        bad = fields[indices[0]+1:indices[1]]
        invoke = fields[indices[1]+1:][0]
        
        result = solve(invoke, good, bad)
        result = "[" + ", ".join(result) + "]"
        print "".join(map(str,["Case #",i+1,": ", result]))
            
