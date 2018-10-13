# Hopcroft-Karp bipartite max-cardinality matching and max independent set
# David Eppstein, UC Irvine, 27 Apr 2002

def bipartiteMatch(graph):
	'''Find maximum cardinality matching of a bipartite graph (U,V,E).
	The input format is a dictionary mapping members of U to a list
	of their neighbors in V.  The output is a triple (M,A,B) where M is a
	dictionary mapping members of V to their matches in U, A is the part
	of the maximum independent set in U, and B is the part of the MIS in V.
	The same object may occur in both U and V, and is treated as two
	distinct vertices if this happens.'''
	
	# initialize greedy matching (redundant, but faster than full search)
	matching = {}
	for u in graph:
		for v in graph[u]:
			if v not in matching:
				matching[v] = u
				break
	
	while 1:
		# structure residual graph into layers
		# pred[u] gives the neighbor in the previous layer for u in U
		# preds[v] gives a list of neighbors in the previous layer for v in V
		# unmatched gives a list of unmatched vertices in final layer of V,
		# and is also used as a flag value for pred[u] when u is in the first layer
		preds = {}
		unmatched = []
		pred = dict([(u,unmatched) for u in graph])
		for v in matching:
			del pred[matching[v]]
		layer = list(pred)
		
		# repeatedly extend layering structure by another pair of layers
		while layer and not unmatched:
			newLayer = {}
			for u in layer:
				for v in graph[u]:
					if v not in preds:
						newLayer.setdefault(v,[]).append(u)
			layer = []
			for v in newLayer:
				preds[v] = newLayer[v]
				if v in matching:
					layer.append(matching[v])
					pred[matching[v]] = v
				else:
					unmatched.append(v)
		
		# did we finish layering without finding any alternating paths?
		if not unmatched:
			unlayered = {}
			for u in graph:
				for v in graph[u]:
					if v not in preds:
						unlayered[v] = None
			return (matching,list(pred),list(unlayered))

		# recursively search backward through layers to find alternating paths
		# recursion returns true if found path, false otherwise
		def recurse(v):
			if v in preds:
				L = preds[v]
				del preds[v]
				for u in L:
					if u in pred:
						pu = pred[u]
						del pred[u]
						if pu is unmatched or recurse(pu):
							matching[v] = u
							return 1
			return 0

		for v in unmatched: recurse(v)

from sys import stdin
readline = stdin.readline

T = int(readline())
for t in xrange(1, T+1):
	N, C, M = map(int, readline().strip().split())
	P = [None]*M
	B = [None]*M
	
	for i in xrange(M):
		P[i], B[i] = map(int, readline().strip().split())
	
	if C == 2:
		P1 = [P[i] for i in xrange(M) if B[i]==1]
		P2 = [P[i] for i in xrange(M) if B[i]==2]
		P1.sort()
		P2.sort()
		
		one1 = sum([1 if x==1 else 0 for x in P1])
		one2 = sum([1 if x==1 else 0 for x in P2])
		
		rideCount = one1+one2
		
		P1 = P1[one1:]
		P2 = P2[one2:]
		
		flag = False
		if max(P1+[0]) > 2 or max(P2+[0]) > 2:
			flag = True
		
		P1len = max(len(P1) - one2, 0)
		P2len = max(len(P2) - one1, 0)
		rideCount += max(P1len, P2len)
		
		graph = {}
		for i in xrange(len(P1)):
			graph[i] = []
			for j in xrange(len(P2)):
				if P1[i] != P2[j]:
					graph[i].append(j)
		
		maxmatch = len(bipartiteMatch(graph)[0])
		if maxmatch > P1len or maxmatch > P2len:
			promotions = 0
		else:
			P1len -= maxmatch
			P2len -= maxmatch
			promotions = min(P1len, P2len)
		
		print 'Case #%d: %d %d' % (t, rideCount, promotions)
#	tickets = []
#	for i in xrange(M):
#		tickets.append(tuple(map(int, readline().strip().split())))
