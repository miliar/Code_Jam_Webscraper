def solve(N, K):
	large = N
	ct_large = 1
	ct_total = 1
	while True:
		large_nxt = large/2
		ct_large_nxt = 0
		for num, ct in [(large, ct_large), (large-1, ct_total-ct_large)]:
			if ct >= K:
				return num/2, num/2 - 1 + num%2
			K -= ct
			if num/2 == large_nxt:
				ct_large_nxt += ct
			if num/2 - 1 + num%2 == large_nxt:
				ct_large_nxt += ct
		large = large_nxt
		ct_large = ct_large_nxt
		ct_total *= 2


T = int(raw_input())
for case in xrange(1, T+1):
	N, K = map(int, raw_input().split())
	print "Case #{}: {}".format(case, "{} {}".format(*solve(N, K)))