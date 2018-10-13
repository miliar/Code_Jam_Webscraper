cases = int(raw_input())

debug = False



for case in range(cases):
	line = raw_input().split()
	Smax = int(line[0])
	rows = line[1]

	neededFriends = 0

	if debug:	print "Rows: " + rows

	peopleClapping = 0
	for row in range(len(rows)):

		if debug: print "@ row " + str(row) + ", " + str(peopleClapping) + " people are clapping"

		# Reserve the first row (lowest shyness level) for your friends
		if row == 0:
			peopleClapping += int(rows[row])
			continue

		peopleOnRow = int(rows[row])
		if row > peopleClapping:
			neededFriends += 1
			peopleClapping += 1
		peopleClapping += peopleOnRow



	print "Case #" + str(case+1) + ": " + str(neededFriends)
