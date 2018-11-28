# http://stackoverflow.com/questions/4960208/python-2-7-getting-user-input-and-manipulating-as-string-without-quotations
t = input()
for i in range(1, t+1):
	# 300000000040000325
	peopleStanding = 0
	extraFriends = 0
	line = raw_input().split()
	# http://stackoverflow.com/questions/8113782/split-string-on-whitespace-in-python
	smax = line[0]
	shyness = line[1]
	# answer = smax
	# Go through all the individuals
	for j in range(0, int(smax)+1):
		# http://stackoverflow.com/questions/2485466/pythons-equivalent-of-in-an-if-statement
		if int(shyness[j]) > 0 and peopleStanding < j:
			extraFriends   += j - peopleStanding
			peopleStanding += j - peopleStanding
		peopleStanding += int(shyness[j])
	# http://stackoverflow.com/questions/2847386/python-string-and-integer-concatenation
	print "Case #" + str(i) + ": " + str(extraFriends)
