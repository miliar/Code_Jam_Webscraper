#!/usr/bin/python

import sys
import resource
import math
from Queue import Queue

def isTidy(N):
    last_c = '-'
    for c in str(N):
        if c < last_c:
            return False
        last_c = c
    return True
    
def tidy(N):
    if N < 10 or isTidy(N):
        return N
    return int(str(tidy(int(str(N)[:-1])-1)) + '9')
    
    
t = int(raw_input())  # read a line with a single integer
for case in xrange(1, t + 1):
    print "Case #{}: {}".format(case, tidy(int(raw_input())))
    


