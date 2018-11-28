import itertools
import time
import operator
# import collections
from collections import Counter
from collections import OrderedDict

inputFileName = "test.in"
# inputFileName = "B-small-attempt0.in"
# inputFileName = "B-small-attempt1.in"
# inputFileName = "B-small-attempt2.in"
# inputFileName = "B-small-attempt3.in"
inputFileName = "B-large.in"
outputFileName = inputFileName[:-3] + ".out"

startTime = time.time()
print startTime


def isTidy(n):
    s = str(n)
    ch = s[0]

    for i in xrange(1, len(s)):
        nCh = s[i]
        if (nCh < ch):
            return False
        ch = nCh
    return True


def findTidyDumb(n):
    for x in xrange(n, 0, -1):
        if isTidy(x):
            return x
    return 0


def findTidySmart(n):
    s = str(n)
    res = 0
    p10 = 1
    d = int(s[len(s) - 1])
    for i in xrange(len(s) - 2, -1, -1):
        nD = int(s[i])
        if nD > d:
            d = 9
            nD -= 1
            res = 10 * p10 - 1
        else:
            res += int(d) * p10
        d = nD
        p10 *= 10
    res += int(d) * p10
    return res


def calcSingleTest(f):
    line = f.readline()
    N = int(line)

    smart = findTidySmart(N)
    if (N < 10000):
        dumb = findTidyDumb(N)
        if dumb != smart:
            raise AssertionError("N = {0}, smart = {1}, dumb = {2}".format(N, smart, dumb))

    return smart


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

if 1 == 0:
    for N in xrange(1, 1000000):
        smart = findTidySmart(N)
        dumb = findTidyDumb(N)
        if N % 1000 == 0:
            print "Progress = {0}".format(N)
        if dumb != smart:
            raise AssertionError("N = {0}, smart = {1}, dumb = {2}".format(N, smart, dumb))
