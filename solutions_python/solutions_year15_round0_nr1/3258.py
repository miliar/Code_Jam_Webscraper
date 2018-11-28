tests = int(raw_input())
casenum = 1

while tests:
	shyest, people = [str(x) for x in raw_input().split()]
	#go through people to see how many friends needed
	friends = 0
	clapping = [0]*len(people) #list of people clapping at each position
	clapping[0] = int(people[0]) #put s = 0 people in first
	if int(shyest) != 0:
		for i in range(1, len(people)):
			if i > clapping[i - 1]:
				friends += 1
				clapping[i-1] = clapping[i-1] + 1
			clapping[i] = int(people[i]) + clapping[i-1]

 	print "Case #" + str(casenum) + ": " + str(friends)
 	casenum += 1
 	tests -= 1
