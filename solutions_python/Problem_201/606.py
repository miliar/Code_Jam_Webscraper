#!/usr/bin/python3

def calculate(n, depth, nMaxs, nMins):
	if depth == 1: return (n, nMaxs)

	if n%2 == 0: return calculate(n//2, depth - 1, nMaxs, nMins * 2 + nMaxs)
	return calculate(n//2, depth - 1, nMaxs * 2 + nMins, nMins)

t = int(input())

for testcase in range(t): 
	(n, k) = map(int, input().split())
	depth = len(bin(k)) - 2
	(maxParent, nMaxs) = calculate(n, depth, 1, 0)
	leafID = k - 2**(depth-1) + 1
	if leafID > nMaxs: 
		maxParent -= 1

	maxDist = max(maxParent//2, 0)
	minDist = max(maxParent//2 + (maxParent%2 - 1), 0)
	print("Case #{}: {} {}".format(testcase+1, maxDist, minDist))


