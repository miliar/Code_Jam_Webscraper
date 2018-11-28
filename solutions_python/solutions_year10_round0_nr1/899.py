#!/usr/bin/python

import sys
#read 1st line as 

test_cases = int(sys.stdin.readline())
for i in xrange(1,test_cases+1):
    n, k = sys.stdin.readline().split()
    n, k = int(n), int(k)
    result = "OFF"
    if(k % 2**n == 2**n-1):
        result = "ON"
    print "Case #" + str(i) + ": " + result

