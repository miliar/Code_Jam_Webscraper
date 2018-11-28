#!/usr/bin/python3

import sys
import math
from functools import reduce

def solve(L, k):
    maxsum = 0

    for i in range(len(L)):
        p = L[i]
        sum = p[0]*p[0] + 2*p[0]*p[1]

        if k>1:
            L2 = list(L)
            del L2[i]
            L2.sort(key=lambda x: x[0] * x[1], reverse=True)
            for p in L2[:k-1]:
                sum += 2*p[0]*p[1]

        if sum>maxsum:
            maxsum = sum

    return math.pi * maxsum

def main():
    nb = int(get_line())
    for case_id in range(1, nb + 1):
        l = get_line()
        N = int(l.split(' ')[0])
        K = int(l.split(' ')[1])
        LL = []
        for r in range(N):
            l = get_line()
            p = [int(x) for x in l.split()]
            LL.append(p)

        ret = solve(LL, K)

        print('Case #%d: %.9f' %(case_id, ret), file = o)

def get_line():
    return f.readline().strip()

def open_files():
    if len(sys.argv) == 1:
        f = sys.stdin
        o = sys.stdout

    if len(sys.argv) == 2:
        f = open(sys.argv[1], 'r')
        o = sys.stdout

    if len(sys.argv) == 3:
        f = open(sys.argv[1], 'r')
        o = open(sys.argv[2], 'w')

    return (f, o)

if __name__ == "__main__":
    (f, o) = open_files()
    main()

