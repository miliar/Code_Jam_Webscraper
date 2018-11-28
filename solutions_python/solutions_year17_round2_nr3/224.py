#!/bin/env python3

# google code jam 2017 round 1B problem 3
# Daniel Scharstein

def solve(a, d):
    n = len(a)
    t = [-1] * n
    t[0] = 0
    cd = [0] * n
    for i in range(n-1):
        cd[i+1] = cd[i] + d[i]
    for i in range(n):
        maxd, s = a[i]
        d0 = cd[i]
        t0 = t[i]
        for j in range(i+1, n):
            d1 = cd[j]
            dd = d1 - d0
            if dd <= maxd:
                t1 = t0 + dd / s
                if t[j] < 0 or t1 < t[j]:
                    t[j] = t1
            else:
                break
    return t[n-1]

tests = int(input())
for t in range(tests):
    n, q = map(int, input().split())
    #print("n", n, "q", q)
    a = []
    for i in range(n):
        e, s = map(int, input().split())
        a.append((e, s))
    d = []
    for i in range(n):
        dd = list(map(int, input().split()))
        if i+1 < n:
            d.append(dd[i+1])
    u, v = map(int, input().split())
    #print("a", a)
    #print("d", d)
    #print("u", u, "v", v)

    if q > 1:
        x = 0
    else:
        x = solve(a, d)
    print("Case #%d: %s" % (t+1, x))
