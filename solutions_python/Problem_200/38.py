# -*- coding: utf-8 -*-
from __future__ import division, print_function
from math import sqrt, ceil, floor
from gmpy2 import is_square, isqrt
from gurobipy import *

def parse(f):
    lst = []
    f.next()
    for l1 in f:
        N = l1.strip()
        lst.append((N))
    return lst


def is_tidy(l):
    for i in xrange(len(l) - 1):
        if l[i] > l[i+1]:
            return False
    return True


def tidy(N):
    sz = len(N)
    M = N
    while(not is_tidy(M)):
        firsti = next((i for i in range(sz-1) if M[i] > M[i+1]), None)
        M = N[:firsti] + str(int(N[firsti]) - 1) + "9"*(sz - firsti - 1)
    return str(int(M))


def output(fw, inlst):
    for i, a in enumerate(inlst):
        print(i, a)
        k = tidy(a)
        fw.write("Case #" + str(i+1) + ": " + str(k) + "\n")


f = open("B-large.in", 'r')
fw = open("B-large.out", 'w')
output(fw, parse(f))

# print(busy(3, 3, [4, 1, 3, 5]))
# print(busy(5, 2, [2,1]))
