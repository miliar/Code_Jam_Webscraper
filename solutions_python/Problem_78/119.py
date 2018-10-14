#!/usr/bin/python

from fractions import gcd

def solve(n,pd,pg):
    # 100 | DPd
    # 100 | (Pg-Pd)*d + Pg*d'
    # D <= N
    if pg == 0 and pd > pg:
        return "Broken"
    if pg == 100 and pg > pd:
        return "Broken"
    m = 100 / gcd(pd,100)
    m2a = gcd(pg,100)
    m2 = m2a/ gcd(abs(pg-pd),m2a)
    lcm = m*m2/gcd(m,m2)
    if lcm > n:
        return "Broken"
    return "Possible" 

r = input()
for i in range(1,r+1):
    l = map(int,raw_input().split())
    n,pd,pg = tuple(l)
    print "Case #%s: %s" % (i, solve(n,pd,pg))
