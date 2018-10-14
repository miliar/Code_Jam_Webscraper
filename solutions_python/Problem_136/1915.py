#!/usr/bin/python2 -u
# -*- coding: utf-8 -*-
#
import sys, math

### ----- Variables
LINES = []

### ----- Functions
def pop_line():
    global LINES
    if len(LINES) == 0:
        return None
    line = LINES[0]
    LINES = LINES[1:]
    return line

### ----- Program Main
LINES = [line.rstrip() for line in sys.stdin]

T = int(pop_line())
for t in range(T):

    (C,F,X) = map(float, pop_line().split())

    minsec = float("inf")
    numfactory = 0

    while True:
        newsec = 0.0
        for i in range(numfactory):
            newsec += C/(2 + F*i)
        newsec += X/(2 + F*numfactory)

        if newsec < minsec:
            minsec = newsec
            numfactory += 1
        else:
            break

    print 'Case #%d: %.8f' % (t+1, minsec)
