import sys
from fractions import gcd
import numpy as np

lines = open(sys.argv[1]).readlines()

T = int(lines[0])

casenum = 0

for line in lines[1:]:
    casenum += 1
    vals = line.split()
    N = vals[0]

    l = len(N)
    tidy = '0'*l

    for i in xrange(l):
        for j in xrange(9, -1, -1):
            test = tidy[:i] + str(j)*(l-i)
            if test > tidy and test <= N:
                tidy = test
                break

    while tidy[0] == '0':
        tidy = tidy[1:]

    print 'case #' + str(casenum) + ": " + tidy


        
