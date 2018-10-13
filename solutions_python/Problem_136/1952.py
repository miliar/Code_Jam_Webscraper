#!/usr/bin/env python
import sys
from optparse import OptionParser
from collections import deque
usage = "usage: %prog input"
parser = OptionParser(usage=usage)
(options, args) = parser.parse_args()
if args:
    if args[0] == "-":
        f = sys.stdin
    else:
        f = open(args[0])
else:
    parser.error("Need input from file or stdin")

T = int(f.readline())

def buy_is_better():
    return X / (production + F) < (X - cookies) / production

for t in range(1, T+1):
    (C, F, X) = [float(x) for x in f.readline().split()]
    cookies = 0
    time = 0
    production = 2
    while cookies < X:
	addition = min(C, X)
	cookies += addition
	time = time + addition / production
        if buy_is_better():
	    cookies = 0
            production += F
	else:
            time += (X - cookies) / production
            cookies = X
    print 'Case #%s: %s' % (t, round(time, 7))

