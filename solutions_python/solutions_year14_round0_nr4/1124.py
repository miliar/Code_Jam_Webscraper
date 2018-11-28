import itertools
import time
import operator
#import collections
from collections import Counter

#inputFileName = "test.in"
#inputFileName = "D-small-attempt0.in"
#inputFileName = "D-small-attempt1.in"
#inputFileName = "D-small-attempt2.in"
#inputFileName = "D-small-attempt3.in"
inputFileName = "D-large.in"
outputFileName = inputFileName[:-3] + ".out"

startTime = time.time()
print startTime

def calc(p1, p2):
    n = len(p1)
    i1 = 0
    i2 = 0
    cnt = 0
    while i1 < n and i2 < n:
        if p1[i1] > p2[i2]:
            i1 += 1
            i2 += 1
            cnt += 1
        else:
            i2 += 1
    return cnt


def calcSingleTest(f):
    line = f.readline()
    N = int(line)
    line = f.readline()
    p1 = map(float, line.split())
    line = f.readline()
    p2 = map(float, line.split())
    p1.sort(reverse=True)
    p2.sort(reverse=True)
    print p1
    print p2
    w1 = calc(p1, p2)
    w2 = N - calc(p2, p1)

    return (w1, w2)

with open(inputFileName) as inpF:
    with open(outputFileName, 'w') as outF:
        line = inpF.readline()
        testsCount = int(line)
        for i in xrange(1, testsCount + 1):
            print '--------  {0}/{1} {2} --------------------------'.format(i, testsCount, (time.time() - startTime))
            r1, r2 = calcSingleTest(inpF)
            print '--------  {0}/{1} {2} --------------------------'.format(i, testsCount, (time.time() - startTime))
            print ' '
            outF.write('Case #{0}: {1} {2}\n'.format(i, r1, r2))
            outF.flush()

print "Finished!!!! Total time = {0}".format((time.time() - startTime))