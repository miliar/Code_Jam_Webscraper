import math
from decimal import *


#f = open(r'e:\downloads\A-large.in', 'r')
f = open(r'e:\downloads\A-small-attempt0.in', 'r')
#f = open(r'h:\work\python\code_jam\bullseye.txt', 'r')

def solve(r, t):
    p = Decimal(2*r-1)/ 2
    q = Decimal(-t)/ 2
    D = (p/2)**2-q
    res = int(-p/2+D.sqrt())
    if res*(2*r+2*res-1) > t:
        res -= 1

    return res

T = int(f.readline())
for t in range(1, T+1):
    r, tt  = map(int, f.readline().split())

    print "Case #%d: %d" % (t, solve(r, tt))


