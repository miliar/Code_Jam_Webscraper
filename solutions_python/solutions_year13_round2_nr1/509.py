#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solve(A, N, ar):
	ar.sort()
	global ret
	ret = 1000000000000
	#print A, ar

	def recur(cur, idx, ctn):
		global ret
		if idx >= N:
			ret = min(ret, ctn)

		elif cur > ar[idx]:
			cur += ar[idx]
			recur(cur, idx+1, ctn)

		else:
			recur(cur, idx+1, ctn+1)
			if cur > 1:
				recur(cur+cur-1, idx, ctn+1)

	recur(A, 0, 0)
	return ret

T = int(raw_input())
for i in xrange(1, T+1):
	A, N = map(int, raw_input().split())
	ar = map(int, raw_input().split())

	print "Case #%d: %d" % (i, solve(A, N, ar))