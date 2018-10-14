from math import ceil, floor


if __name__ == "__main__":
	cases = int(raw_input())
	for case in range(cases):
		#
		# N: number of ingredients
		# P: number of packages (for each ingredient)
		#
		N, P = map(lambda e: int(e), raw_input().strip().split())
		#
		# R: requirement
		#
		R = map(lambda e: int(e), raw_input().strip().split())
		#
		# possession: what we have
		#
		possession = []
		for ingredient in range(N):
			packages = map(lambda e: int(e), raw_input().strip().split())
			packages.sort()
			possession.append(packages)
		#
		# N-way merge QAQ
		#
		answer = 0
		merge_pointers = [0 for i in range(N)]
		while max(merge_pointers) < P:
			servings_ranges_lower = []
			servings_ranges_upper = []
			for i in range(N):
				# calculate the servings range of possession[N][P]
				# using R[i]
				# R[i] * servings * 0.9 <= possession[N][P] <= R[i] * servings * 1.1
				upper = int(floor(possession[i][merge_pointers[i]] / (R[i] * 0.9)))
				lower = int(ceil(possession[i][merge_pointers[i]] / (R[i] * 1.1)))
				servings_ranges_lower.append(lower)
				servings_ranges_upper.append(upper)
			# print "servings ranges:"
			# print servings_ranges_upper
			# print servings_ranges_lower
			# print ""
			valid_ranges = [1 for i in range(N) if servings_ranges_upper[i] >= servings_ranges_lower[i]]
			if 0 < max(servings_ranges_lower) <= min(servings_ranges_upper) and len(valid_ranges) == N:
				# yes! forming a kit
				answer += 1
				merge_pointers = [mp + 1 for mp in merge_pointers]
			else:
				# no! should move one of the mp
				merge_pointers[servings_ranges_lower.index(min(servings_ranges_lower))] += 1
		print "Case #%d: %d" % (case + 1, answer)
