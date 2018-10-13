import queue

cases = int(input())

for c in range(1,cases+1):
	raw = input().split()
	N = int(raw[0])
	K = int(raw[1])

	q = queue.PriorityQueue()
	sets = {N: 1}
	s = 0

	gMin, gMax = 0,0

	q.put((-N, N))

	while s < K:
		size = q.get()[1]
		amount = sets[size]
		gMin = (size-1)//2
		gMax = size-1-gMin
		s += amount

		if gMin in sets:
			sets[gMin] += amount
		else:
			sets[gMin] = amount
			q.put((-gMin, gMin))

		if gMax in sets:
			sets[gMax] += amount
		else:
			sets[gMax] = amount
			q.put((-gMax, gMax))

	print("Case #", c, ": ", gMax, " ", gMin, sep="")

