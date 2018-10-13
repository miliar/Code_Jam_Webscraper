from random import random
import math
import re
import fractions


#fileio
fileName = 'A-large'
# fileName = 'A-small-attempt1'
# fileName = 'A-test'
input = fileName + ".in"
output = fileName + ".myout"
MOD = 10**9+7
###
with open(input) as fi, open(output, "w") as fo:
    T = fi.readline()
    for count in xrange(1, int(T)+1):
        r = 0
        arr = []
        D, N = map(int, fi.readline().strip().split())
        for _ in xrange(N):
            arr.append(map(int, fi.readline().strip().split()))
        D = float(D)
        ### code
        def time(x):
            return (D - x[0]) / x[1]
        arrived = max(map(time, arr))
        # print D, arr, arrived
        r = "%.8f" % (D / arrived)
        # r = "%.6f" % round(D / arrived, 6)
        ###
        #normal
        resultStr = "Case #"+str(count)+": "+str(r)
        print resultStr
        fo.write(resultStr+'\n')
