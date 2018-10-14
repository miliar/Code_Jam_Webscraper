def timeSpan(C, F, X, buys):

	# returns second in float
	t = 0.0
	rate = 2.0
	if buys > 0:
		for i in range(0, buys):

			t += C / rate	# time consumed for buying
			rate += F 	# rate upgrade
	t += X / rate
	return t

fi = open('B-small-attempt2.in')

casesT = fi.readline()

for i in range(0, int(casesT)):

	line = fi.readline()
	C, F, X = [float(j) for j in line[:-1].split(" ")]
	resultBuf = []
	resultBufLimit = 50
	result = 0.0
	resultMin = 0.0
	if C < F:
		maxIter = int(X / (C / F)) + 1
	else:
		maxIter = int(X / 2.0) + 1
	if maxIter < resultBufLimit:

		resultBufLimit = maxIter
	# for buys in range(0, maxIter):
	buys = 0
	while 1:
	
		result = timeSpan(C, F, X, buys)
		# print "case ", i + 1, buys, result
		if len(resultBuf) >= resultBufLimit:

			# free the oldest reading
			resultBuf.pop(0)
		resultBuf.append(result)
		if resultMin == 0.0:

			# initial min
			resultMin = result
		else:
			if result < resultMin:

				# new Min found
				resultMin = result
			if resultMin < min(resultBuf):

				# no more improvement
				break
		buys += 1

	mesg = '%.7f' % resultMin
	print "Case #{0}: {1}".format(i + 1, mesg)
	# print "case ", i+ 1, line 

fi.close()

