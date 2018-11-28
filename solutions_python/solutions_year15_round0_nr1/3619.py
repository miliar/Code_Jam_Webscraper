with open("./A-small-attempt0.in.txt") as f:

	test_case_no = int(f.readline())

	for test_no in xrange(test_case_no):
		test_case = f.readline().split()
		smax = int(test_case[0])
		audience = [int(i) for i in str(test_case[1])]

		friends = 0
		standing = 0



		for (shy_level, shyness) in enumerate(audience):
			if standing >= shy_level:
				standing += shyness
			else:
				friends += shy_level - standing
				standing = shy_level
				standing += shyness

		print "Case #" + str(test_no + 1) + ": " + str(friends)