from collections import defaultdict

T = int(raw_input())

def f(n,k):
	intervals = defaultdict(int)
	intervals[n] = 1
	while k>0:
		to_cut = max(intervals.keys())
		duplicates = intervals[to_cut]
		left = (to_cut-1)/2
		right = to_cut-1-left
		k -= duplicates
		del intervals[to_cut]
		intervals[left] += duplicates
		intervals[right] += duplicates
	return right, left

for test_case in range(T):
	N, K = [int(x) for x in raw_input().split()]
	a, b = f(N,K)
	print "Case #%s: %s %s"%(test_case+1, a, b)

