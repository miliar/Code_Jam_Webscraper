#!/usr/bin/python
import sys

infile = open(sys.argv[1], 'r')

numCases = int(infile.readline())
caseNum = 0

for case in range(numCases):
	caseNum += 1
	numVals = int(infile.readline())
	nums = [int(i) for i in infile.readline().split()]
	nums.sort()
	nums.reverse()
	
	totalXor = 0
	for i in nums:
		totalXor ^= i
		
	if totalXor != 0 or len(nums) < 2:
		print "Case #%s: NO" % (caseNum)
		continue
	else:
		print "Case #%s: %s" % (caseNum, sum(nums[:-1]))
	
	"""
	maxVal = 0
	temp = nums[0]
	while temp:
		temp >>= 1
		maxVal += 1
		
	myNums = []
	hisNums = []
	
	count = 0
	for i in range(maxVal-1, -1, -1):	# bit value to 0
		myCount = 0
		hisCount = 0
		leftCount = 0
		bitVal = 1 << i
		for j in myNums:
			if j & bitVal:
				myCount += 1 
		for j in hisNums:
			if j & bitVal:
				hisCount += 1
		for j in nums:
			if j & bitVal:
				leftCount += 1
		for j in range(nums-1):
	"""
