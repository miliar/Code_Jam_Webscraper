a = raw_input()
T = int(a)
for caseno in xrange(1, T + 1):
	line = raw_input()
	S, a = line.split()
	S = int(S)
	a = [ord(c) - ord('0') for c in a]
	#print S, a
	total = a[0]
	invite = 0
	for i in xrange(1, len(a)):
		if a[i] > 0 and i > total:
			invite += i - total
			total += (i - total) + a[i]
		else:
			total += a[i]
	print "Case #%d: %d" % (caseno, invite)
