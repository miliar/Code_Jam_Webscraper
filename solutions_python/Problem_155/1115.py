text = open("/Users/cameronfranz/Documents/Learning/Projects/Code Jam/2015/A-large.in")
numCases = int(text.readline())


for i in range(numCases):	
	
	S_max,S_data	 = text.readline().split()
	totalClapping	 = 0
	neededGuests	 = 0
	
	for j in range(int(S_max)+1):
		n = int(S_data[j])
		if(n>0):
			if(totalClapping < j):
				neededGuests += j - totalClapping
				totalClapping += j - totalClapping
			totalClapping +=n
	
	print "Case #" + str(i+1) + ": " + str(neededGuests)
