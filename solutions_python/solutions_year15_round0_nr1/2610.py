#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solve(input):
	ans = 0
	input = input.split()
	levels = input[0]
	guys = input[1]
	n = 0
	for i, c in enumerate(guys):
		if n < i and i > 0:
			ans = ans + (i-n)
			n = n + (i-n)
		n = n + int(c)
	return ans

if __name__ == "__main__":
    testcases = input()
     
    for caseNr in xrange(1, testcases+1):
        cipher = raw_input()
        print("Case #%i: %s" % (caseNr, solve(cipher)))