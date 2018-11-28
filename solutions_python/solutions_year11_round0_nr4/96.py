#!/usr/bin/python
import sys

if len(sys.argv) != 2:
	print 'Required: Filename'
	exit(2)

f = open(sys.argv[1], 'r')

def solve(n, values):

	result = 0
	i = 1
	while i <= n:
		if i != values[i - 1]:
			result += 1
		i += 1

	return result

testCasesTotal = int(f.readline())
testCaseCurrent = 1;

while testCaseCurrent <= testCasesTotal:
	n = int(f.readline().strip())
	input = map(int, f.readline().strip().split())
	print 'Case #%d: %.6f' % (testCaseCurrent, solve(n, input));
	testCaseCurrent += 1;