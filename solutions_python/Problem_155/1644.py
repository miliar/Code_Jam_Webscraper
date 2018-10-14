T = int(raw_input())

for t in xrange(T):
	S = map(int, [c for c in raw_input().split(' ')[1]])
	# SMax = len(S)-1
	R = 0
	u = 0
	for i, v in enumerate(S[:-1]):
		if u + v >= i + 1:
			u += v
		else:
			u += 1
			R += 1

	print "Case #%d: %d" %(t+1, R)
