#!/usr/bin/python2

from math import ceil, floor
from pdb import set_trace as T

def main():
    n = input()
    for t in range(n):
        input()
        li = map(int, raw_input().split())
        print 'Case #{}: {}'.format(t + 1, solve(li))

def argmin(fn, seq):
    m = min(seq, key=fn)
    return fn(m)

def solve(li):
    m = max(li)
    #splits = set(int(ceil(1.0 * m / i)) for i in range(1, m + 1))
    splits = range(1, m+1)
    def get_time(split):
        return split + sum(int(ceil(1.0 * i / split)) - 1 for i in li)
    return argmin(get_time, splits)

main()
