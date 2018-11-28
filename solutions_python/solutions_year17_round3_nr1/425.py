from math import pi

if __name__ == "__main__":
	T = int(raw_input())
	for case_num in range(T):
		#
		# read the input
		#
		N, K = [int(t) for t in raw_input().split()]
		cakes = []
		for cake_num in range(N):
			r, h = [int(t) for t in raw_input().split()]
			cakes.append((r, h))
		#
		# main logic
		#
		answer = 0.0
		# 1) sort by radii and then by side surface
		cakes = sorted(cakes, key=lambda x:(x[0], x[0] * x[1]))
		# 2-1) take the last 1
		current_taken_biggest_index = -1
		biggest_radii = cakes[-1][0]
		taken = [cakes[-1]]
		# 2-2) sort the rest by side area
		rest = cakes[:-1]
		rest = sorted(rest, key=lambda x: x[0] * x[1])
		# 2-3) take K-1 from the rest with largest side areas
		if K-1 > 0:
			taken += rest[-(K-1):]
		# 2-4) calculate the answer
		answer = pi * taken[0][0] * taken[0][0]
		answer += sum([2.0 * pi * cake[0] * cake[1] for cake in taken])
		# 3) refining!!!
		while True:
			new_taken_biggest_index = None
			for i in range(-current_taken_biggest_index+1, N+1):
				if cakes[-i][0] < cakes[current_taken_biggest_index][0]:
					new_taken_biggest_index = -i
					break
			# 2-1 again
			if new_taken_biggest_index == None:
				break
			current_taken_biggest_index = new_taken_biggest_index
			biggest_radii = cakes[current_taken_biggest_index][0]
			taken = [cakes[current_taken_biggest_index]]
			# 2-2 again
			rest = cakes[:current_taken_biggest_index]
			rest = sorted(rest, key=lambda x: x[0] * x[1])
			# 2-3 again
			if K-1 > 0:
				taken += rest[-(K-1):]
			# 2-4 (new): check if taken K already
			if len(taken) < K:
				break
			# 2-5 (the previous 2-4) calculate the answer
			tmp_answer = pi * taken[0][0] * taken[0][0]
			tmp_answer += sum([2.0 * pi * cake[0] * cake[1] for cake in taken])
			if tmp_answer > answer:
				answer = tmp_answer
		print "Case #%d: %f" % (case_num + 1, answer)
	pass