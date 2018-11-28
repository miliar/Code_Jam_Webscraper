def ovation(case,input):
	numclapping = int(input[0])
	friends = 0
	for index,value in enumerate(input[1:]):
		diff = (index+1) - numclapping
		if int(value) > 0 and diff > 0:
			friends += diff
			numclapping += diff
		numclapping += int(value)
	print "Case #"+str(case+1)+": "+ str(friends)

with open("A-small-attempt0.in") as f:
	numtests = f.readline()
	for case in xrange(int(numtests)):
		line = f.readline()
		input = line.split(" ")[1]
		ovation(case,input.rstrip())
