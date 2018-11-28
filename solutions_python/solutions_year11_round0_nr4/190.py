#!/usr/bin/python

import sys, math

def main():
    lines = iter(sys.stdin)
    T = int(next(lines))
    for x in range(1, T+1):
        N = int(next(lines))
        lst = list(int(a) for a in next(lines).split())
        lst_sorted = sorted(lst)
        ans = sum(1 for a,b in zip(lst, lst_sorted) if a!=b)
        print "Case #%s: %0.6f" % (x, ans)

main()
