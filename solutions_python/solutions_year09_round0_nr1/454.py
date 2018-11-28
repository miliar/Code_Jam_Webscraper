#!/usr/bin/env python

import sys
import re

(L, D, N) = map(int, sys.stdin.readline().split())
words = []
for i in range(1, D+1):
	words.append(sys.stdin.readline().strip())

for i in range(1, N+1):
	pattern = sys.stdin.readline().strip()
	pattern = re.sub('\(', '[', pattern)
	pattern = re.sub('\)', ']', pattern)
	count = 0
	for w in words:
		if re.match(pattern, w):
			count = count + 1
	print "Case #%s: %s" % (i, count)
