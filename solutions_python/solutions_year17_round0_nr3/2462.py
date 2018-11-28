#!/usr/bin/env python

import numpy as np

debug = False

def bath(N, K):
	taken = -1
	ls = np.arange(-1, N+1)
	ls[0] = taken
	ls[N+1] = taken

	rs = np.arange(N, -2, -1)
	rs[0] = taken
	rs[N+1] = taken

	def prn():
		print("ls: ", ls)
		print("rs: ", rs)

	def place(n):
		"""place person in the n-th spot (0 is the leftmost)"""
		if debug: print ("picking spot %d. before:" % n)
		if debug: prn()
		assert ls[n] != taken
		assert rs[n] != taken

		max_free = max(ls[n], rs[n])
		min_free = min(ls[n], rs[n])
		ls[n] = taken
		rs[n] = taken

		# fix rs to the left only
		dist = 0
		for m in range(n-1, 0, -1):
			if rs[m] == taken:
				break
			else:
				rs[m] = dist
			dist += 1

		# fix ls only to the right
		dist = 0
		for m in range(n+1, N+1):
			if ls[m] == taken:
				break
			else:
				ls[m] = dist
			dist += 1
		if debug: print("after:")
		if debug: prn()
		return max_free, min_free

	for n in range(1, K+1):
		if debug: print ("placing person #%d" % n)
		if debug: prn()
		# maximise for min(ls, lr)
		mi = np.minimum(ls, rs)
		if debug: print("mi: ", mi)

		max_min = max(mi)
		if debug: print("MI: ", max_min)

		cand = np.where(mi == max_min)[0]
		num_cands = cand.shape[0]
		if debug: print("WH: ", cand, num_cands)
		assert num_cands >= 1
		if num_cands == 1:
			max_free, min_free = place(cand[0])
			continue

		# maximise for max(ls, lr)
		ma = np.maximum(ls, rs)
		if debug: print("ma: ", ma)
		max_max = -1 
		max_idx = -1 
		for m in cand:
			if ma[m] > max_max:
				max_max = ma[m]
				max_idx = m
		if debug: print("MA: ", max_max, " at (leftmost) ", max_idx)
		max_free, min_free = place(max_idx)
	
	return max_free, min_free

num_tests = int(input())

for t in range(1, num_tests+1):
	n, k = [int(x) for x in input().split(" ")]
	free_max, free_min = bath(n, k)
	print("Case #%d: %d %d" % (t, free_max, free_min))
