#Get number of cases
T = int(raw_input())
 
#Run cases
for t in range(T):
	#Get N for case t+1
	N = int(raw_input())
	#Check if N is tidy, if not, check next number
	tidy = False
	while not tidy:
		testN = N
		digit = 9
		tidy = True
		while testN > 0:
			if testN%10 > digit:
				tidy = False
				N -= 1
				break
			digit = testN%10
			testN /= 10
	print "Case #{0}: {1}".format(t+1, N)