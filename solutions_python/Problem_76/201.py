for casenum in xrange(1,1+int(raw_input())):
	N = int(raw_input())
	Candies = [int(z) for z in raw_input().split()]
	sum = 0
	min = Candies[0]
	xor = 0
	for C in Candies:
		sum += C
		xor = xor ^ C
		if C < min:
			min = C
	if xor != 0:
		print("Case #%d: " % casenum) + str("NO")
	else:
		print("Case #%d: " % casenum) + str(sum - min)
		