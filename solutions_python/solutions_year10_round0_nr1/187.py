#!/usr/bin/python

import sys
import math

f = open(sys.argv[1])

numCases = int(f.readline())
cur = 1;
for x in f.readlines():
    arr = x.split(" ")
    n = int(arr[0])
    k = int(arr[1]);
    m = 2 ** n
    if (k + 1) % m == 0:
        print "Case #" + str(cur) + ": ON"
    else:
        print "Case #" + str(cur) + ": OFF"
    cur += 1
