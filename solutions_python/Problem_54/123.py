#!/usr/bin/env python

import sys

def GCD(l):
    while len(l) > 1:
	if l[0] < l[1]:
	    l[1] = l[0] - (l[1] % l[0])
	elif l[0] > l[1]:
	    l[0] = l[1] - (l[0] % l[1])
	else:
	    del l[0]
    return l[0]

filename=sys.argv[1]
inputfile=file(filename, 'r')
numcases=int(inputfile.readline().strip())
for case in range(1,numcases+1):
    t = map(long, inputfile.readline().strip().split())
    # t[0] = N
    del t[0]
    t.sort()

    d = []
    i = 0
    for j in range(1, len(t)):
	if t[j] > t[i]:
	    d.append(t[j] - t[i])
	    i = j

    T = GCD(d)
    x = t[0] % T
    if x == 0:
	y = 0
    else:
	y = T - x

    print "Case #%d: %d" % (case, y)
