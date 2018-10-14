#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import sys


def judge(N, K):
#	print "N:" + str(N)
#	print "K:" + str(K)
	return ((K + 1) % (2**N)) == 0

casenum = int(sys.stdin.readline().rstrip())
testcases = []

for line in sys.stdin.readlines():
	line = line.rstrip()
	testcases.append(line)

for testnum in range(casenum):
#	print testcases[testnum]
	case = testcases[testnum].split()
	if(judge(int(case[0]), int(case[1]))):
		print "Case #"+str(testnum+1)+": ON"
	else:
		print "Case #"+str(testnum+1)+": OFF"

