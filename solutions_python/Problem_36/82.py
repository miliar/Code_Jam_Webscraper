#!/usr/bin/python
import sys

T = int(sys.stdin.readline())
for cs in range(1, T+1):
	A = sys.stdin.readline().strip()
	B = "welcome to code jam"
	assert len(B) == 19
	memo = {}
	
	def f(i, j):
		if i > len(A) or j > len(B): return 0
		if i == len(A) and j == len(B): return 1

		key = (i, j)
		if key in memo: return memo[key]
		
		res = f(i+1, j)
		if i < len(A) and j < len(B) and A[i] == B[j]:
			res += f(i+1, j+1)

		memo[key] = res
		return res

	print "Case #%d: %04d" % (cs, f(0, 0) % 10000)
