#!/usr/bin/env python3.1

import sys

def calc():
	line = sys.stdin.readline().strip().split(" ")
	a = line[1:1+int(line[0])]
	p = 2 + len(a)
	b = line[p:p+int(line[p-1])]
	inp = list(line[-1])
	combine = {}
	for r in a:
		combine[r[0]+r[1]] = r[2]
		combine[r[1]+r[0]] = r[2]
	oppose = {}
	for r in ["Q", "W", "E", "R", "A", "S", "D", "F"]:
		oppose[r] = []
	for r in b:
		oppose[r[0]].append(r[1])
		oppose[r[1]].append(r[0])
	
	stack = []
	while len(inp) > 0:
		new = (stack.pop() if stack else '') + inp.pop(0)
		stack += list(combine.get(new, new))
		for o in oppose.get(stack[-1], []):
			if o in stack:
				stack[:] = []
				break
	return str(stack).replace("'", '')

numTestCases = int(sys.stdin.readline())
for i in range(numTestCases):
	result = calc()
	print("Case #%d: %s" % (i+1, result))
