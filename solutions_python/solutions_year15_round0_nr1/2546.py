#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import string

def solve(cipher):
	pat = re.compile("[ ]")
	field = pat.split(cipher)
	n = int(field[0])
	s = field[1]
	leave = 0
	result = 0
	for i in xrange(0, n + 1):
		if (leave < i):
			result = result + 1
			leave = leave + 1
		leave += int(s[i])
	return result

if __name__ == "__main__":
	testcases = input()

	for caseNr in xrange(1, testcases+1):
		cipher = raw_input()
		print("Case #%i: %s" % (caseNr, solve(cipher)))
