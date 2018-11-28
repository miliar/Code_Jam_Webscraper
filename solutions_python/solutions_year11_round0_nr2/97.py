#!/usr/bin/env python
import sys

if len(sys.argv) != 2:
	print 'Required: Filename'
	exit(2)

f = open(sys.argv[1], 'r')

def solve(cDict, dDict, invoke):

	result = []

	while len(invoke) > 0:

		result.append(invoke[0])
		invoke = invoke[1:]

		if len(result) == 1: continue

		while ''.join(result[-2:]) in cDict:
			tail = result.pop() + result.pop()
			result.append(cDict[tail])

		if result[-1] in dDict:
			bombs = dDict[result[-1]]
			for b in bombs:
				if b in result:
					result = []

	return str(result).replace("'", "")

testCasesTotal = int(f.readline())
testCaseCurrent = 1;

while testCaseCurrent <= testCasesTotal:
	input = f.readline().strip().split()
	cDict, dDict = {}, {}

	c = int(input.pop(0))
	for i in range(c):
		item = input.pop(0)
		cDict[item[0:2]] = item[2]
		cDict[item[1::-1]] = item[2]

	d = int(input.pop(0))
	for i in range(d):
		item = input.pop(0)
		if item[0] in dDict:
			dDict[item[0]].append(item[1])
		else:
			dDict[item[0]] = [item[1]]

		if item[1] in dDict:
			dDict[item[1]].append(item[0])
		else:
			dDict[item[1]] = [item[0]]

	n = int(input.pop(0))
	invoke = input.pop(0)

	print 'Case #%d: %s' % (testCaseCurrent, solve(cDict, dDict, invoke))
	testCaseCurrent += 1;