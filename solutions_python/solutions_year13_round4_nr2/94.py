#!/usr/bin/env pypy
from __future__ import with_statement
import math
import sys

def floor_log(k):
    return len(bin(k))-3

def compute_result(N, P):
    power = 2**N
    if P == power:
        return (P-1, P-1)
    guaranteed = floor_log(power-P)+1
    always = 2**(N-guaranteed+1) - 2
    poss_wins = N-floor_log(P)
    sometimes = power - 2**poss_wins
    return (always, sometimes)

def main():
    fname, gname = sys.argv[1:]
    with open(fname) as f, open(gname, 'w') as g:
        # number of test cases
        T = int(f.readline().strip())
        for i in xrange(T):
            N, P = map(int, f.readline().strip().split())
            always, sometimes = compute_result(N, P)
            g.write("Case #{0}: {1} {2}\n".format(i+1, always, sometimes))

if __name__ == "__main__":
    status = main()
    sys.exit(status)
