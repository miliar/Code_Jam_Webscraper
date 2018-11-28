# -*- coding: utf-8 -*-

import sys

def solve(n, l, h, notes):
    for i in range(l, h+1):
        for n in notes:
            if i < n:
                if n % i != 0:
                    break
            elif i > n:
                if i % n != 0:
                    break
        else:
            return str(i)
    return "NO"

def main():
    f = sys.stdin
    t = int(f.readline())
    for i in range(t):
        n,l,h = [int(s) for s in f.readline().split()]
        notes = [int(s) for s in f.readline().split()]
        print "Case #%d: %s" % (i+1, solve(n,l,h,notes))

main()
