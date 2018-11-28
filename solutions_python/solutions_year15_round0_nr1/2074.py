def Q1(max_shy, shy_levels):
	num_participants = sum(shy_levels)
	num_stand = 0
	num_extras = 0
	
	if(max_shy == 0):
		return "0"
	elif(num_stand == num_participants):
		return "0"
	else:
		# Make the 0's stand up
		num_stand = num_stand + shy_levels[0]
		for i in range(1, len(shy_levels)):
			if shy_levels[i] == 0:
				continue

			if(num_stand >= i):
				num_stand = num_stand + shy_levels[i]
			else:
				num_needed = i - num_stand
				shy_levels[i] = shy_levels[i] + num_needed
				num_extras = num_extras + num_needed
				num_stand = num_stand + shy_levels[i]

	return str(num_extras)


if __name__ == "__main__":
	m_file = open("A-large.in")
	num_testcases = int(m_file.readline())

	for i in range(0, num_testcases):
		# Parsing Input
		m_input = m_file.readline()
		split_input = str.split(m_input, " ")

		max_shyness = int(split_input[0])
		shy_input = split_input[1].rstrip()
		shyness_levels = []

		for char in shy_input:
			shyness_levels.append(int(char))

		num = Q1(max_shyness, shyness_levels)
		print "Case #" + str(i + 1) + ":" + " " + str(num)