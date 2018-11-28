from random import random
import math
import re
import fractions

#fileio
fileName = 'C-large'
# fileName = 'C-small-2-attempt0'
# fileName = 'C-test'
input = fileName + ".in"
output = fileName + ".out"

###
with open(input) as fi, open(output, "w") as fo:
    count = 0
    for line in fi.readlines()[1:]:
        r = (0, 0)
        # arr = [0]*100
        ### Top-bottom
        N, K = map(int, line.split(" "))
        def rec(i):
            if i == 1:
                t = N
            else:
                mxpo2 = int(math.log(i, 2))
                # accuracy
                if 2 ** (mxpo2+1) <= i:
                    mxpo2 = mxpo2+1
                elif 2 ** mxpo2 <= i:
                    pass
                else:
                    mxpo2 = mxpo2 - 1
                mxpo2 = 2 ** mxpo2
                normi = i - mxpo2
                col = normi / (mxpo2/2)
                if mxpo2/2 == 0:
                    row = 1
                else:
                    row = normi % (mxpo2/2)
                t = rec(row + mxpo2/2)
                # print i, mxpo2, normi, row, col
                # print t
                t = t[col]
            t -= 1
            if t % 2:
                return [t/2+1, t/2]
            else:
                return [t/2, t/2]
        r = rec(K)

        ###
        #normal
        count += 1
        resultStr = "Case #"+str(count)+": "+" ".join(map(str, r))
        print resultStr
        fo.write(resultStr+'\n')
