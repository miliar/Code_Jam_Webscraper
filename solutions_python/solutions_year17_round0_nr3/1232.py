# Vendula Poncova

# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.

from heapq import heappop, heappush

T = int(input())
for i in range(1, T + 1):

	N, K = (int(n) for n in input().split(" "))
	heap = []
	left_s = -1
	right_s = -1
	max_s = N

	for k in range(K):
		left_s = int((max_s - 1) / 2)
		right_s = (max_s - 1) - left_s

		heappush(heap, -left_s)
		heappush(heap, -right_s)
		max_s = -heappop(heap)
		
	print("Case #{}: {} {}".format(i, max(left_s, right_s), min(left_s, right_s)))
	
