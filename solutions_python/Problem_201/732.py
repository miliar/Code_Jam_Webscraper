import sys, string

if len(sys.argv) == 2:
	try:
		f = open(sys.argv[1], 'r')
	except IOError:
		print("usage python [curr_testing_file] [input_file_name]")
		sys.exit(1)
	
	num_tests = int(f.readline())
	outputs = []

	for i in range(0, num_tests):
		test = f.readline()

		while test == '\n':
			test = f.readline()

		num_stalls = int(test.split(' ')[0])
		num_people = int(test.split(' ')[1])
		x = num_people
		level = 0
	
		while x != 1:
			x = x / 2
			level += 1
		
		num_odds = 0
		num_evens = 0
		odd_num = 0
		even_num = 0

		if num_stalls % 2 == 0:
			even_num = num_stalls
			num_evens = 1
		else:
			odd_num = num_stalls
			num_odds = 1

		first_in_level = 1
		left_over = num_people

		for v in xrange(0, level):
			left_over -= first_in_level
			first_in_level *= 2
			old_num_odds = num_odds
			old_num_evens = num_evens
			old_odd_num = odd_num
			old_even_num = even_num
			num_odds = 0
			num_evens = 0

			if old_num_odds != 0:
				temp = old_odd_num / 2

				if temp % 2 == 0:
					num_evens += 2 * old_num_odds
					even_num = temp
				else:
					num_odds += 2 * old_num_odds
					odd_num = temp

			if old_num_evens != 0:
				num_odds += old_num_evens
				num_evens += old_num_evens
				
				temp = old_even_num / 2

				if temp % 2 == 0:
					even_num = temp
					odd_num = temp - 1
				else:
					odd_num = temp
					even_num = temp - 1
	
		if even_num < odd_num:
			left_over -= num_odds
			if left_over <= 0:
				print("Case #" + str(i + 1) + ": " + str(odd_num / 2) + " " + str(odd_num / 2))
			else:
				print("Case #" + str(i + 1) + ": " + str(even_num / 2) + " " + str(max(0, (even_num / 2) - 1)))
		else:
			left_over -= num_evens

			if left_over <= 0:
				print("Case #" + str(i + 1) + ": " + str(even_num / 2) + " " + str(max((even_num / 2) - 1, 0)))
			else:
				print("Case #" + str(i + 1) + ": " + str(odd_num / 2) + " " + str(odd_num / 2))
