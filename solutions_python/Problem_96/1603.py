numCases = (int)(raw_input())
for caseNum in range(1, numCases + 1):
	line = raw_input().strip()
	tokens = line.split(" ")
	numGooglers = int(tokens[0])
	numSurprising = int(tokens[1])
	p = int(tokens[2])
	nums = [int(tokens[3+i]) for i in range(0, numGooglers)]


	count = 0
	countAlmost = 0
	for i in range(0, numGooglers):
		tmp = nums[i]
		if tmp != 0:
			inc = 0
			inc_surprise = 0
			mod = tmp%3
			if mod == 0:
				inc = 0
				inc_surprise = 1
			elif mod == 1:
				inc = 1
				inc_surprise = 1
			else:
				inc = 1
				inc_surprise = 2
		else:
			inc = 0
			inc_surprise = 0
		if (tmp/3)+inc >= p:
			count+=1
		elif (tmp/3)+inc_surprise >= p:
			countAlmost+=1
		#print "nums[i]=%d, nums[i]/3=%d, numSurprising=%d, p=%d, inc=%d, inc_surprise=%d" % (nums[i], nums[i]/3, numSurprising, p, inc, inc_surprise)
	count += min(countAlmost, numSurprising)
	print "Case #%d: %d" % (caseNum, count)
