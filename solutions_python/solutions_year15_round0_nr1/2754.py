T = input()

for test_case in xrange(T):

	t, string = raw_input().split()
	t = int(t)
	table = []
	for i in xrange(t+1):
		table.append(int(string[i]))
	#print table

	people_standing = 0
	friends_invited = 0

	i = 0
	while i < t+1:
		#print "i =", i
		if table[i] == 0:
			while table[i] == 0:
				#print "\ti =", i
				i += 1
			if people_standing < i:
				friends_invited += (i - people_standing)
				people_standing += (i - people_standing)
		people_standing += table[i]
		#print "people =", people_standing, "friends =", friends_invited
		i += 1
	print "Case #" + str(test_case+1) + ": " + str(friends_invited)