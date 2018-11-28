from random import random
import math
import re
import fractions


#fileio
fileName = 'A-large'
# fileName = 'A-small-attempt0'
# fileName = 'A-test'
input = fileName + ".in"
output = fileName + ".out"
MOD = 10**9+7
###
with open(input) as fi, open(output, "w") as fo:
    count = 0
    for line in fi.readlines()[1:]:
        r = 0
        ### code
        S, K = line.split(" ")
        K = int(K)
        S = map(lambda x: x == "+", "+"+S)
        f = [False] * len(S)
        current = False
        for i, s in enumerate(S):
            if f[i]:
                current = not current
            if not current ^ s:
                current = not current
                r += 1
                if i + K - 1 >= len(S):
                    r = "IMPOSSIBLE"
                    break
                if i + K < len(S):
                    f[i + K] = True
        ###
        #normal
        count += 1
        resultStr = "Case #"+str(count)+": "+str(r)
        print resultStr
        fo.write(resultStr+'\n')
