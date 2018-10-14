import heapq
import math

T = input()
for xx in range(1,T+1):
	N, K = [int(s) for s in raw_input().split()]
	heap = [-N]
	temp1, temp2 = 0, 0
	for i in range(K):
		x = heapq.heappop(heap)
		temp1 = math.ceil(float(x+1)/2)
		temp2 = math.floor(float(x+1)/2)
		heapq.heappush(heap, temp1)
		heapq.heappush(heap, temp2)
	print "Case #%d: %d %d" %(xx, -temp2, -temp1)