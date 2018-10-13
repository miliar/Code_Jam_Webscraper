#!/usr/bin/python

from sys import stdin
from operator import mul

def calc_P(A, B, p):
    global _p
    _p = p
    rem = B - A + 1
    retype = B + 1
    keep_type = p_to(A) * rem + (1.0 - p_to(A)) * (rem + retype)
    back_space_n = [p_to(A-n) * (2*n+rem) + (1.0 - p_to(A-n)) * (2*n+rem + retype) for n in range(1, 1+A)]
    enter = 1 + retype
    return min([keep_type, enter] + back_space_n)

def p_to(num_letters):
    return reduce(mul, _p[0:num_letters], 1)

T = int(stdin.readline())
for i in range(1, 1+T):
    A, B = map(int, stdin.readline().split())
    p = map(float, stdin.readline().split())
    print "Case #%d: %f" % (i, calc_P(A, B, p))

