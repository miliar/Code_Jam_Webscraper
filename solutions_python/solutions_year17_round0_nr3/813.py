T = int(raw_input())

for re in range(T):
	N, K = map(int, raw_input().split())

	s = 0
	p = 1

	big = N + 1
	bigCnt = 0

	while K > s + p:
		s += p
		p *= 2
		big = (N - s) / p + 1
		bigCnt = (N - s) % p


	ans = big if K - s <= bigCnt else big-1
	ans -= 1
	
	print 'Case #' + str(re+1) + ': ' + str(ans - ans/2) + ' ' + str(ans/2)
