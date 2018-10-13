f = file('B-small-attempt1.in','r')

lines = f.readlines()
T = int(lines[0].strip())

cache = {}
splits ={}

# Keys		# Values	# Time
cache['[]']  = [(0,0)]	# 0
cache['[1]'] = [(1,0)]	# 1
cache['[2]'] = [(2,0)]	# 2
cache['[3]'] = [(3,0)]	# 3
cache['[4]'] = [(2,1)]	# 3
cache['[5]'] = [(3,1)]	# 4
cache['[6]'] = [(3,1)]	# 4
cache['[7]'] = [(4,1)]	# 5
cache['[8]'] = [(4,1)]	# 5
cache['[9]'] = [(5,1),(3,2)]	# 6, 5

#splits[1] = [[1]]
#splits[2] = [[2]]
#splits[3] = [[3]]
splits[4] = [[2,2]]
splits[5] = [[3,2]]
splits[6] = [[3,3]]
splits[7] = [[4,3]]
splits[8] = [[4,4]]
splits[9] = [[6,3],[5,4]]

def run(D,P):
	P = sorted(P, reverse=True)
	sol = alg(P)
	if str(P) not in cache:
		#cache[str(P)] = sol
		pass
	return sol

def find_opts(high):
	return splits[high]

def find_opt(high):
	min_sol = (high,0)
	opt_parts = [high]
	for i in xrange(1,high/2+1):
		parts = [high-i, i]
		sols = ( cache[ str( [ parts[0] ] ) ], cache[ str( [parts[1] ] ) ] )
		# Max of eating time + sum of needed splits + 1 split to create parts
		#time = max(sols[0][0],sols[1][0]) + sols[0][1] + sols[1][1] + 1
		sol = (max(sols[0][0],sols[1][0]), sols[0][1] + sols[1][1] + 1)
		if better(min_sol,sol) == sol:
			min_sol = sol
			opt_parts = parts
	return opt_parts 

def better(p1, p2):
	if p1 == None:
		return p2
	if p2 == None:
		return p1
	t1, t2 = sum(p1), sum(p2)
	if t1 < t2:
		return p1
	if t2 < t1:
		return p2
	if p1[1] < p2[1]:
		return p1
	return p2

def alg(a):
	if len(a) == 0:
		return (0,0)

	# Chceck cache
	s = str(a)
	if s in cache:
		possible = cache[s]
		best_sol = None
		for sol in possible:
			best_sol = better(sol,best_sol)
		return best_sol

	front = a[0]

	# Consider split
	best_sort_a = None
	best_split_params = None
	if front > 3:
		# Possible split optimal
		for split in find_opts(a[0]):
			cpy = a[:]
			cpy.pop(0)
			new_a = cpy + split
			sort_a = sorted(new_a, reverse=True)
			split_sol = alg(sort_a)
			split_params = (split_sol[0], split_sol[1]+1)
			if better(split_params,best_split_params) == split_params:
				best_split_params = split_params
				best_sort_a = sort_a
		'''
		cpy = a[:]
		high = cpy.pop(0)
		opt_split = find_opt(high)
		new_a = cpy + opt_split
		sort_a = sorted(new_a, reverse=True)
		split_sol = alg(sort_a)
		split_params = (split_sol[0], split_sol[1]+1)
		'''

	# Decrement all
	new_a = []
	for elem in a:
		if elem > 1:
			new_a.append(elem-1)
	# Recurse on eating time
	eat_sol = alg(new_a)
	eat_params = (eat_sol[0]+1, eat_sol[1])

	#print best_split_params, eat_params
	sol = better(best_split_params, eat_params)
	key = None
	if sol == best_split_params:
		key = str(best_sort_a)
		#cache[str(sort_a)] = sol
	else:
		key = str(new_a)
		#print "ADD TO CACHE: ", str(new_a), sol
		#cache[str(new_a)] = sol
	
	if key in cache == False:
		#cache[key] = sol
		pass
	return sol

for i in xrange(0,T):
	D = int(lines[2*i+1].strip())
	P = [int(j) for j in lines[2*i+2].strip().split(' ')]

	params = run(D,P)
	#print P, "->", params, " | ", sum(params) #, cache
	out = sum(params)

	print "Case #" + str(i+1) + ": " + str(out)