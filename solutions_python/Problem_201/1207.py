from collections import defaultdict

def too_many_ppl(n):
	# if too many people relative to stalls, will be 0 0
	if n == 1:
		return 1
	elif n == 2:
		return 2
	else:
		x, y = new_dist(n)
		return too_many_ppl(x) + too_many_ppl(y)

def new_dist(n):
	if n % 2 == 0: # if even
		return [n/2, n/2-1]
	else:
		return [(n-1)/2, (n-1)/2]

t = int(raw_input()) # this is the number of test cases
for i in xrange(1, t+1):
	stalls, ppl = str(raw_input()).split(" ")
	stalls = int(stalls)
	ppl = int(ppl)

	if ppl >= too_many_ppl(stalls):
		print  "Case #{}: {} {}".format(i, 0, 0)
	else:
		vacant_dict = defaultdict(lambda: 0)
		vacant_dict[stalls] = 1
		dist = [0,0] # previous known distance
		for j in range(ppl):
			longest = max(vacant_dict.keys())
			if vacant_dict[longest] == 1:
				vacant_dict.pop(longest, None)
			else:
				vacant_dict[longest] -= 1

			if longest <= 1:
				dist = [0,0]
			else:
				dist = new_dist(longest)
			
			for k in range(2):
				vacant_dict[dist[k]] += 1

				
		print  "Case #{}: {} {}".format(i, dist[0], dist[1])
	
