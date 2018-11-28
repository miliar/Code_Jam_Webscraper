#!/usr/bin/env python
from __future__ import with_statement
#from collections import defaultdict

def sorted_pair(e_1, e_2):
    if e_1 < e_2:
        return e_1 + e_2
    else:
        return e_2 + e_1
def processFile(fname):
    def processCase(f):
        case = f.readline().strip("\n").split(" ")
        C = int(case.pop(0))
        pairs = {}
        for i in range(C):
            formula = case.pop(0)
            pair = formula[:2]
            if formula[1] < formula[0]:
                pair = formula[1] + formula[0]
            pairs[pair] = formula[-1] 
        nulls = {}
        D = int(case.pop(0))
        for i in range(D):
            formula = case.pop(0)
            nulls.setdefault(formula[0], []).append(formula[1])
            nulls.setdefault(formula[1], []).append(formula[0])
            #pair = formula
            #if formula[1] < formula[0]:
            #    pair = formula[1] + formula[0]
            #nulls[pair] = True # this is awk.
        print pairs
        print nulls
        N = int(case.pop(0))
        invocation = case.pop(0)
        e_list = []
        for j in range(N):
            i = invocation[j]
            if e_list and pairs.get(sorted_pair(e_list[-1], i), []):
                e_list[-1] = pairs[sorted_pair(e_list[-1], i)]
            else:
                reset = False
                for e in nulls.get(i, []):
                    if e in e_list:
                        e_list = []
                        reset = True
                if not reset:
                    e_list.append(i)
        return str(e_list).replace("'","")
    
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
#processFile("B-small-attempt0.in")
processFile("B-large.in")