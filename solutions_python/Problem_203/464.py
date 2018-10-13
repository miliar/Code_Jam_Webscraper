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
    T = fi.readline()[0]
    T = 100
    print T
    for count in xrange(int(T)):
        r = 0
        ### code
        arr = []
        h, w = map(int, fi.readline().strip().split())
        for _ in xrange(h):
            arr.append(list(fi.readline().strip()))
        for j in xrange(h):
            for i in xrange(1, w):
                if arr[j][i] == "?":
                    arr[j][i] = arr[j][i-1]
            for i in xrange(w-2, -1, -1):
                if arr[j][i] == "?":
                    arr[j][i] = arr[j][i+1]
        for i in xrange(w):
            for j in xrange(1, h):
                if arr[j][i] == "?":
                    arr[j][i] = arr[j-1][i]
            for j in xrange(h-2, -1, -1):
                if arr[j][i] == "?":
                    arr[j][i] = arr[j+1][i]
        arr = "\n".join(map(lambda x: "".join(x), arr))
        ###
        #normal
        count += 1
        resultStr = "Case #"+str(count)+": \n"+str(arr)
        print resultStr
        fo.write(resultStr+'\n')
