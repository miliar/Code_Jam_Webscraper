#!/usr/bin/python

import os
import sys

infile = open(sys.argv[1])

count = 1
line_num = int(infile.readline())

for i in range(line_num):
    line = infile.readline()
    items = line.split(' ')
    N = int(items[0])
    k = int(items[1])
    if (k + 1) % pow(2, N) == 0:
        print 'Case #' + str(i + 1) + ': ON'
    else:
        print 'Case #' + str(i + 1) + ': OFF'
