import timeit
start = timeit.default_timer()


def numberOfFriends(test):
	numberOfFriends = 0
	numberOfStandingPeople = 0
	realTest = test[2:]
	firstPosPassed = False
	while int(realTest[numberOfFriends]) is 0:
		numberOfFriends+=1 
	numberOfStandingPeople = numberOfFriends
	for i in xrange(numberOfFriends, int(test[0]) + 1):
		while numberOfStandingPeople < i:
			# we need more friends:
			numberOfFriends +=1
			numberOfStandingPeople += 1
		# at this point, the people will stand up:
		numberOfStandingPeople += int(realTest[i])
	return numberOfFriends

f = open("ovation.txt", 'r')
counter = 0 
for line in f:
	counter += 1
	if counter > 1:   
		print "Case #" + str(counter - 1) + ": " + str(numberOfFriends(line))








# test = "0 1"

# numberOfFriends = 0
# numberOfStandingPeople = 0
# realTest = test[2:]
# firstPosPassed = False
# while int(realTest[numberOfFriends]) is 0:
# 	numberOfFriends+=1 
# numberOfStandingPeople = numberOfFriends
# for i in xrange(numberOfFriends, int(test[0]) + 1):
# 	while numberOfStandingPeople < i:
# 		# we need more friends:
# 		numberOfFriends +=1
# 		numberOfStandingPeople += 1
# 	# at this point, the people will stand up:
# 	numberOfStandingPeople += int(realTest[i])
# print numberOfFriends
