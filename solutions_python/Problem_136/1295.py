
testcase = int(raw_input())
for caseno in xrange(1, testcase + 1):
	C, F, X = map(float, raw_input().split())
	v = 2
	t = 0
	if C / v + X / (v + F) >= X / v:
		print "Case #%d: %.7f" % (caseno, X / v)
		continue
	n = 1
	while C / (v + n * F) + X / (v + n * F + F) < X / (v + n * F):
		n *= 2
	l = n / 2
	r = n
	while l + 1 != r:
		n = (l + r) / 2
		if C / (v + n * F) + X / (v + n * F + F) < X / (v + n * F):
			l = n
		else:
			r = n
		# print l, r
	# n = l
	# print "C / (v + n * F) + X / (v + n * F + F) = ", C / (v + n * F) + X / (v + n * F + F)
	# print "X / (v + n * F) = ", X / (v + n * F)
	# n = r
	# print "C / (v + n * F) + X / (v + n * F + F) = ", C / (v + n * F) + X / (v + n * F + F)
	# print "X / (v + n * F) = ", X / (v + n * F)

	n = l
	t = 0
	for i in xrange(0, n + 1):
		t += C / (v + i * F)
	t += X / (v + n * F + F)
	print "Case #%d: %.7f" % (caseno, t)
	#print "Case #%d: %.7f" % (caseno, t)
