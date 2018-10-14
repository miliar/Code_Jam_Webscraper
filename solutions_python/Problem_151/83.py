import itertools
import random
import time
import operator
#import collections
from collections import Counter

#inputFileName = "test.in"
#inputFileName = "C-small-practice.in"
inputFileName = "D-small-attempt0.in"
#inputFileName = "C-small-attempt1.in"
#inputFileName = "C-small-attempt2.in"
#inputFileName = "C-small-attempt3.in"
#inputFileName = "C-large.in"
outputFileName = inputFileName[:-3] + ".out"

startTime = time.time()
print startTime

MOD = 1000000007

def make_trie(words):
    root = dict()
    cnt = 1
    for word in words:
        current_dict = root
        for letter in word:
            if not letter in current_dict:
                cnt += 1
            current_dict = current_dict.setdefault(letter, {})
    return root, cnt

cache = dict()

def calc_trie_size(words):
    merged = "|".join(words)
    if merged in cache:
        return cache[merged]
    else:
        t, c = make_trie(words)
        cache[merged] = c
        return c


def calcSingleTest(f):
    line = f.readline()
    M = int(line.split()[0])
    N = int(line.split()[1])
    w = []
    for i in xrange(M):
        line = f.readline()
        if line[-1] == '\n':
            line = line[:-1]
        w.append(line)
    print w
    t, c = make_trie(w)
    print t
    print c

    r = pow(N, M)
    print r
    max = -1
    max_cnt = 0
    for allp in xrange(r):
        w_a = []
        for i in xrange(N):
            w_a.append([])
        tmp = allp
        for i in xrange(M):
            p = tmp % N
            tmp /= N
            w_a[p].append(w[i])
        all_nonempty = True
        s = 0
        for i in xrange(N):
            if len(w_a[i]) == 0:
                all_nonempty = False
                break
            s += calc_trie_size(w_a[i])
        if not all_nonempty:
            continue

        if max < s:
            max = s
            max_cnt = 1
        elif max == s:
            max_cnt += 1
    return (max, max_cnt)

with open(inputFileName) as inpF:
    random.seed(0)
    with open(outputFileName, 'w') as outF:
        line = inpF.readline()
        testsCount = int(line)
        for i in xrange(1, testsCount + 1):
            print '--------  {0}/{1} {2} --------------------------'.format(i, testsCount, (time.time() - startTime))
            res, res_cnt = calcSingleTest(inpF)
            print '--------  {0}/{1} {2} --------------------------'.format(i, testsCount, (time.time() - startTime))
            print ' '
            outF.write('Case #{0}: {1} {2}\n'.format(i, res, res_cnt))
            outF.flush()

print "Finished!!!! Total time = {0}".format((time.time() - startTime))