for t in range(input()):
	A = raw_input().split()
	Smax = int(A[0])
	people = A[1]
	numClapping = int(people[0])
	moreNeeded = 0
	for i in range(1, Smax+1):
		if numClapping >= i:
			numClapping += int(people[i])
		else:
			moreNeeded += (i-numClapping)
			numClapping += (i-numClapping)
			numClapping += int(people[i])
	print "Case #"+str(t+1)+": "+str(moreNeeded)