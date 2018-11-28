#!/usr/bin/env python2.6

def nextNumber(line):
	lst = list(line)
	if reversedSort(lst):
		zeroCount = lst.count('0')
		for i in range(zeroCount):
			lst.remove('0')
		lst.sort()
		return lst[0] + '0' * (zeroCount + 1) + "".join(lst[1:])
	else:
		brk = -1
		for i in range(1,1+len(lst)):
			if reversedSort(lst[-i:]):
				brk = i
		prev = lst[:-brk-1]
		x = lst[-brk-1]
		nxt = lst[-brk:]
		for i in range(int(x) + 1, 10):
			if nxt.count(str(i)) != 0:
				break
		newx = str(i)
		nxt.remove(newx)
		nxt.append(x)
		nxt.sort()
		return "".join(prev) + newx + "".join(nxt)

def reversedSort(lst):
	lst2 = lst[:]
	lst2.sort()
	lst2.reverse()
	return lst == lst2


import sys
lines = sys.stdin.read().split("\n")
numTestCases = int(lines[0])
lines = lines[1:]

for testCase in range(numTestCases):
	line = lines[testCase]
	output = nextNumber(line)
	print "Case #" + str(testCase + 1) + ": " + str(output)
