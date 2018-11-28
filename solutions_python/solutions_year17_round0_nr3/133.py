import itertools
import time
import operator
# import collections
from collections import Counter
from itertools import repeat
import bisect

inputFileName = "test.in"

# inputFileName = "C-small-1-attempt0.in"
# inputFileName = "C-small-1-attempt1.in"

# inputFileName = "C-small-2-attempt0.in"

# inputFileName = "C-small-attempt0.in"
# inputFileName = "C-small-attempt1.in"
# inputFileName = "C-small-attempt2.in"

# inputFileName = "C-small-attempt3.in"
# inputFileName = "C-small-attempt4.in"

inputFileName = "C-large.in"
outputFileName = inputFileName[:-3] + ".out"

startTime = time.time()
print startTime


def dumb(N, K):
    BIG_VALUE = 2 * 10 ** 18
    st = [0] * (N + 1)
    st[-1] = 1
    ll = [-1] * N
    rr = [N] * N
    mm = [(-1, -1)] * N

    for i in xrange(0, N):
        l = i - ll[i] - 1
        r = rr[i] - i - 1
        mm[i] = (max(l, r), min(l, r))

    answers = []

    bestI = 0
    dbgCnt = 0
    last_dbgCnt = 0
    last_time = startTime
    lastBestI = N + 1
    lastBest = (-1, -1)
    for k in xrange(K):
        foundSame = False

        for i in xrange(lastBestI + 1, N):
            cur = mm[i]
            if st[i] == 1:
                continue
            if cur == lastBest:
                bestI = i
                foundSame = True
                break

        if not foundSame:
            bestI = 0
            best = (-1, -1)
            for i in xrange(N):
                cur = mm[i]
                if st[i] == 1:
                    continue
                if (cur[1] > best[1]) or (cur[1] == best[1] and cur[0] > best[0]):
                    bestI = i
                    best = cur

        st[bestI] = 1

        answers.append((k + 1, bestI + 1, best[0], best[1]))
        for i in xrange(bestI + 1, N):
            if ll[i] < bestI:
                dbgCnt += 1
                ll[i] = bestI
                l = i - ll[i] - 1
                r = rr[i] - i - 1
                mm[i] = (max(l, r), min(l, r))
            else:
                break

        for i in xrange(bestI - 1, -1, -1):
            if rr[i] > bestI:
                dbgCnt += 1
                rr[i] = bestI
                l = i - ll[i] - 1
                r = rr[i] - i - 1
                mm[i] = (max(l, r), min(l, r))
            else:
                break
        pass
        lastBestI = bestI
        lastBest = best
        if (1 == 0) and (((k % 100 == 0) and k < 1000) or (k % 5000 == 0)):
            curTime = time.time()
            print "{0:06.2f} / {7:04.2f}: k = {1:05d}, dbgCnt = {2:08d} {3:.3f} {4:.3f} {5:.5f} {6:05d}, best = {8}".format(
                (curTime - startTime), k, dbgCnt,
                float(dbgCnt) / (k + 1), float(dbgCnt) / N,
                float(dbgCnt) / (k + 1) / N,
                (dbgCnt - last_dbgCnt),
                (curTime - last_time),
                best)
            last_dbgCnt = dbgCnt
            last_time = curTime

    # bestI = 0
    # best = mm[bestI]
    # for i in xrange(1, N):
    #     cur = mm[i]
    #     if (cur[1] > best[1]) or (cur[1] == best[1] and cur[0] > best[0]):
    #         bestI = i
    #         best = cur

    # print "\n".join(map(str, answers))

    return mm[bestI]


def smart(N, K):
    qi = [N]
    q = dict()
    q[N] = 1

    k = K
    while k > 0:

        s = qi.pop(-1)
        c = q[s]
        if c < k:
            k -= c
            s1 = (s - 1) / 2
            s2 = s / 2
            if s1 not in q:
                bisect.insort(qi, s1)
                q[s1] = c
            else:
                q[s1] += c

            if s2 not in q:
                bisect.insort(qi, s2)
                q[s2] = c
            else:
                q[s2] += c
        else:
            return (s / 2, (s - 1) / 2)

    return (-1, -1)


def calcSingleTest(f):
    line = f.readline()
    N = int(line.split()[0])
    K = int(line.split()[1])

    if K > N / 2 + 1 and 1 == 0:
        x, y = (0, 0)
    else:
        x, y = r2 = smart(N, K)
        # r1 = dumb(N, K)
        # if r2 != r1:
        #     raise AssertionError("N = {0}, K = {1}, dumb = {2}, smart = {3}".format(N, K, r1, r2))
    return "{0} {1}".format(x, y)


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
