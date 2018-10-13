#! /usr/bin/python

import sys

def collerroaster(R,k,N,groups):
	monies = 0
	if sum(groups) <= k: return R * sum(groups)
	head = 0
	cache = {}
	for ride in xrange(R):
		pplz = 0
		ridehead = head
		cached = cache.get(ridehead)
		if cached != None:
			ridecash,newhead = cached
			head = newhead
			monies += ridecash
			continue
		while (pplz + groups[head] <= k):
			pplz += groups[head]
			head = (head + 1) % N
		cache[ridehead] = (pplz,head)
		monies += pplz
	return monies

if __name__ == "__main__":
	cases = int(sys.stdin.readline())
	for case in xrange(1,cases+1):
		R,k,N = map(int, sys.stdin.readline().strip().split())
		groups = map(int, sys.stdin.readline().strip().split())
		assert len(groups) == N
		monies = collerroaster(R,k,N,groups)
		print "Case #%d: %d" % (case, monies)
