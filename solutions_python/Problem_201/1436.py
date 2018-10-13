import heapq

t = input()
for case in xrange(t):
	h = []
	row = raw_input().split()
	n = int(row[0])
	k = int(row[1])
	heapq.heappush(h, -n)
	for _ in xrange(k-1):
		largest = -heapq.heappop(h)
		l = 0
		r = 0
		if largest % 2 == 0:
			l = (largest - 1) / 2
			r = largest / 2
		else:
			l = r = largest / 2
		if l: heapq.heappush(h, -l)
		if r: heapq.heappush(h, -r)
	last = -heapq.heappop(h)
	left = 0
	right = 0
	if last % 2 == 0:
		left = (last - 1) / 2
		right = last / 2
	else:
		left = right = last / 2
	print "Case #{}: {} {}".format(case+1,
								   max(left, right),
								   min(left, right))
