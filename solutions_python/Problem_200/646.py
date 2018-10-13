#!/bin/python

def findFirstUntidyPos(nstr):
    n = len(nstr)
    if n == 1:
        return 1
    prev = nstr[0]
    i = 1
    while i < n:
        d = nstr[i]
        if prev <= d:
            i = i + 1
            prev = d
        else:
            return i
    return i

def maxTidy(limit):
    n = len(limit)
    if n == 1:
        return limit
    result = bytearray(n)
    p = findFirstUntidyPos(limit)
    if p == n:
        return limit
    else:
        for i in xrange(p, n):
            result[i] = '9'
        i = p-1
        if i > 0:
            d = limit[i]
            i = i - 1
            while i >= 0:
                nd = limit[i]
                if d > nd:
                    result[i+1] = str(int(d)-1)
                    result[:i+1] = limit[:i+1]
                    return str(result)
                else:
                    result[i+1] = '9'
                    i = i -1
                    d = nd
        fd = limit[0]
        if fd > '1':
            result[0] = str(int(fd) - 1)
            return str(result)
        else:
            return str(result[1:])

t = int(raw_input().strip())
for i in xrange(1, t+1):
    n = raw_input().strip()
    v = maxTidy(n)
    print "Case #%d: %s" % (i, v)
