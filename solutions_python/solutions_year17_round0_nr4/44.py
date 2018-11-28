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

t = int(raw_input())

for q in range(t):
	[n, m] = map(int, raw_input().split(' '))

	RX = range(n)
	CX = range(n)
	dic = {}
	board = {}
	for r in range(n):
		for c in range(n):
			if (r-c) not in dic:
				dic[r-c] = []
			dic[r-c].append(r+c)
	ans = 0
	for i in range(m):
		[s, r, c] = raw_input().split(' ')
		s = s[0]
		r, c = map(int, (r, c))
		r -= 1
		c -= 1
		board[(r,c)] = s
		if s == 'x' or s == 'o':
			if r in RX:
				RX.remove(r)
			if c in CX:
				CX.remove(c)
		if s == '+' or s == 'o':
			if r-c in dic:
				del dic[r-c]
			for key in dic.keys():
				if r+c in dic[key]:
					dic[key].remove(r+c)
		if s == 'o':
			ans += 1
		ans += 1

	added = {}
	for i in range(len(RX)):
		r, c = RX[i], CX[i]
		added[(r,c)] = ('o' if (r,c) in board else 'x')
		board[(r,c)] = added[(r,c)]
		ans += 1

	matching, _ , _ = bipartiteMatch(dic)
	for key in matching.keys():
		val = matching[key]
		r = (key+val)/2
		c = (key-val)/2
		added[(r,c)] = ('o' if (r,c) in board else '+')
		board[(r,c)] = added[(r,c)]
		ans += 1

	print "Case #" + str(q+1) + ": " + str(ans) + " " + str(len(added))
	for (r, c) in added:
		print added[(r, c)], r+1, c+1





