#!/usr/bin/env python

import sys, math

def gensquares (start, end):
	sqstart = int (math.ceil (math.sqrt (start)))
	sqend = int (math.floor (math.sqrt (end)))

	for n in range (sqstart, sqend+1):
		yield n


def ispali (n):
	s = str (n)
	return s == s[::-1]


def solve (casenum, start, end):
	result = 0
	for n in gensquares (start, end):
		if ispali (n) and ispali (n*n):
			result += 1

	print "Case #%d: %s" % (casenum, result)


num_testcases = int (sys.stdin.readline())

for case in range (1, num_testcases+1):
	(start, end) = map (int, sys.stdin.readline().split())

	solve (case, start, end)
