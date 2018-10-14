#!/bin/env python

# google code jam 2017 round 1A problem 1
# Daniel Scharstein

def fill(a, x, rmin, rmax, cmin, cmax):
    for r in range(rmin, rmax):
        for c in range(cmin, cmax):
            if a[r][c] == '?':
                a[r][c] = x
            elif a[r][c] != x:
                print("error 1")

def letters(a, rmin, rmax, cmin, cmax):
    s = set()
    for r in range(rmin, rmax):
        for c in range(cmin, cmax):
            s.add(a[r][c])
    return list(s - {'?'})

def solve(a, rmin, rmax, cmin, cmax):
    #print a
    x = letters(a, rmin, rmax, cmin, cmax)
    #print x
    n = len(x)
    if n == 1:
        fill(a, x[0], rmin, rmax, cmin, cmax)
        return
    for r in range(rmin, rmax):
        i = len(letters(a, rmin, r, cmin, cmax))
        if i >= 1 and i < n:
            solve(a, rmin, r, cmin, cmax)
            solve(a, r, rmax, cmin, cmax)
            return
    for c in range(cmin, cmax):
        i = len(letters(a, rmin, rmax, cmin, c))
        if i >= 1 and i < n:
            solve(a, rmin, rmax, cmin, c)
            solve(a, rmin, rmax, c, cmax)
            return
    print("error 2")
    

tests = int(raw_input())
for k in range(tests):
    r, c = map(int, raw_input().split())
    a = []
    for i in range(r):
        a.append(list(raw_input()))
    solve(a, 0, r, 0, c)
    print "Case #%d:" % (k+1)
    for row in a:
        print "".join(row)
