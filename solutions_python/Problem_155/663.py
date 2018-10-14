T = int(raw_input())

for test in range(1, T+1):

	line = raw_input().split()
	S_max, shyness = int(line[0]), line[1]

	total_people, needed_people = 0, 0


	for level, value in enumerate(shyness):
		value = int(value)
		if level:
			if level > total_people:
				delta = level - total_people

				needed_people += delta
				total_people += delta				

		total_people += value

	print "Case #{}: {}".format(test, needed_people)
