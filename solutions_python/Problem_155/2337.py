def trial():
	test = raw_input().split()
	s_max = int(test[0])
	scores = [int(i) for i in list(test[1])]
	claps = 0
	new_claps = 0
	for i, s in enumerate(scores):
		claps += s
		if claps < i + 1:
			new_claps += i + 1 - claps
			claps = i + 1
	return new_claps

T = int(raw_input())
for t in range(T):
	print "Case #%d: %d" % (t + 1, trial())