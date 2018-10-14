#!/usr/bin/env python

import fileinput
import sys
import math

def read_cases():
    fh = fileinput.input()
    T = int(fh.readline().strip())
    cases = []
    for t in range(T):
        case = {}
        N, X = map(int, fh.readline().strip().split(" "))
        S = map(int, fh.readline().strip().split(" "))
        case["N"], case["X"], case["S"] = N, X, S 
        cases += [case]
    if fh.readline().strip() !="":
        raise Exception
    return cases



def process_case(case):
    discs = case["S"]
    X = case["X"]
    discs.sort()
    d = 0
    while discs:
        if len(discs)>=2 and discs[-1] + discs[0] <= X:
            d+=1
            discs = discs[1:-1]
        else:
            discs = discs[:-1]
            d+=1
        
    return d


if __name__ == "__main__":
    cases = read_cases()
    #print cases

    for i, case in enumerate(cases[:]):
        result = process_case(case)
        print "Case #%s:" % (i+1, ) , result
        #sys.stderr.write("Progress: %d/%d (%d%%) \r" % (i+1, len(cases), int(100.*(i+1)/len(cases) ) ) )
        #sys.stderr.flush()
