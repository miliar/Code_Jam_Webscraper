#!/usr/bin/python2.6

import os, sys, math

def fun(a, b, c):
    if a * c >= b:
        return 0
    else:
        a = float(a)
        b = float(b)
        la = math.log(a)/math.log(float(c))
        lb = math.log(b)/math.log(float(c))
        ld = (la+lb)/2
        ld = ld * math.log(float(c))
        d = math.exp(ld)
        dd = math.floor(d)
        if (d - dd) > 0.5:
            dd = dd+1
        return max(fun(a,dd,c),fun(dd, b, c))+1


file = open(sys.argv[1] , 'r')
nbr_testcases = int(file.readline())

for test in range(nbr_testcases):
    L, P, C = tuple([int(k) for k in file.readline().split()])
    attempt = fun(L,P,C)
    print "Case #"+str(test+1)+": "+str(attempt)

file.close()
