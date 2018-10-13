#!/usr/bin/env python
# -*- coding: utf-8 -*-


def solve(smax , p ):
	level = 0
	needed = 0
	standing = 0
	for x in p:
		if (int(x) > 0):
			if(standing >= level ): 
				standing += int(x)
			else: 
				needed += (level- standing)
				standing = standing + int(x) + (level - standing)
		level += 1

	return needed





























if __name__ == "__main__":
	testcases = input()
	for caseNr in xrange(1, testcases+1):
		smax, p = raw_input().split()
		smax = int(smax)
		print("Case #%i: %s" % (caseNr, solve(smax, p)))
