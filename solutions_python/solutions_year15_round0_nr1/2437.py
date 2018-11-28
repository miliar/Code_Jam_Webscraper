#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solve(testcase):
	num = int(testcase.split()[0])
	numbers = int(testcase.split()[1])
	st = testcase.split()[1]
	ans = 0
	human = 0
	for i in range(0, num+1):
		ith = int(st[i])
		
		if i == 0 and ith == 0:
			ans = ans + 1
			human = human + 1

		if i != 0 and ith != 0:
			if i > human:
				ans = ans + (i - human)
				human = human + (i - human)

		human = human + ith
		#print i, ith, human, ans
	return ans

if __name__ == "__main__":
    testcases = input()
     
    for caseNr in xrange(1, testcases+1):
        cipher = raw_input()
        print("Case #%i: %s" % (caseNr, solve(cipher)))