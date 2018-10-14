#!/usr/bin/env python

import sys


cases = int(sys.stdin.readline())

for i in range(1,cases+1):
	line = sys.stdin.readline()
	(smax , nums ) = line.split()
	answer = 0
	count = 0
	si = 0
	for char in nums:
		count += int(char)
		if char == "0":
			if count <= si:
				answer += 1
				count += 1
		si += 1
	print "Case #%d: %d" % ( i,answer)
		
