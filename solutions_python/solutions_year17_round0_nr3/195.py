#!/usr/bin/python3

import sys
import math
from functools import reduce

def solve(n, k):
    if k == 1:
        n1 = n // 2
        n2 = n1 - (n - 1) % 2
        return str(n1) + ' ' + str(n2)

    corr = 0
    if k % 2 != 0:
        if n//2*2 == n:
            corr = -1
    return solve(n//2 + corr, k//2)

def main():
    nb = int(get_line())
    for case_id in range(1, nb + 1):
        l = get_line()
        N = int(l.split(' ')[0])
        K = int(l.split(' ')[1])
        ret = solve(N, K)

        if ret == None:
            l = 'IMPOSSIBLE'
        else:
            l = str(ret)

        print('Case #%d: %s' %(case_id, l), file = o)

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

