from queue import PriorityQueue

t = int(input())



for tc in range(t):
	tc += 1
	n, k = map(int, input().split())

	pq = PriorityQueue()
	pq.put(0)
	for i in range(k - 1):
		x = n - pq.get()
		r = int(x / 2)
		l = int((x - 1) / 2)
		pq.put(n - r)
		pq.put(n - l)

	x = n - pq.get()
	print('Case #{}: {} {}'.format(tc, int(x / 2), int((x - 1) / 2)))
