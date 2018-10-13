#!/usr/bin/env python

import numpy as np


def cookie_min_time(c, f, x):
    c = float(c)
    f = float(f)
    x = float(x)

    #tol = 1e-6
    n = 0
    t_n = x / 2
    t_m = c / 2 + x / (2 + f)

    while t_m < t_n:
        n += 1
        t_n = t_m
        t_m -= x / (2 + n*f)
        t_m += c / (2 + n*f)
        t_m += x / (2 + (n+1)*f)

    return t_n


#input_file = 'data'
#input_file = 'B-small-attempt0.in'
input_file = 'B-large.in'

f = open(input_file)
lines = f.read().splitlines()
f.close()

T = int(lines[0])
for i in xrange(T):
    x = np.fromstring(lines[i+1], dtype=float, sep=' ')
    #print x[0], x[1], x[2]
    t = cookie_min_time(x[0], x[1], x[2])
    print "Case #%d: %.7f" % (i + 1, t)
