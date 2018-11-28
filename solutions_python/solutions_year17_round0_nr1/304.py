#!/usr/bin/env python3

import sys
import os

def solve(s, k) :
    l = len(s)
    n = 0
    s = list(s)
    for i in range(l):
        if s[i] == '+': continue
        if i > (l-k): return "IMPOSSIBLE"
        for j in range(k):
            s[j+i] = '+' if s[j+i] == '-' else '-'
        n += 1

    return n

def main():
    sys.stdin.readline()
    for i, l in enumerate(sys.stdin):
        (s, k) = l.split(' ')
        ans = solve(s,int(k))
        print("Case #{}: {}".format(i+1, ans))

if __name__ == '__main__':
    main()
