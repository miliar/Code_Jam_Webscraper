import sys
from fractions import gcd
from math import log

n = int(sys.stdin.readline())

for i in range(n):
    n,d = [int(x) for x in sys.stdin.readline().split('/')]
    g = gcd(n, d)
    n = n / g
    d = d / g
    r = log(d, 2)
    if (r != int(r)):
        ans = 'impossible'
    else:
        c = 1
        while ((float(n) / d) < 0.5):
            d = d / 2
            c = c + 1
        ans = c
    print 'Case #%d: %s' % (i + 1, ans)
        
