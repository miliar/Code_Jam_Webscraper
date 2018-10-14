def y(wires):
	n = 0
	i = 0
	while i < len(wires):
		(A1, B1) = wires[i]
		for (A2, B2) in wires[i+1:]:
			if (A1 < A2 and B1 > B2) or (A2 < A1 and B2 > B1):
				n += 1
		i += 1
	return n

T = int(raw_input())
for x in xrange(1, T + 1):
	N = int(raw_input())
	wires = [tuple(map(int, raw_input().split(' '))) for _ in xrange(N)]
	print('Case #%d: %d' % (x, y(wires)))
