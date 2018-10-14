#!/usr/bin/env python
# encoding: utf-8

import sys
import os

def prepare(g, k):
    n = len(g)
    u, v = [], []
    for p in range(n):
        s = 0
        q = p
        c = 0
        while s + g[q] <= k and c < n:
            s += g[q]
            q = (q + 1) % n
            c += 1
        u.append(q)
        v.append(s)
    return u, v

def main():
    t = int(sys.stdin.readline())
    for i in range(t):
        r, k, n = map(int, sys.stdin.readline().split())
        g = map(int, sys.stdin.readline().split())
        next, money = prepare(g, k)
        p = 0
        total = 0
        count = 0
        s = [0] * n
        c = [0] * n
        while count < r:
            count += 1
            total += money[p]
            if c[p] != 0:
                cycle_len = count - c[p]
                cycle_sum = total - s[p]
                x = (r - count) // cycle_len
                total += cycle_sum * x
                count += cycle_len * x
            c[p] = count
            s[p] = total
            p = next[p]
        print "Case #%d: %d" % (i + 1, total)

if __name__ == '__main__':
	main()
