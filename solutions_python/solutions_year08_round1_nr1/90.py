#!/usr/bin/env python

import sys

def process(case, v1, v2):
	v1.sort()
	v2.sort(reverse = True)

	sum = 0
	for i, a in enumerate(v1):
		sum = sum + a * v2[i]

	print 'Case #%d: %d' % (case, sum)


fp = sys.stdin

n = int(fp.readline())

for case in range(1, n + 1):
	len = int(fp.readline())
	v1 = map(int, fp.readline().split())
	v2 = map(int, fp.readline().split())
	
	process(case, v1, v2)

fp.close()
