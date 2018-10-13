import heapq
t = int(input())
for testcase in range(1, t + 1):
	n, k = [int(s) for s in input().split(" ")]
	heap = []
	m1, m2 = 0, 0
	heap.append(-1*n)
	heapq.heapify(heap)
	for i in range(0, k):
		#print (heap)
		max_item = heapq.heappop(heap)
		m1 = int((max_item+1) / 2)
		m2 = int(max_item / 2)
		heapq.heappush(heap, m1)
		heapq.heappush(heap, m2)

	print("Case #{}: {} {}".format(testcase, -1*m2, -1*m1))