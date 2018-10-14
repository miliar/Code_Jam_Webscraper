#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import math
import fractions

f_input = open(sys.argv[1])
problems = int(f_input.readline().rstrip())
for probnum in xrange(1, problems+1):
    P, Q = map(int, f_input.readline().rstrip().split("/"))
    gcd = fractions.gcd(P, Q)
    P, Q = P/gcd, Q/gcd
    
    rawmax = math.log(Q, 2)
    #print rawmax, int(rawmax)
    if(int(rawmax)!=rawmax or rawmax>40):
        ans = "impossible"
    else:
        ans = str(int(rawmax) - int(math.log(P, 2)))
    print("Case #%i: %s" % (probnum, ans))

