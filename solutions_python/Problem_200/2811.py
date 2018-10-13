#!/usr/bin/env python3

import sys

def solveNum(line):
	num = list(map(int, list(line)))
	if len(line) == 1:
		return line
	sol = ""
	for i in range(len(num)-1):
		if num[i] <= num[i+1]:
			sol += str(num[i])
		else:
			sol += str(num[i]-1)
			sol += "9" * (len(num)-i-1)
			return solveNum(sol)
	sol += str(num[-1])
	return sol

def solve(line, t):
	sol = solveNum(line).lstrip("0")
	print("Case #%d: %s" % (t, sol))


lines = [ l.strip() for l in sys.stdin.readlines() ]

T = int(lines[0])

for i in range(T):
	solve(lines[i+1], i+1)
