import inspect
base = inspect.getfile(inspect.currentframe())[:-3]
data = file(base+'.in', 'r')
out = file(base+'.out', 'wb')

import collections
T = int(data.readline())
for case in range(1,T+1):
	N = int(data.readline())
	C = [int(x) for x in data.readline().split()]
	best = -1
	bx_sums, bs_sums, b_subset = None, None, 0
	for subset in range(1, 2**N-1):   # all subsets
		x_sums = [0,0]
		s_sums = [0,0]
		for idx, val in enumerate(C):
			pile = ((1<<idx) & subset) != 0
			x_sums[pile] ^= val
			s_sums[pile] += val
		if x_sums[0] == x_sums[1] and max(s_sums) > best:
			best = max(s_sums)
			bx_sums = x_sums
			bs_sums = s_sums
			b_subset = subset
	answer = best if best != -1 else 'NO'
	#print N, C, bx_sums, bs_sums, bin(b_subset), answer
	out.write("Case #{0}: {1}\n".format(case, answer))
