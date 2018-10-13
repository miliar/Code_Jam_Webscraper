import sys
buffer = sys.stdin.read().splitlines()
caseNum = int(buffer[0])
for i in range(1,caseNum+1):
	stand = 0
	result = 0
	slev, cust = buffer[i].strip().split()
	slev = int(slev)
	test = [0 for j in range(slev+1)]
	isStand = [False for j in range(slev+1)]
	for j in range(slev+1):
		test[j] = int(cust[j])
		if test[j] == 0:
			isStand[j] = True
	for j in range(slev+1):
		if isStand[j] == True:
			continue
		while stand < j:
			stand += 1
			result += 1
		if stand >= j:
			stand += test[j]

	print "Case #%d: %d" % (i,result) 