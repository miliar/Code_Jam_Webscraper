#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Usage: python run.py < A-small-practice.in > result.txt

def solve(r1, d1, r2, d2):
	B = "Bad magician!"
	C = "Volunteer cheated!"

	i = [v for v in d1[r1-1] if v in d2[r2-1]]

	if (len(i) == 1):
		return i[0]
	elif (len(i) > 1):
		return B
	else:
		return C

testcases = input()
     
for caseNr in xrange(1, testcases+1):
    r1 = int(raw_input())
    d1 = []

    for i in range(0,4):    
    	d1.append(raw_input().split(' '))

    r2 = int(raw_input());
    d2 = []

    for i in range(0,4):    
    	d2.append(raw_input().split(' '))

    print("Case #%i: %s" % (caseNr, solve(r1, d1, r2, d2)))

