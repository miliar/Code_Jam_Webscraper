#!/usr/bin/env python3

def calc(n, l, h, a):
        for f in range(l, h+1):
                found = True
                for g in a:
                        if g % f and f % g:
                                found = False
                                break
                if found: return f
        return 'NO'

t = int(input())
for i in range(t):
        n, l, h = [int(a) for a in input().split()]
        a = [int(a) for a in input().split()]
        print("Case #{0}: {1}".format(i+1, calc(n, l, h, a)))

