from itertools import combinations, chain

def f(v, i, S, memo):
	if i >= len(v): return 1 if S == 0 else 0
	if (i, S) not in memo:
		count = f(v, i + 1, S, memo)
		count += f(v, i + 1, S - v[i], memo)
		memo[(i, S)] = count
	return memo[(i, S)]

def g(v, S, memo):
	subset = []
	for i, x in enumerate(v):
		if f(v, i + 1, S - x, memo) > 0:
			subset.append(x)
			S -= x
	return subset

cases = int(raw_input())

for i in range(cases):
	inp = raw_input().split()
	newL = []
	newS = set()
	for x in range(int(inp[0])):
		newL.append(int(inp[x+1]))
		newS.add(int(inp[x+1]))
	newL.sort(reverse=True)
	print "Case #" + str(i+1) + ":"
	memo = dict()
	subset_sizes = reversed(range(2,11))
	seen = set()
	for item in chain.from_iterable(combinations(newS,f) for f in subset_sizes):
		pairs = set(combinations(item,2))
		if not pairs.intersection(seen):
			seen.update(pairs)
			#print item
	for x1 in range(len(seen)):
		curset = seen.pop()
		cursum = sum(curset)
		newSCOPY = newS.copy()
		for y22 in curset:
			newSCOPY.remove(y22)
		
		if f(list(newSCOPY), 0, cursum, memo) == 0:
			if x1 == len(seen): 	print "Impossible"
			continue
			#print("There are no valid subsets.")
			# No valid subset
		else:
			for t2 in curset:
				print t2,
			print''
			for t in g(list(newSCOPY), cursum, memo):
				print t,
			print ''
			break
