#!/bin/env python

# google code jam 2015 problem 3

i = 2
j = 3
k = 4

mt = { (1, 1) : 1, (1, i) :  i, (1, j) :  j, (1, k) :  k,
       (i, 1) : i, (i, i) : -1, (i, j) :  k, (i, k) : -j,
       (j, 1) : j, (j, i) : -k, (j, j) : -1, (j, k) :  i,
       (k, 1) : k, (k, i) :  j, (k, j) : -i, (k, k) : -1 }

def mult(x, sy):
    if sy == 'i':
	y = i
    elif sy == 'j':
	y = j
    else:
	y = k
    ax = abs(x)
    ay = abs(y)
    sx = x / ax
    sy = y / ay
    return mt[ax, ay] * sx * sy

def prod(s):
    p = 1
    for c in s:
	p = mult(p, c)
    return p

def solve(s):
    x = 0
    n = len(s)
    p = 1
    while x < n and p != i:
	p = mult(p, s[x])
	x += 1
    p = 1
    while x < n and p != j:
	p = mult(p, s[x])
	x += 1
    p = 1
    while x < n:
	p = mult(p, s[x])
	x += 1
    return p == k

tests = int(raw_input())
for t in range(tests):
    L, X = [int(x) for x in raw_input().split()]
    s = raw_input()
    if X > 7:
	X = (X % 4) + 4
    #print prod('ijk'), prod(s), prod(s*2), prod(s*4)
    s = s * X
    #print L * X, len(s), s[:50]
    sol = "YES" if solve(s) else "NO"
    print "Case #%d: %s" % (t+1, sol)
