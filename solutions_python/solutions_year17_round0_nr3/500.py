#!/bin/env python

# google code jam 2017 qualifiers problem 3
# Daniel Scharstein

def update(c, q, a, i):
    if a in c:
        c[a] += i
    else:
        c[a] = i
    q.add(a)
    
def solve(n, k):
    c = {n:1}
    q = {n}
    i = 0
    while i < k:
        m = max(q)
        q.remove(m)
        cnt = c[m]
        #print "m=%d cnt=%d c=%s" %(m, cnt, c)
        i += cnt
        a, b = m/2, (m-1)/2
        update(c, q, a, cnt)
        update(c, q, b, cnt)
    return a, b

tests = int(raw_input())
for t in range(tests):
    n, k = map(int, raw_input().split())
    a, b = solve(n, k)
    print "Case #%d: %d %d" % (t+1, a, b)
