#!/usr/bin/python
import sys

if len(sys.argv) != 2:
	print 'Required: Filename'
	exit(2)

f = open(sys.argv[1], 'r')

def solve(n, values):

	xor = 0
	for i in values:
		xor = xor ^ i
	if xor != 0:
		return 'NO'

	values.remove(min(values))
	return sum(values)

testCasesTotal = int(f.readline())
testCaseCurrent = 1;

while testCaseCurrent <= testCasesTotal:
	n = int(f.readline().strip())
	input = map(int, f.readline().strip().split(' '))
	print 'Case #%d:' % testCaseCurrent, solve(n, input);
	testCaseCurrent += 1;