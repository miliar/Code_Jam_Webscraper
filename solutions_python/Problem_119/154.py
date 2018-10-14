#!/usr/bin/env python

'''
'cause python is a really stupid way to search this space.

Not even pypy can save me now, but it's 2:30am
'''

import sys
from collections import Counter

def blert(): return map(int, sys.stdin.next().strip().split())

class Solution(Exception): pass

cwin=None
ckey=None

def minimally_solvable(haz, chestsleft):
	haz = Counter(haz)
	for c in chestsleft:
		haz[ckey[c]] -= 1
		haz.update(cwin[c])
	return all(rem >= 0 for k,rem in haz.items())


## We're doing a DFS.
## If we've tried this already, we didn't hit the goal before this
## was called before, so that means we're wasting our time

broken_dreams = None
def tried(soln, chestsleft, hazkeys):
	dream = repr(chestsleft)+repr(sorted(hazkeys.items()))
	orly = dream in broken_dreams
	broken_dreams.add(dream)
	return orly

def YARRRRRR(soln, chestsleft, hazkeys):
	if tried(soln,chestsleft,hazkeys): 
		return
	#print "at",soln,"chestsleft",chestsleft,"hazkeys",hazkeys
	if not minimally_solvable(hazkeys, chestsleft): return
	if len(chestsleft) == 0:
		s = Solution()
		s.soln = soln
		raise s
	for n in chestsleft:
		if hazkeys[ckey[n]]:
			# include unlocking sound
			newhazkeys = Counter(hazkeys)
			newhazkeys[ckey[n]] -= 1
			newhazkeys.update(cwin[n])
			newchestsleft = list(chestsleft)
			newchestsleft.remove(n)
			YARRRRRR(soln+" "+str(n), newchestsleft, newhazkeys)

if __name__ == '__main__':
	ncases, = blert()
	for casenum in range(1,ncases+1):
		nstartkeys, nchests = blert()
		startkeys = blert()
		broken_dreams = set()
		cwin = [None]
		ckey = [None]
		for _ in xrange(nchests):
			C = blert()
			cwin.append(C[2:])
			ckey.append(C[0])
		#print nchests,"chests. start with: ",startkeys
		#allkeys = Counter()
		#map(allkeys.update, cwin[1:])
		#print "ever solvable?", minimally_solvable(startkeys,allkeys.elements(), ckey[1:])
		try:
			YARRRRRR("", range(1,nchests+1), Counter(startkeys))
			print "Case #%s: IMPOSSIBLE" % casenum
		except Solution as soln:
			print "Case #%s:%s" % (casenum,soln.soln)
		
