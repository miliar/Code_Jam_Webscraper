from math import floor

def middle_n(N):
	x = floor(N/2)
	if x == N/2:
		return x-1, N-x
	else:
		return x, N-(x+1)

def find_largest_gap(L):
	return max(L)

for t in range(int(input())):
	N, K = map(int,input().split())

	gaps = [N]

	for i in range(K-1):
		gap = find_largest_gap(gaps)
		m = gaps.index(gap)

		l, r = middle_n(gap)

		splt = []
		if l > 0: splt.append(l)
		if r > 0: splt.append(r)

		gaps = gaps[:m] + splt + gaps[m+1:]

	# i = K
	gap = find_largest_gap(gaps)
	l, r = middle_n(gap)
	
	print("Case #{0}: {1} {2}".format(t+1, max(l,r), min(l,r)))