import sys
import re
from math import log
from gmpy import ceil
from pprint import pprint

input = sys.stdin
T=int(input.readline())
for i in xrange(1,T+1):
    L,P,C = [int(x) for x in input.readline().split()]
    #print L, P, C
    # if float(P) / L == C:
    #     x = 0
    # else:
    # #x =  ceil(log(log(float(P)/L,C), 2))
    #     x = ceil(log(ceil(log(float(P)/L,2)), C))
    if L*C >= P:
        x = 0
    else:
        x = ceil(log(ceil(log(ceil(float(P)/L),C)), 2))
    print "Case #%s: %s" % (i,int(x))
