#! /usr/bin/python3.1

import sys
import os
import itertools
import multiprocessing

def winning1(a, b):
    if a < b:
        a, b = b, a
    a1 = a % b
    if a1 == 0:
        return 1
    a2 = a1 + b
    if a2 < a:
        result = max(-winning1(b, a1), -winning1(b, a2))
    else:
        result = -winning1(b, a1)
    return result
    
def winning(a, b):
    return winning1(a, b) > 0

def solve(case):
    ncase, case = case
    print("Solving #{0}: {1}".format(ncase, case), file=sys.stderr)
    a1, a2, b1, b2 = case
    count = 0
    for a in range(a1, a2+1):
        for b in range(b1, b2+1):
            if a == b:
                continue
            if winning(a, b):
                count += 1
    return (ncase, count)

def read_cases(inf):
    ncases = int(inf.readline().strip())
    cases = []
    for i in range(1, ncases + 1):
        case = (i, [int(x) for x in inf.readline().split()])
        cases.append(case)
    return cases

def get_ncores():
    with open('/proc/cpuinfo') as f:
        cores = [x for x in f.readlines() if x.startswith('processor\t:')]
    return len(cores)

def main(argv=sys.argv):
    cases = read_cases(sys.stdin)
    pool = multiprocessing.Pool(processes=get_ncores())
    #results = pool.map(solve, cases)
    results = [solve(case) for case in cases]
    for i, result in results:
        print("Case #{0}: {1}".format(i, result))
    return 0
        
if __name__ == '__main__':
    sys.exit(main())
