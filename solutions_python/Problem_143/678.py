import sys

with open(sys.argv[1]) as inputFile:
	data=inputFile.readlines()
	numTestCases=int(data[0].strip())
	for i in range(1,len(data)):
		positiveCases=0
		thisTestCase=data[i].strip().split(" ")
		a,b,k=int(thisTestCase[0]),int(thisTestCase[1]),int(thisTestCase[2])
		arrayA=[ia for ia in range(0,a)]
		arrayB=[ib for ib in range(0,b)]
		arrayK=[ik for ik in range(0,k)]
		for itemA in arrayA:
			for itemB in arrayB:
				if int(itemA&itemB) in arrayK:
					positiveCases+=1
		print "Case #"+str(i)+": "+str(positiveCases)
