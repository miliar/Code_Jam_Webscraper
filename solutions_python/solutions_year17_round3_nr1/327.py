from random import random
import math
import re
import fractions
from decimal import *
# getcontext().prec = 9
# PI = 3.141592653589793238462643383279502884197169399375105820974944592307816406286

#fileio
fileName = 'A-large'
# fileName = 'A-small-attempt2'
# fileName = 'A-test'
input = fileName + ".in"
output = fileName + ".myout"
MOD = 10**9+7
###
with open(input) as fi, open(output, "w") as fo:
    T = fi.readline()
    for count in xrange(int(T)):
        # r = Decimal(0)
        r = 0
        arr = []
        d = {}
        mxb = (0, 0)
        N, K = map(int, fi.readline().strip().split())
        for i in xrange(N):
            rr, h = map(int, fi.readline().strip().split())
            arr.append((2 * rr * h, i, rr * rr))
        sarr = sorted(arr)
        topK = sarr[-K:]
        minTopK = sarr[-K]
        s = set(map(lambda x: x[1], topK))
        sumH = sum(map(lambda x: x[0], topK))
        mxr = 0
        for i in xrange(N):
            if i in s:
                mxr = max(mxr, sumH + arr[i][2])
            else:
                mxr = max(mxr, sumH - minTopK[0] + arr[i][0] + arr[i][2])
        # print mxb, arr, mxr
        r = Decimal(math.pi) * Decimal(mxr)
        # print r


        ###
        #normal
        resultStr = "Case #"+str(count+1)+": "+str(r)
        print resultStr
        fo.write(resultStr+'\n')
