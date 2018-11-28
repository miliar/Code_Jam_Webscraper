#!/usr/bin/env python
# -*- coding: utf-8 -*-
def solve(data):
	[x,r,c] = data.split(" ")
	x = int(x)	
	r = int(r)	
	c = int(c)
	square = r * c
	if x >= 7:
		return 'RICHARD'
	if square % x != 0:
		return 'RICHARD'
	if x > max(r,c):
		return 'RICHARD'
	if (square / x) < 3 and x > 3:
		return 'RICHARD'
	dim = {1: 1, 2: 1, 3: 2, 4: 2, 5: 3, 6: 3}
	if dim[x] > min(r,c):
		return 'RICHARD'
	return 'GABRIEL'
	
if __name__ == "__main__":
    testcases = input()
     
    for caseNr in xrange(1, testcases+1):
        data = raw_input()
        print("Case #%i: %s" % (caseNr, solve(data)))