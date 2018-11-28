#!/usr/bin/python
import sys
from sys import stderr
from fractions import Fraction

"""
pd = 100 * wd / d
pg = 100 * wg / g


d <= n
wd <= n

d <= g

pd / 100 = wd / d
pg / 100 = wg / g


80 / 100
56 / 100

4 = 5 * wd / d
14 = 25 * wg / g

wd ~ 4
d ~ 5

wg ~ 14
g ~ 25

d = wd * 100 / pd

"""

def Solve(n, pd, pg):
    print >>stderr, n, pd, pg

    if pg == 0 and pd != 0:
        return "Broken"
    if pg == 100 and pd != 100:
        return "Broken"
    if pd == 0:
        return "Possible"


    fd = Fraction(pd, 100)
    fg = Fraction(pg, 100)
    print >>stderr, fd, fg

    m_wd = fd.numerator
    m_d = fd.denominator
    m_wg = fg.numerator
    m_g = fg.denominator

    m_d = ((m_wd + m_d - 1)/ m_d) * m_d
    m_g = ((m_wg + m_g - 1)/ m_g) * m_g

    if m_d > n:
        return "Broken"
    else:
        return "Possible"


f = open(sys.argv[1])

T = int(f.readline())
for t in range(T):
    n, pd, pg = map(int, f.readline().split())
    print "Case #%d: %s" % (t+1, Solve(n, pd, pg))



