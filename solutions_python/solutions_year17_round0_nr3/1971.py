def solve(n, k):
	s = n+2
	a = [0]*s
	a[0] = 1
	a[-1] = 1

	# print(a)

	max_lsrs = 0
	min_lsrs = 0
	target = 0

	for _ in range(k):
		ls = [0]*s
		l = 0
		for i in range(s):
			ls[i] = l
			if a[i] == 0:
				l += 1
			else:
				l = 0

		rs = [0]*s
		r = 0
		for i in range(s-1, -1, -1):
			rs[i] = r
			if a[i] == 0:
				r += 1
			else:
				r = 0

		farthest_dist = 0
		farthest_stalls = []
		for i in range(s):
			if a[i] == 0:
				neighbor_dist = min(ls[i], rs[i])
				if neighbor_dist > farthest_dist:
					farthest_dist = neighbor_dist
					farthest_stalls = [i]
				elif neighbor_dist == farthest_dist:
					farthest_stalls.append(i)

		if len(farthest_stalls) == 1:
			target = farthest_stalls[0]
		else:
			max_dist = 0
			new_stalls = []
			for stall in farthest_stalls:
				dist = max(ls[stall], rs[stall])
				if dist > max_dist:
					max_dist = dist
					new_stalls = [stall]
				elif dist == max_dist:
					new_stalls.append(stall)
			target = new_stalls[0]


		a[target] = 1
		max_lsrs = max(ls[target], rs[target])
		min_lsrs = min(ls[target], rs[target])

		# print(a)

	return max_lsrs, min_lsrs
	

t = int(input())
for case in range(1, t+1):
	n, k = map(int, input().split())
	maxs, mins = solve(n, k)
	print("Case #%i: %i %i" % (case, maxs, mins))











