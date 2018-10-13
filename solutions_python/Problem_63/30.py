#!/usr/bin/python

import os
import sys
import math


infile = open(sys.argv[1])
T = int(infile.readline())
for i in range(T):
    line = infile.readline()
    items = line.split(' ')
    L = int(items[0])
    P = int(items[1])
    C = int(items[2])
    diff = math.log(float(P)/float(L), C)
    if diff <= 1:
        print 'Case #' + str(i+1) + ':', 0
    else:
        count = math.ceil(math.log(diff, 2))
        print 'Case #' + str(i+1) + ':', int(count)
