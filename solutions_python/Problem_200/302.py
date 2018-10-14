from random import random
import math
import re
import fractions


# fileio
fileName = 'B-large'
# fileName = 'B-small-attempt0'
# fileName = 'B-test'
input = fileName + ".in"
output = fileName + ".out"

###
with open(input) as fi, open(output, "w") as fo:
    count = 0
    for line in fi.readlines()[1:]:
        # arr = [0]*100
        ###
        K = int(line)
        N = len(str(K))
        r = ""
        mask = 1
        ninesi = -1
        for i in xrange(N-1, -1, -1):
            right = (K / mask) % 10
            mask *= 10
            left = (K / mask) % 10
            if left > right:
                K -= mask
                ninesi = i
            else:
                r += str(right)
        if ninesi > -1:
            r = r[::-1][:ninesi] + "9" * (N - ninesi)
        else:
            r = r[::-1]
        if not r: r = "0"
        ###
        #normal
        count += 1
        resultStr = "Case #"+str(count)+": "+str(int(r))
        print resultStr
        fo.write(resultStr+'\n')
