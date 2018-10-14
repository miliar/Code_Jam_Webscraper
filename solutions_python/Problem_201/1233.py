# Google CodeJam 2017 - Qualification Round
# Problem C. Bathroom Stalls
# Author: Mahmoud Aladdin <aladdin3>

import sys
from heapq import heappush, heappop
from Queue import PriorityQueue

def addToPQ(pq, val, cnt, vis):
	if val not in vis:
		vis[val] = 0
		heappush(pq, -1 * val)
	vis[val] += cnt

def solve(cn):
	n, k = map(int, raw_input().strip().split())
	
	pq = []
	vis = {}
	
	addToPQ(pq, n, 1, vis)
	
	mx, mn = -1, -1
	while k > 0:
		sz = -1 * heappop(pq)

		ls = rs = sz >> 1
		if sz % 2 == 0: # Even
			ls -= 1

		addToPQ(pq, rs, vis[sz], vis)
		addToPQ(pq, ls, vis[sz], vis)
		
		k -= vis[sz]
		
		mx = max(ls, rs)
		mn = min(ls, rs)

	print "Case #%d: %d %d" % (cn, mx, mn)
	print >>sys.stderr, "Case #%d: %d %d" % (cn, mx, mn)
	

if __name__ == "__main__":
	tc = input()
	for i in xrange(tc):
		solve(i + 1)
