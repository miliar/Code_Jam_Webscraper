for t in xrange(int(raw_input())):
	line = map(int, raw_input().split())
	S, p = line[1:3]
	scores = line[3:]
	count = 0
	for score in scores:
		if p <= (score + 2) / 3 and score >= p:
			count += 1
		elif p <= (score + 4) / 3 and S > 0 and score >= p:
			count += 1
			S -= 1
	print "Case #%d: %d" % (t + 1, count)
	#p * 3 - 2 <= sum -- count it
	#p * 3 - 4 <= sum -- count it with surprise
