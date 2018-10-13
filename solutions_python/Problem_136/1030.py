# Python 2.7
from __future__ import division
from __future__ import print_function

n_cases = int(raw_input())
for ctr in xrange(1, n_cases+1):
    c, f, x = [float(x) for x in raw_input().split(' ')]
    t = 0 # current time
    n = 0 # num cookies
    r = 2 # current rate
    while n < x:
        if x < c or c*(r+f) + x*r >= x*(r+f):
            t += (x-n)/r
            break
        else:
            # Buy a building
            t += c/r
            r += f
    print('Case #%d: %.7f' % (ctr, t))
