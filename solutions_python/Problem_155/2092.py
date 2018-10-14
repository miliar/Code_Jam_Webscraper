#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solve(str):
	strParts = str.split()
	maxShyness = strParts[0]
	audience = strParts[1]

	count = 0
	k = 0
	friends = 0
	for c in audience:
		while count < k:
			friends = friends + 1
			count = count + 1

		count = count + int(c)
		k = k + 1

	return friends

if __name__ == "__main__":
    testcases = input()
     
    for caseNr in xrange(1, testcases+1):
        caseToSolve = raw_input()
        print("Case #%i: %s" % (caseNr, solve(caseToSolve)))