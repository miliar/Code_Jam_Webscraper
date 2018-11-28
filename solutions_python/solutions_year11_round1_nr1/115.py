#! /usr/bin/env python

T = input()

def gcd(n, m):
    if n>m:
        m, n = n, m
    if n==0:
        return m
    else:
        return gcd(m%n, n)

def solve(N, PD, PG):
    if PG == 100:
        if PD != 100:
            return "Broken"
        else:
            return "Possible"
    if PG == 0:
        if PD == 0:
            return "Possible"
        else:
            return "Broken"
    x = 100/gcd(PD, 100)
    if x<=N:
        return "Possible"
    else:
        return "Broken"
    
for t in range(1, T+1):
    N, PD, PG = map(int, raw_input().split())
    print "Case #%d: %s" % (t, solve(N, PD, PG))
