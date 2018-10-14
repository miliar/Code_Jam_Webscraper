#!/usr/bin/python3

import sys
import heapq

def docase():
	n = int(sys.stdin.readline())
	x = []
	l = []
	bestl = []
	for i in range(n):
		r = sys.stdin.readline().split()
		x.append(int(r[0]))
		l.append(int(r[1]))
		bestl.append(0)
	target = int(sys.stdin.readline())
	q = []
	heapq.heappush(q, (-x[0], 0))
	bestl[0] = x[0]
	while len(q):
		pri, cur = heapq.heappop(q)
		if pri != -bestl[cur]:
			continue
		if x[cur]+bestl[cur] >= target:
			return "YES"
		i = 1
		while cur+i < n and x[cur+i] <= x[cur]+bestl[cur]:
			avl = min(bestl[cur], x[cur+i]-x[cur], l[cur+i])
			if avl > bestl[cur+i]:
				bestl[cur+i] = avl
				heapq.heappush(q, (-avl, cur+i))
			i += 1
	return "NO"

ncases = int(sys.stdin.readline())
case = 0
for case in range(ncases):
       sys.stdout.write("Case #%d: %s\n" % (case+1, docase()))
