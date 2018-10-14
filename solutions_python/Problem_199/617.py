#!/bin/python


def countOps(bits, k):
    def applyFlips(flips, i):
        for j in xrange(i, i + k):
            flips[j] += 1
    
    n = len(bits)
    flips = [0] * (n + k -1)
    count = 0
    for i,b in enumerate(bits):
        if (b + flips[i]) % 2 == 1:
            applyFlips(flips, i)
            count += 1
    if flips[n] > 0:
        return -1
    else:
        return count

def strToBits(s):
    return map(lambda c: 1 if c == '-' else 0, s)

t = int(raw_input().strip())

for i in xrange(1, t+1):
    s, k = raw_input().strip().split(' ')
    k = int(k)
    c = countOps(strToBits(s), k)
    if c >= 0:
        print "Case #%d: %d" % (i, c)
    else:
        print "Case #%d: IMPOSSIBLE" % i
