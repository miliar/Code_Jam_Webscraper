tests = int(raw_input())

for test in range(tests):
	case = raw_input().split()
	string_length = int(case[0])
	audience_size = sum(map(lambda x: int(x), case[1]))
	total_standing = 0
	count = 0

	for digit, counter in zip(case[1], range(string_length+2)):
		digit = int(digit)
		invite = 0
		if total_standing < counter and digit != 0:
			invite = counter - total_standing
			count += invite

		total_standing += digit + invite

	print "Case #%d: %d" % (test+1, count)
