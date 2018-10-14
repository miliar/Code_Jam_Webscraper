def stalls(N, K):

	# initialize the L and R lists
	L = list(range(N))
	R = list(reversed(range(N)))

	# place K people in stalls
	for _ in range(K):

		# start at the first empty stall
		for stall in range(N):
			if L[stall] is not None:
				best = stall
				best_min = min(L[best], R[best])
				best_max = max(L[best], R[best])
				break;

		# find the best empty stall to go to
		# since we started the best stall as the first empty one, we should only look after that
		for stall in range(best + 1, N):

			# if the current stall is occupied we can just move on
			if L[stall] is None:
				continue

			# grab the current distances between stalls
			curr_min = min(L[stall], R[stall])
			curr_max = max(L[stall], R[stall])

			# if the minimum distance is greater, we definitely trump the previous one
			# if the minimum distance is equal, but the maximum distance is greater, we also trump the previous one
			if (curr_min > best_min) or (curr_min == best_min and curr_max > best_max):
				best = stall
				best_min = min(L[best], R[best])
				best_max = max(L[best], R[best])

		# update the right-distances of stalls to the left of us
		index = best - 1
		dist = 0

		# stop when we hit an occupied stall or the end of the list
		while index >= 0 and R[index] is not None:
			R[index] = dist

			index -= 1
			dist += 1

		# update the left-distances of stalls to the right of us
		index = best + 1
		dist = 0

		# stop when we hit an occupied stall or the end of the list
		while index < N and L[index] is not None:
			L[index] = dist

			index += 1
			dist += 1

		# update ourself to be occupied
		L[best] = None
		R[best] = None

	return best_max, best_min

# play each case
num_cases = int(input())
for case_num in range(num_cases):

	# read in the current case
	N, K = input().split(" ")
	N = int(N)
	K = int(K)

	# run the current case
	max_dist, min_dist = stalls(N, K)
	print("Case #{case}: {max} {min}".format(
		case=case_num + 1,
		max=max_dist,
		min=min_dist,
	))
