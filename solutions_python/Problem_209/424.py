import sys
from fractions import gcd
import numpy as np
import math

lines = open(sys.argv[1]).readlines()

T = int(lines[0])

casenum = 0

pos = 1

while pos < len(lines):
    casenum += 1
    vals = lines[pos].split()
    pos += 1
    N = int(vals[0])
    K = int(vals[1])

    RH = []
    for i in xrange(N):
        vals = lines[pos].split()
        pos += 1
        RH.append([int(vals[0]),int(vals[1])])

    RH = sorted(RH,reverse=True)

    best = 0
    for s in xrange(0,len(RH)-K+1):
        
        Rcont = RH[s][0] * RH[s][0] * math.pi + 2 * math.pi * RH[s][0] * RH[s][1]
        V = [2 * math.pi * RH[i][0] * RH[i][1] for i in xrange(s+1,N)]
        V = sorted(V, reverse=True)
        Vcont = sum(V[:K-1])
        if (Rcont + Vcont > best):
            best = Rcont + Vcont

            
    print 'case #' + str(casenum) + ": ", best

    



        
