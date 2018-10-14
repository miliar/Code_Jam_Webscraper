from decimal import *
from sys import stdin

t = int(stdin.readline())

b = 3 + Decimal(5).sqrt()
for i in range(t):
    n = int(stdin.readline())
    x = b ** n
    s = str(x)
    k = s.find('.')
    j = max(0, k - 3)
    t = s[j:k]
    print "Case #%d: %03d" % (i+1, int(t))

