#!/usr/bin/env python

import sys
import math

def Qpalendrome(x):
    x = str(x)
    if x == x[::-1]:
        return True
    else:
        return False

fair_square = []
for n in xrange(1, long(1e7)):
    if Qpalendrome(n):
        p = n*n
        if Qpalendrome(p):
            fair_square.append(p)
#print len(fair_square)
#print fair_square

f = open(sys.argv[1],'r')
# read num cases
T = int(f.readline())

for i in range(T):
    A, B = map(long, f.readline().split())
    num_squares = 0
    for j in fair_square:
        if A <= j and B >=j:
            num_squares += 1
    print "Case #%d: %d" % (i+1, num_squares)
