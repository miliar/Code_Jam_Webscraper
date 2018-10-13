import math

def distance(N, K):
	"""
		returns min(Ls, Rs), max(Ls, Rs)
	"""
	if N == 1:
		return 0, 0

	if K == 1:
		return (N-1)//2, N//2


	lv = int(math.log(K, 2))  # how many levels we'll go down this "binary tree split"
							  # note that if K == 2**N-1, we'll technically complete the last level,
							  # but since we need to know (Ls, Rs) for that level, we let /lv/
							  # be equal to one less than the actual depth

	r = K + 1 - 2**lv  # remaining # of splits to be made on the last level


	spaces = {N: 1}

	for i in range(lv):
		# print(spaces)
		new_spaces = {}
		for a,b in spaces.items():
			new_spaces[(a-1)//2] = new_spaces.get((a-1)//2, 0) + b
			new_spaces[a//2] = new_spaces.get(a//2, 0) + b
		spaces = new_spaces

	

	while r > 1:
		# print(spaces)
		# print(r)

		max_gap = max(spaces.keys())
		if spaces[max_gap] < r:  # split all spaces with max_gaps
			r -= spaces[max_gap]
			spaces[(max_gap-1)//2] = spaces.get((max_gap-1)//2, 0) + spaces[max_gap]
			spaces[max_gap//2] = spaces.get(max_gap//2, 0) + spaces[max_gap]
			spaces.pop(max_gap)
		else:
			# technically we need to make r-1 splits -- but since we know there will be at least 1
			# max_gap left, we know that value will be our /last_gap/ value
			# so we can just leave the dictionary as it is
			r = 1

	# print(spaces)
	# print(r)


	last_gap = max(spaces.keys())
	
	if last_gap == 0:
		return 0, 0

	return (last_gap-1)//2, last_gap//2




t = int(input())  # read a line with a single integer

for j in range(1, t + 1):
    N, K = map(int, input().split(" "))

    smin, smax = distance(N, K)


    print("Case #{}: {} {}".format(j, smax, smin))