import re
import sys

testExpr = []

input = sys.stdin
(L, D, N) = input.readline().split(' ')

for i in range (0, int(D)):
	testExpr.append(input.readline().strip())
	
for i in range (0, int(N)):
	jmd = re.compile(input.readline().strip().replace('(', '[').replace(')', ']'))
	count = 0
	for sample in testExpr:
		if jmd.match(sample) != None:
			count += 1

	print "Case #%d: %d" % (i+1, count)