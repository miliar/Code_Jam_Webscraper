
"""

Basic idea:
	We define a tree such that level i corresponds to 2^i - 1 people having entered the bathroom
	Each level also has a "canonical" n_i, representing the number of spaces in between occupied stalls
	Every vertex at level i has some offset >= 0 from the canonical n_i, representing a gap of n_i + offset
	To find level i + 1, we first check to see if n_i is even or odd.
		if n_i is even, then every vertex with offset 0 splits into one vertex of offset 0 and one of offset 1
			and every vertex with offset 1 splits into two vertices with offset 1
		if n_i is odd, then every vertex with offset 0 splits into two vertices with offset 0
			and every vertex with offset 1 splits into one vertex with offset 0 and one vertex with offset 1
		in either case, n_{i + 1} is floor((n_i - 1) / 2)
	At the root, we have n_0 = N and the only vertex is a zero.

	Once we get to a level m such that adding a new layer to the tree would require more than K people to have entered 
		the bathroom, we put the remaining people in the gaps, filling those with offset 1 first
	If the last person is put in a gap with offset 1, we get left = floor((n_m + 1) / 2) and right = ceil((n_m + 1) / 2)
	If the last person is put in a gap with offset 0, we get left = floor(n_m / 2) and right = ceil(n_m / 2)

"""

from math import floor, ceil

numInputs = int(input())

for case in range(1, numInputs + 1):
	N, K = [int(s) for s in input().split(" ")] # taken from the quickstart guide
	n = N
	peopleLeft = K
	nextLevel = 1
	zeros, ones = 1, 0
	while peopleLeft > 2**(nextLevel - 1):
		if n%2 == 0:
			ones = zeros + (2 * ones)
			# zeros stays the same
		else:
			zeros = (2 * zeros) + ones
			# ones stays the same
		n = floor((n - 1) / 2)
		peopleLeft -= 2**(nextLevel - 1)
		nextLevel += 1
	if peopleLeft <= ones:
		# enough one-offset slots to put the last person in one of them
		left = floor(n/2)
		right = ceil(n/2)
	else:
		# will run out of one-offset slots, so last person goes in zero-offset slot
		left = floor((n - 1)/2)
		right = ceil((n - 1)/2)
	print("Case #" + str(case) + ": " + str(right) + " " + str(left)) # right >= left