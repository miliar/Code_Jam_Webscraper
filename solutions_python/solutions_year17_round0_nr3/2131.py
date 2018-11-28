def slow(N, K):
	occupied = set()
	def get_gaps():
		diff_minus1 = lambda l: [l[j+1]-l[j]-1 for j in range(len(l)-1)]
		return diff_minus1([-1] + sorted(occupied) + [N])
	def get_min_max_vals(gaps):
		return [(min(gaps[j+1], gaps[j]), max(gaps[j+1], gaps[j])) for j in range(len(gaps)-1)]
	for j in range(K):
		gaps = get_gaps()
		# min_max_vals = get_min_max_vals(gaps)
		# print(min_max_vals)
		# min_max_vals = zip(range(len(min_max_vals)), *zip(*min_max_vals))
		# print(min_max_vals)
		# def compare_key(elem):
		# 	idx, minimum, maximum = elem
		# 	return minimum*N + maximum
		# # min_max_vals = sorted(min_max_vals, key=compare_key)
		# idx, minimum, maximum = max(min_max_vals, key=compare_key)

		def compare_key(elem):
			idx, gap = elem
			return gap
		idx, gap = max(enumerate(gaps), key=compare_key)
		minimum = (gap-1) // 2
		maximum = gap // 2

		curr_occupied_list = list([-1] + sorted(occupied) + [N])
		occupied.add((curr_occupied_list[idx]+curr_occupied_list[idx+1]) // 2)
		if j == K-1:
			return "%d %d" % (maximum, minimum)

T = int(input())
for j in range(T):
	(N, K) = input().split(" ")
	res = slow(int(N), int(K))
	print("Case #%d: %s" % (j+1, res))
