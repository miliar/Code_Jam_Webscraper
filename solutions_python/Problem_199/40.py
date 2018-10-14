#!/usr/bin/env python2
for t in xrange(1, 1 + int(raw_input())):
    print 'Case #%d:' % t,
    s, k = raw_input().strip().split()
    s = map({'+': True, '-': False}.__getitem__, s)
    k = int(k)
    count = 0
    for i in xrange(len(s) - (k - 1)):
        if s[i] == False:
            s[i:i+k] = [not x for x in s[i:i+k]]
            count += 1
    if all(s):
        print count
    else:
        print 'IMPOSSIBLE'
