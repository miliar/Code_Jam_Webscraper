import math

t = int(input())
for t in range(t):
	n,k = tuple(map(int, input().split(' ')))
	stalls = [[0, math.floor((n+1) / 2), n+1]]
	#occupied = [False] * (n+2)
	#occupied[0] = occupied[n+1] = True
	#occupied[buckets[0][1]] = True

	for i in range(k-1):
		candidates = []
		for l,m,r in stalls:
			candidates.append([l, math.floor((l+m) / 2), m])
			candidates.append([m, math.floor((r+m) / 2), r])

		_l = None
		_r = None
		curr_best = None
		for l,m,r in candidates:
			if (curr_best == None) \
				or min(m-l-1, r-m-1) > _l:
				_l = min(m-l-1, r-m-1)
				_r = max(m-l-1, r-m-1)
				curr_best = [l,m,r]
			elif min(m-l-1, r-m-1) == _l and max(m-l-1, r-m-1) > _r:
				_r = max(m-l-1, r-m-1)
				curr_best = [l,m,r]

		for s in stalls:
			if curr_best[1] < s[1] and s[0] < curr_best[1]: s[0] = curr_best[1]
			if curr_best[1] > s[1] and s[2] > curr_best[1]: s[2] = curr_best[1]

		stalls.append(curr_best)

	l,m,r = stalls[-1]
	_l = max(m-l-1, r-m-1)
	_r = min(m-l-1, r-m-1)

	print('Case #%d: %d %d' % (t+1, _l, _r))
