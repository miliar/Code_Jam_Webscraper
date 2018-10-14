for cases in xrange(input()):
	input = raw_input()  
	l = input.split()
	maxshy = int(l[0])
	sym = list(l[1])
	shy = [int(x) for x in sym]
 	mininvite = 0
	runsum = 0
	for j in xrange(maxshy+1):
		mininvite = max(mininvite,j - runsum)
		runsum += shy[j]
	print "Case #"+str(cases+1)+": "+str(mininvite)

