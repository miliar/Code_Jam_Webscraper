#!/usr/bin/env python

import sys
import itertools


def solve(FL, SL):
    t = 0
    fSet = set(map(lambda i: int(i), FL.strip().split(" ")))
    sSet = set(map(lambda i: int(i), SL.strip().split(" ")))
    cap = fSet.intersection(sSet)
    if len(cap) == 1:
        return cap.pop()
    elif len(cap) > 1:
        return "Bad magician!"
    elif len(cap) < 1:
        return "Volunteer cheated!"


filename = sys.argv[1]

inp = open(filename.strip())
lines = inp.readlines()

i = 1
body = iter(lines[1:])
for line in body:
    (FA,) = map(lambda i: int(i), line.strip().split(" "))
    FL = ""
    for j in range(4):
        l = body.next()
        if (j + 1)  == FA:
            FL = l.strip()
    line = body.next()
    (SA,) = map(lambda i: int(i), line.strip().split(" "))
    SL = ""
    for j in range(4):
        l = body.next()
        if (j + 1)  == SA:
            SL = l.strip()
    print "Case #%d: %s" % (i, solve(FL, SL))
    i += 1

