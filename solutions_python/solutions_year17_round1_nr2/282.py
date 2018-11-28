from itertools import permutations

def solve(N, P, R, qts):
	ranges = []
	for i in xrange(N):
		rng = []
		ranges.append(rng)
		for j in xrange(P):
			ratio =  qts[i][j] * 100 / (110 * R[i])
			dv = qts[i][j] * 100 % (110 * R[i])
			if dv == 0:
				mn = ratio
			else:
				mn = ratio + 1
			mn = max(1, mn)
			mx = qts[i][j] * 100 / (90 * R[i])
			if mn > mx:
				continue
			rng.append((mn, mx))
		rng.sort()
	mx = 0
	if len(ranges) == 1:
		return len(ranges[0])
	if len(ranges[1]) > len(ranges[0]):
		perm, stat = ranges[1], ranges[0]
	else:
		perm, stat = ranges[0], ranges[1]
	for ass in permutations(perm, len(stat)):
		ct = 0
		for i in xrange(len(stat)):
			s0, s1 = stat[i]
			a0, a1 = ass[i]
			if s0 <= a1 and a0 <= s1:
				ct += 1
		mx = max(ct, mx)
	return mx


T = int(raw_input())
for case in xrange(1, T+1):
	N, P = map(int, raw_input().split())
	R = map(int, raw_input().split())
	qts = [map(int, raw_input().split()) for _ in xrange(N)]
	print "Case #{}: {}".format(case, solve(N, P, R, qts))

