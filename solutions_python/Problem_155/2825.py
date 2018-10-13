for case in xrange(input()):
	maxshy, shyer = raw_input().split()
	sumStand = 0
	needMore = 0
	for i in range(len(shyer)):
		if not sumStand >= i:
			needMore += i - sumStand
			sumStand += (i - sumStand)
		sumStand += int(shyer[i])
	print "Case #"+str(case+1)+": "+str(needMore)