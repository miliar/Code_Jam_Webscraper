#!/usr/bin/env python3
import sys
from math import log

def solve(p,q):
    counter = 0
    while q > p:
#        print(q)
        if q % 2:
            return "impossible"
        q = int(q / 2)
        counter += 1
    if p == q:
        return counter
#    print ("{0} {1}".format(p,q))

    while q != 1:
#        print (q)
        if q % 2:
            return "impossible"
        q = int(q / 2)

    return counter

def main(filename):
    with open(filename, 'r') as f:
        testcases = int(f.readline())
        for case_num in range(testcases):
            P, Q = f.readline().split('/')
            P = int(P)
            Q = int(Q)
            print("Case #{0}: {1}".format(case_num+1, solve(P,Q)))
            

if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv[1])
