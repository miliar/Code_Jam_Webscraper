#!/usr/bin/env python

import sys 
import itertools

input = sys.argv[1]

cases = []

with open(input) as fh:
    num_cases = fh.readline()
    for case in range(0,int(num_cases)):
        cases.append(fh.readline().strip())

cn = 1
for case in cases:
    num = int(case)
    targ = case.strip()+'0'
    best = None 
    for item in itertools.permutations(targ,len(targ)):
        sol = int(''.join(item))
        if sol < num or sol == num:
            continue
        if best is None:
            best = sol
        elif (sol - num) < (best - num):
            best = sol

    print 'Case #%d: %d' % (cn, best)
    cn += 1
