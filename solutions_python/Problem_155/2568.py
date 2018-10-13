#!/usr/bin/env python

import os, sys, re

def read_input(filename):
    cases = []
    f = open(filename, 'r')
    for i, line in enumerate(f):
        words = line.split(' ')
        if i == 0:
            continue
        case = []
        for i in range(int(words[0])+1):
            case.append(words[1][i])
        cases.append(case)
    return cases

def solve_case(case):
    standing = 0
    friends = 0
    for ppl_needed, ppl_num in enumerate(case):
        ppl_num = int(ppl_num)
        if ppl_num > 0:
            to_add = max(ppl_needed - standing, 0)
            standing += ppl_num + to_add
            friends += to_add
    return friends

filename = sys.argv[1] if len(sys.argv) > 1 else 'input2.txt'
cases = read_input(filename)
for i, case in enumerate(cases):
    print 'Case #%i: %i' % (i+1, solve_case(case))
