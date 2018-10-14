import itertools
import time
import operator
# import collections
from collections import Counter
from fractions import gcd
from random import randint
import random

# inputFileName = "test.in"
# inputFileName = "A-small-attempt0.in"
# inputFileName = "A-small-attempt1.in"
# inputFileName = "A-small-attempt2.in"
# inputFileName = "A-small-attempt3.in"
inputFileName = "A-large.in"
outputFileName = inputFileName[:-3] + ".out"

startTime = time.time()
print startTime


def calcSingleTest(f):
    line = f.readline()
    N = int(line.split()[0])
    P = int(line.split()[1])
    line = f.readline()
    g = map(int, line.split())
    m = map(lambda x: x % P, g)
    c = Counter(m)
    res = c[0]
    if (P == 2):
        res += (c[1] + 1) / 2
    elif (P == 3):
        c1 = c[1]
        c2 = c[2]
        mi = min(c1, c2)
        ma = max(c1, c2)
        res += mi + (ma - mi + 2) / 3
    elif (P == 4):
        print c

        c1 = c[1]
        c2 = c[2]
        c3 = c[3]
        res += c2 / 2
        c2 = c2 % 2
        mi = min(c1, c3)
        res += mi
        c1 -= mi
        c3 -= mi
        ma = max(c1, c3)
        if (c2 != 0):
            res += 1
            res += (ma + 1) / 4
        else:
            res += (ma + 3) / 4

        print res
    else:
        raise AssertionError("AAAA " + str(N))

    return res


with open(inputFileName) as inpF:
    with open(outputFileName, 'w') as outF:
        line = inpF.readline()
        testsCount = int(line)
        for i in xrange(1, testsCount + 1):
            print '--------------------------------------------'
            res = calcSingleTest(inpF)
            outF.write('Case #{0}: {1}\n'.format(i, res))

print "Finished!!!! Total time = {0}".format((time.time() - startTime))
