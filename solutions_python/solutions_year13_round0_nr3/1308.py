#!/usr/bin/python
from gmpy2 import mpz
from gmpy2 import isqrt

f = open("C-small-attempt0.in")
n = int(f.readline())
for i in xrange(n):
    s = f.readline()
    a = mpz(s.strip().split(' ')[0])
    b = mpz(s.strip().split(' ')[1])
    
    beg = isqrt(a)
    if beg**2 < a:
        beg = beg + 1
    end = isqrt(b)
    count = 0
    while beg <= end:
        if str(beg) == str(beg)[::-1]:
            if str(beg**2) == str(beg**2)[::-1]:
                count = count + 1
        beg = beg + 1
    print "Case #{0}: {1}".format(i+1, count)

f.close()
