from math import floor, ceil
from heapq import heappop, heappush

def solve(n, k):
	maxheap = [-n]
	for _ in range(k-1):
		freespace = heappop(maxheap) + 1
		heappush(maxheap, floor(freespace/2))
		heappush(maxheap, ceil(freespace/2))
	sol = heappop(maxheap) + 1
	return -floor(sol/2), -ceil(sol/2)

sols = []

with open('C-small-2-attempt0.in') as f:
	t = int(f.readline())
	for i in range(t):
		n, k = map(int, f.readline().split())
		sols.append(solve(n, k))

with open('sols-C-small-2.txt', 'w') as f:
	for i, y in enumerate(sols):
		f.write('Case #{}: {} {}\n'.format(i+1, y[0], y[1]))