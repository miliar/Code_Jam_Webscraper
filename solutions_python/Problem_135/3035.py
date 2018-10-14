#! /usr/bin/env python

T = int(raw_input())
t = 1
while t <= T:
    a = int(raw_input())
    i = 0
    while i < a-1:
        raw_input()
        i += 1
    r1 = set(raw_input().split(" "))
    while i < 3:
        raw_input()
        i += 1

    a = int(raw_input())
    i = 0
    while i < a-1:
        raw_input()
        i += 1
    r2 = set(raw_input().split(" "))
    c = r1.intersection(r2)
    lc = len(c)
    if lc == 1:
        print "Case #%s: %s"%(t, c.pop())
    elif lc == 0:
        print "Case #%s: Volunteer cheated!" % t
    else:
        print "Case #%s: Bad magician!" % t
    while i < 3:
        raw_input()
        i += 1
    t += 1
