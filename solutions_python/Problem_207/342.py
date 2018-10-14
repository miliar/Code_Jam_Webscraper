# 


for _ in xrange(input()):
	A = map(int, raw_input().split())
	N = A.pop(0)

	j = i = min([x for x in range(6) if A[x] > 0], key=lambda x: A[x])
	s = ""
	while 1:
		s += "ROYGBV"[i]
		A[i] -= 1
		N -= 1
		if N == 0:
			if j not in [(i + 2 + x) % 6 for x in range(3)]:
				s = "IMPOSSIBLE"
			break
		i = max([(i + 2 + x) % 6 for x in range(3)], key=lambda x: A[x])
		if A[i] == 0: break

	print "Case #%d:" % (_ + 1), N == 0 and s or "IMPOSSIBLE"
