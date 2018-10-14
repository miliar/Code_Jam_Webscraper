#!/usr/bin/env python

n = int(raw_input())
for t in range(1, n+1):
	Smax, S = raw_input().split()
	cnt, added = 0, 0
	for i in range(len(S)):
		Si = int(S[i])
		if Si == 0:
			continue
		if cnt >= i:
			cnt += Si
			continue
		added += i - cnt
		cnt = i + Si
	print 'Case #%d: %d' % (t, added)
