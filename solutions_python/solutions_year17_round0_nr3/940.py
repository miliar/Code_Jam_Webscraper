import heapq
from collections import defaultdict

def solve(n, k):
	if k > n:
		return -1, -1
	heap = [-n]
	counts = defaultdict(int)
	counts[n] = 1
	while True:
		n = -heapq.heappop(heap)
		c = counts.pop(n)

		n -= 1
		a = n / 2
		b = n - a
		# b >= a
		# print (n, b, a, len(heap), len(counts))
		
		k -= c
		if k <= 0:
			return b, a

		if b > 0:
			if b not in counts:
				heapq.heappush(heap, -b)
			counts[b] += c
		if a > 0:
			if a not in counts:
				heapq.heappush(heap, -a)
			counts[a] += c			


for t in range(int(raw_input())):
	n, k = map(int, raw_input().strip().split())
	a, b = solve(n, k)
	print "Case #{}: {} {}".format(t+1, a, b)
