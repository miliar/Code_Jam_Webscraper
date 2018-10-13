#!/usr/bin/python
import sys
r1 = lambda: sys.stdin.readline()
T = int(r1())
for n in xrange(T):
    a1 = int(r1())
    for i in xrange(4):
        if i == a1-1: 
            c1 = map(int, r1().split())
        else:
            r1()
    a2 = int(r1())
    for i in xrange(4):
        if i == a2-1:
            c2 = map(int, r1().split())
        else:
            r1()
    m = 0
    for i in xrange(4):
        for j in xrange(4):
            if c1[i] == c2[j]:
                m = m+1
                anwser = str(c1[i])

    if m == 0:
        anwser = "Volunteer cheated!"
    elif m > 1:
        anwser = "Bad magician!"
    print "Case #%d: %s" % (n+1, anwser)
