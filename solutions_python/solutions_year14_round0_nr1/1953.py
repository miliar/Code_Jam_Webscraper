#!/usr/bin/python
#coding: utf-8

t = int(raw_input())

for case in xrange(1,t+1):
    l1 = set([])
    l2 = set([])
    a = int(raw_input())
    for i in xrange(1,5):
        l = [eval (n) for n in raw_input().strip().split(" ")]
        if (i == a):
            l1 = set(l)
    b = int(raw_input())
    for i in xrange(1,5):
        l = [eval (n) for n in raw_input().strip().split(" ")]
        if (i == b):
            l2 = set(l)
    s = l1.intersection(l2)
    if (len(s) == 1):
        print "Case #%d: %d" % (case,s.pop())
    elif (len(s) == 0):
        print "Case #%d: Volunteer cheated!" % case
    else:
        print "Case #%d: Bad magician!" % case
