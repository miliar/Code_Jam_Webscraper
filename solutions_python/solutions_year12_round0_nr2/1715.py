import sys

input_file = open(sys.argv[1], 'r')

test_cases = int(input_file.readline())
case_counter = 1
scores_range = range(0, 11)

while case_counter <= test_cases:
	
	# processing input
	test_case_input = input_file.readline()
	
	test_case_input = test_case_input.split(' ')
	googlers = int(test_case_input[0])
	surprise = int(test_case_input[1])
	min = int(test_case_input[2])
	
	sum_scores = []
	for s in test_case_input[3:]:
		sum_scores.append(int(s))
	
	# forming output
	googlers_w_min = 0
	
	for s in sum_scores:
		base = int(s / 3)
		
		if s % 3 == 0:
			if base >= min :
				googlers_w_min = googlers_w_min + 1
			elif surprise > 0 and base > 0 and base + 1 >= min:
				googlers_w_min = googlers_w_min + 1
				surprise = surprise - 1
	
		elif s % 3 == 1:
			if base >= min or base + 1 >= min:
				googlers_w_min = googlers_w_min + 1
			elif surprise > 0 and base + 1 >= min:
				googlers_w_min = googlers_w_min + 1
				surprise = surprise - 1
	
		elif s % 3 == 2:
			if base >= min or base + 1 >= min:
				googlers_w_min = googlers_w_min + 1
			elif surprise > 0 and base + 2 >= min:
				googlers_w_min = googlers_w_min + 1
				surprise = surprise - 1
	
	print 'Case #%d: %d' % (case_counter, googlers_w_min)
	
	case_counter = case_counter + 1
	
input_file.close()