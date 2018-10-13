#!/usr/bin/env python3

import sys
import os
import bisect

def insert(s, a):
    (v, c) = a
    if v == 0: return
    pos = bisect.bisect(s, (v, 0))
    if pos == len(s) -1 or len(s) == 0:
        s.insert(pos, (v, c))
    else:
        (v2, c2) = s[pos]
        if v2 == v:
            s[pos] = (v, c+c2)
        else:
            s.insert(pos, (v,c))

def solve(n,k) :
    s = [(n,1)]
    while True:
        (p, i) = s.pop()
        if k <= i:
            break
        k -= i
        p -= 1
        l,r = (p//2 + p%2, p//2)
        insert(s, (l, i))
        insert(s, (r, i))

    p -= 1
    return (p//2 + p%2, p//2)

def main():
    sys.stdin.readline()
    for i, line in enumerate(sys.stdin):
        (n, k) = line.split(' ')
        l,r = solve(int(n), int(k))
        print("Case #{}: {} {}".format(i+1, l, r))

if __name__ == '__main__':
    main()
