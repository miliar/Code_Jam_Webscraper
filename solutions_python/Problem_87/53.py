#!/usr/bin/env python3.1

from __future__ import division

import sys
f = sys.stdin
#f = open('in')

def calc(x, s, r, t, lines):
	timer = 0
	diff = r - s
	wws = []
	xrem = x
	for (b, e, w) in lines:
		wws.append([w+s, e-b])
		xrem -= (e-b)
	wws.append([s, xrem])
	wws.sort()
	for i in range(len(wws)):
		(speed, length) = wws[i]
		time = length / (speed + diff)
		runtime = min(time, t)
		t -= runtime
		if runtime == time:
			wws[i][0] += diff
		else:
			wws.append([speed + diff, length * (runtime / time)])
			wws[i][1] -= length * (runtime / time)
			break
	for (speed, length) in wws:
		timer += length / speed
	return timer

def getints():
	return [int(x) for x in f.readline().strip().split(" ")]

numTestCases = getints()[0]
for i in range(numTestCases):
	(x, r, s, t, n) = getints()
	result = calc(x, r, s, t, [getints() for ii in range(n)])
	print("Case #%d: %f" % (i+1, result))
