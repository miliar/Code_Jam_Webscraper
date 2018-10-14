#!/usr/bin/env python2

T = int(raw_input())

l = set()
for t in xrange(T):
    l.clear()
    stra, strb = raw_input().split()
    a = int(stra)
    b = int(strb)
    size = len(stra)
    for i in xrange(a, b+1):
        stri = str(i)
        for j in xrange(1, size):
            if stri[j] == '0':
                continue
            strj = stri[j:] + stri[:j]
            if stri == strj:
                continue
            intj = int(strj)
            if intj > i and intj <= b:
                l.add((i, intj))
    print("Case #%d: %d" %(t+1, len(l)))

