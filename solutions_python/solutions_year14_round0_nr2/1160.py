import itertools
import time
import operator
#import collections
from collections import Counter

#inputFileName = "test.in"
#inputFileName = "B-small-attempt0.in"
#inputFileName = "B-small-attempt1.in"
#inputFileName = "B-small-attempt2.in"
#inputFileName = "B-small-attempt3.in"
inputFileName = "B-large.in"
outputFileName = inputFileName[:-3] + ".out"

startTime = time.time()
print startTime


def calcSingleTest(f):
    line = f.readline()
    C0 = float(line.split()[0])
    F0 = float(line.split()[1])
    X0 = float(line.split()[2])
    S0 = 2

    #    k = 100000
    k = 1
    C = C0 * k
    F = F0 * k
    X = X0 * k
    S = S0 * k
    tf = C / F

    cs = S
    tt = 0
    et = (X - C) / cs
    while et > tf:
        tt += C / cs
        cs += F
        et = (X - C) / cs
    et0 = X / cs
    return et0 + tt


with open(inputFileName) as inpF:
    with open(outputFileName, 'w') as outF:
        line = inpF.readline()
        testsCount = int(line)
        for i in xrange(1, testsCount + 1):
            print '--------  {0}/{1} {2} --------------------------'.format(i, testsCount, (time.time() - startTime))
            res = calcSingleTest(inpF)
            print '--------  {0}/{1} {2} --------------------------'.format(i, testsCount, (time.time() - startTime))
            print ' '
            outF.write('Case #{0}: {1}\n'.format(i, res))
            outF.flush()

print "Finished!!!! Total time = {0}".format((time.time() - startTime))