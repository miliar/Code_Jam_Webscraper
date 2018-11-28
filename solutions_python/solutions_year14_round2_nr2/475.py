#!/usr/bin/env python

for t in range(int(raw_input())):
	A, B, K = map(int, raw_input().split())
	answer = 0
	for a in range(A):
		for b in range(B):
			if a & b < K:
				answer += 1
	print 'Case #{0}: {1}'.format(t + 1, answer)
