#!/usr/bin/python

cases = int(raw_input())
for c in xrange(cases):
    line = raw_input().split()
    goog = int(line[0])
    s = int(line[1])
    p = int(line[2])
    min_score = 3*p - 4
    ans = 0
    for g in xrange(goog):
        d = int(line[3+g])
        if (d < min_score):
            continue
        if (d >= 3*p -2 ):
            ans += 1
            continue
        if (s and d >= p and (d == (3*p - 3) or d == (3*p - 4)) ):
            s -= 1
            ans += 1
            continue
    print "Case #%d: %d" % (c+1,ans)
