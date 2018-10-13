#! /usr/bin/python2.6
# coding: utf-8

for t in xrange(1, input()+1):
    a,b = map(int, raw_input().split())
    d = {}
    for n in xrange(a, b):
        s = str(n)
        ms = [int(s[i:] + s[:i]) for i in range(len(s))]
        for m in ms:
            if m != n and  a <= n < m <= b:
                if m not in d:
                    d[m] = set()
                d[m].add(n)
    print 'Case #%d:' % t, sum(len(d[k]) for k in d)
