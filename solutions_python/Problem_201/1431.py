# Woooo! Trying the (not-that-) new hammer (python, that is) on ALL THE NAILZ!

# span-splitting fun!  (beats talking about bathroom stalls...)

tc = int(input())  # of test cases
for cc in range(1, tc + 1):
	n, k = [int(i) for i in input().split()]
	spans = {n: 1}

	# HACK: without actually doing the math
	# short circuit cases that are clearly pathological

	if k > n *3/4:
		minspan = maxspan = 0
		k = -1

	for _ in range(k):
		# find largest span
		width = sorted(spans.keys(), reverse=True)[0]

		# split it and assign max/min span values
		minspan = width // 2
		maxspan = width - minspan
		if (maxspan>minspan):
			maxspan -= 1
		else:
			minspan -= 1

		# if not end then chuck spans back into list
		spans[width] -= 1
		if spans[width] < 1: del spans[width]

		# in light of gratuitous book-keeping
		# spans is now a list of widths and non-zero frequencies
		if maxspan > 0:
			try:
				spans[maxspan] += 1
			except KeyError:
				spans[maxspan] = 1

		if minspan > 0:
			try:
				spans[minspan] += 1
			except KeyError:
				spans[minspan] = 1			

		# print(spans)


	print("Case #{}: {} {}".format(cc, maxspan, minspan))