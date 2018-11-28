#!/usr/bin/env python

from collections import defaultdict

def process(i, line):
    global v
    global a
    global h
    global d1
    global d2
    for j, c in enumerate(line):
        a[c] += 1
        v[i][c] += 1
        h[j][c] += 1
        d1Idx = 1 + i - j
        if 0 <= d1Idx <= 2:
            d1[d1Idx][c] += 1
        d2Idx = 1 + i + j - 3
        if 0 <= d2Idx <= 2:
            d2[d2Idx][c] += 1

def test(d):
    for c in 'OX':
        if d[c] + d['T'] == 4:
            return c
    return None

def testAll(l):
    for d in l:
        res = test(d)
        if res is not None:
            return res
    return None

def fullTest():
    global v
    global h
    global d1
    global d2
    return testAll(v) or testAll(h) or testAll(d1) or testAll(d2)

if __name__ == '__main__':
    test_count = int(raw_input())
    
    for i in range(1, test_count + 1):
        #print "Case #" + str(i) + ":"
        v  = [defaultdict(lambda: 0) for r in range(4)]
        h  = [defaultdict(lambda: 0) for r in range(4)]
        d1 = [defaultdict(lambda: 0) for r in range(3)]
        d2 = [defaultdict(lambda: 0) for r in range(3)]
        a = defaultdict(lambda: 0)
        for j in range(4):
            line = raw_input().strip()
            #print line
            process(j, line)
        res = fullTest()
        #print v, h, d1, d2
        if i != test_count:
            raw_input()
        if res is not None: print("Case #%d: %c won" % (i, res))
        elif a['.'] > 0: print("Case #%d: Game has not completed" % (i,))
        else: print("Case #%d: Draw" % (i,))
