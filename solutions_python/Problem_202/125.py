import itertools
import time
import operator
# import collections
from collections import Counter

inputFileName = "test.in"
inputFileName = "D-small-attempt0.in"
# inputFileName = "D-small-attempt1.in"
# inputFileName = "D-small-attempt2.in"
# inputFileName = "D-small-attempt3.in"
# inputFileName = "D-large.in"
outputFileName = inputFileName[:-3] + ".out"

startTime = time.time()
print startTime


def calcSingleTest(f):
    line = f.readline()
    N = int(line.split()[0])
    M = int(line.split()[1])
    mm = []
    R1 = ['.'] * N
    for i in xrange(M):
        line = f.readline()
        mt = line.split()[0]
        r = int(line.split()[1]) - 1
        c = int(line.split()[2]) - 1
        mm.append((mt, r, c))
        R1[c] = mt

    print ''.join(R1)
    ans = []
    sc = 3 * N - 2 if N > 1 else 2
    x2 = -1
    for i in xrange(N - 1):
        if R1[i] == '.':
            ans.append(('+', 1, (i + 1)))
        elif R1[i] == '+':
            pass
        elif R1[i] == 'o':
            x2 = i
        elif R1[i] == 'x':
            ans.append(('o', 1, (i + 1)))
            x2 = i

    if x2 == -1:
        x2 = N - 1
        if R1[N - 1] != 'o':
            ans.append(('o', 1, N))
    else:
        if R1[N - 1] != '+':
            ans.append(('+', 1, N))

    for i in xrange(1, N - 1):
        ans.append(('+', N, (i + 1)))

    for i in xrange(0, x2):
        ans.append(('x', (N - i), (i + 1)))
    for i in xrange(x2 + 1, N):
        ans.append(('x', (i - x2 + 1), (i + 1)))

    strAns = "{0} {1}".format(sc, len(ans))
    for a in ans:
        strAns += "\n{0} {1} {2}".format(a[0], a[1], a[2])
    return strAns


with open(inputFileName) as inpF:
    with open(outputFileName, 'w') as outF:
        line = inpF.readline()
        testsCount = int(line)
        for i in xrange(1, testsCount + 1):
            print '--------  {0}/{1} {2} --------------------------'.format(i, testsCount, (time.time() - startTime))
            r1 = calcSingleTest(inpF)
            print '--------  {0}/{1} {2} --------------------------'.format(i, testsCount, (time.time() - startTime))
            print ' '
            outF.write('Case #{0}: {1}\n'.format(i, r1))
            outF.flush()

print "Finished!!!! Total time = {0}".format((time.time() - startTime))
