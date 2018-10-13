# Andy Rock
# April 7, 2016
# 
# Qualification Round 2017: Problem C. 

def calc(n):
	return (n / 2, n / 2) if n % 2 else (n / 2 - 1, n / 2)

def fast(N, K):

	ans = calc(N)
	while K > 1:
		if ans[0] == ans[1]:
			K /= 2
			ans = calc(ans[1])
		else:
			if K % 2:
				K = (K - 1) / 2
				ans = calc(ans[0])
			else:
				K /= 2
				ans = calc(ans[1])

	return (max(ans), min(ans))

for T in xrange(1, int(input()) + 1):
	N, K = map(int, raw_input().split())

	ans = fast(N, K)

	print 'Case #%d: %d %d' % (T, ans[0], ans[1])
