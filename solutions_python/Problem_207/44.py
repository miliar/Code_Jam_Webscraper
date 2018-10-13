def find_max(c, exc, av, pref):
	#print c, exc
	mx, s = -1, ''
	for k in c:
		if k not in exc:
			#print k, exc
			if c[k] > mx:
				s, mx = k, c[k]
			elif c[k] == mx and k in av[pref] and s not in av[pref]:
				s = k
	return s, mx

def solve_small(cols):
	N = cols[0]
	c = {'R': cols[1], 'O': cols[2], 'Y': cols[3], 'G': cols[4], 'B': cols[5], 'V': cols[6]}
	av = {'R': set('ROV'), 'O': set('ROVYG'), 'Y': set('YOG'), 'G': set('GYBVO'), 'B': set('BGV'), 'V': set('VROGB')}
	sol = []
	exc = set([])
	pref = 'R'
	while len(sol) < N:
		if sol:
			exc = av[sol[-1]]
			pref = sol[0]
		k, rem = find_max(c, exc, av, pref)
		#print k, rem
		if rem == 0:
			#print sol
			return 'IMPOSSIBLE'
		c[k] -= 1
		sol.append(k)
	if sol[0] in av[sol[-1]]:
		return 'IMPOSSIBLE'
	return ''.join(sol)


T = int(raw_input())
for case in xrange(1, T+1):
	cols = map(int, raw_input().split()) #N, R, O, Y, G, B, V
	solution = solve_small(cols)
	print "Case #{}: {}".format(case, solution)


