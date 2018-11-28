#~ from __future__ import division
import sys, string
import itertools

sys.setrecursionlimit(1e6)

def readlist():
	return [int(x) for x in sys.stdin.readline().strip().split(" ")]

T = int(sys.stdin.readline())

D = []
N = 0
C = 0

cache = {}
def fun(i,L,tsb):
	if i == N: 
		return 0 # am ajuns :)

	if (i,L,tsb) in cache: return cache[i,L,tsb]
	dnext = D[i % C]
	
	# sans booster
	a = dnext * 2 + fun(i+1, L, max(tsb - dnext*2, 0))
	
	#~ print >> sys.stderr, i,L,tsb,"sans", dnext * 2 
	if L:
		dslow = tsb/2
		dfast = dnext - dslow
		if dfast > 0: # castig ceva daca fac speed buster
			b = tsb + dfast + fun(i+1, L-1, 0) # with booster
			#~ print >> sys.stderr, i,L,tsb,"with", tsb + dfast
			a = min(a,b)
	
	cache[i,L,tsb] = a
	return a

for k in range(T):
	data = readlist()
	L,t,N,C = data[0:4]
	D = data[4:]
	cache = {}
	print >> sys.stderr, data[0:4]

	m = fun(0, L, t)
	print "Case #%d: %s" % (k+1, m)
