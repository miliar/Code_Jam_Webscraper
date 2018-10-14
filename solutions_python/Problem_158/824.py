def get_cases(filename):
	file = open(filename, "r")
	num_tests = int(file.readline())
	test_cases = file.readlines()
	file.close()
	return num_tests, test_cases
	
def Q1(filename):
#	num_tests unused - and in fact I don't know why it's included
#	what language fails to detect an EOF??
	num_tests, test_cases = get_cases(filename)
	output = open(filename + ".solution", "w")
	for case in range(len(test_cases)):
		required_friends = 0
		current_clappers = 0
		audience_string = test_cases[case].split()[1]
		for shyness_level in range(len(audience_string)):
			if (current_clappers >= shyness_level):
				current_clappers += int(audience_string[shyness_level])
			else:
				required_friends += shyness_level - current_clappers
				current_clappers = shyness_level + int(audience_string[shyness_level])
		output.write("Case #%d: %d\n" % (case + 1,required_friends))
	output.close()

def Q2(filename):
	num_tests, test_cases = get_cases(filename)
	output = open(filename + ".solution2", "w")
	for case in range(len(test_cases) / 2):
		diners = map(int, test_cases[2*case+1].split())
		diners.sort(reverse=True)
		rate_of_consumption = len(diners)
		highest_stack = diners[0]
		length_of_breakfast = 0
		if (diners[0] / 2 >= len(diners)):
			worth_continuing = True
		else:
			worth_continuing = False
		for diner in range(1,diners[0]/2):
			if not worth_continuing and (diners[0] > diners[diner] + diner):
				worth_continuing = True
		while worth_continuing:
			reverse_insort(diners, diners[0] / 2)
			reverse_insort(diners,(diners[0]+1) / 2)
			diners.pop(0)
			rate_of_consumption += 1
			highest_stack = diners[0]
			length_of_breakfast += 1
			if (diners[0] / 2 >= len(diners)):
				worth_continuing = True
			else:
				worth_continuing = False
			for diner in range(1,diners[0]/2):
				if not worth_continuing and (diners[0] > diners[diner] + diner):
					worth_continuing = True
		length_of_breakfast += diners[0]
		output.write("Case #%d: %d\n" % (case + 1,length_of_breakfast))
	output.close()
	
def Q2_single(diners):
	diners.sort(reverse=True)
	rate_of_consumption = len(diners)
	highest_stack = diners[0]
	length_of_breakfast = 0
	if (diners[0] / 2 >= len(diners)):
		worth_continuing = True
	else:
		worth_continuing = False
	for diner in range(1,diners[0]/2):
		if not worth_continuing and (diners[0] > diners[diner] + diner):
			worth_continuing = True
	while worth_continuing:
		print diners
		reverse_insort(diners, diners[0] / 2)
		reverse_insort(diners,(diners[0]+1) / 2)
		diners.pop(0)
		rate_of_consumption += 1
		highest_stack = diners[0]
		length_of_breakfast += 1
		if (diners[0] / 2 >= len(diners)):
			worth_continuing = True
		else:
			worth_continuing = False
		for diner in range(1,diners[0]/2):
			if not worth_continuing and (diners[0] > diners[diner] + diner):
				worth_continuing = True
	length_of_breakfast += diners[0]
	print length_of_breakfast
	
	
def reverse_insort(a, x, lo=0, hi=None):
    """Insert item x in list a, and keep it reverse-sorted assuming a
    is reverse-sorted.

    If x is already in a, insert it to the right of the rightmost x.

    Optional args lo (default 0) and hi (default len(a)) bound the
    slice of a to be searched.
    """
    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo+hi)//2
        if x > a[mid]: hi = mid
        else: lo = mid+1
    a.insert(lo, x)
	
def Q3(filename):
	num_cases, test_cases = get_cases(filename)
	symbols = set(["i", "j", "k", "1"])
	q_dict = {"ij" : "k", "ji" : "-k", "ik" : "-j", "ki" : "j", "jk" : "i", "kj": "-i"}
	output = open(filename + ".solution", "w")
	for case in range(num_cases):
		X = int(test_cases[2*case].split()[1])
		input_string = test_cases[2*case+1][:-1]*(X%8)
		match_found = False
		check_string = input_string
		while len(check_string) > 1:
			check_string = eval_first_two(check_string, symbols, q_dict)
		if check_string == "-":
			worth_checking = True 
		else:
			worth_checking = False
		while worth_checking and not match_found and len(input_string) > 0:
			if (input_string[0] == "i"):
				j_input_string = input_string[1:]
				while not match_found and len(j_input_string) > 0:
					if (j_input_string[0] == "j"):
						k_input_string = j_input_string[1:]
						while not match_found and len(k_input_string) > 0:
							if (k_input_string == "k"):
								match_found = True
							k_input_string = eval_first_two(k_input_string, symbols, q_dict)
					j_input_string = eval_first_two(j_input_string, symbols, q_dict)
			input_string = eval_first_two(input_string, symbols, q_dict)
		result = "YES" if match_found else "NO"
		output.write("Case #%d: %s\n" % (case + 1,result)) 
	output.close()
	
def Q3_alt(filename):
	num_cases, test_cases = get_cases(filename)
	symbols = set(["i", "j", "k", "1"])
	q_dict = {"ij" : "k", "ji" : "-k", "ik" : "-j", "ki" : "j", "jk" : "i", "kj": "-i"}
	output = open(filename + ".solution", "w")
	for case in range(num_cases):
		X = int(test_cases[2*case].split()[1])
		input_string = test_cases[2*case+1][:-1]*(X%8)
		while len(input_string) > 1:
			input_string = eval_first_two(input_string, symbols, q_dict)
		if input_string == "-":
			result = "YES" 
		else:
			result = "NO"
		output.write("Case #%d: %s\n" % (case + 1,result))
	output.close()
	
def eval_first_two(quaternion_string, symbols, q_dict):
	offset = 0
	chars = []
	negative = False
	while len(chars) < 2 and offset < len(quaternion_string):
		if quaternion_string[offset] == "-":
			negative = not negative
		else:
			chars.append(quaternion_string[offset])
		offset += 1
	if len(chars) < 2:
		return ""
	char_set = set(chars)
	if len(char_set) == 1:
		result = ""
		if list(char_set)[0] != "":
			negative = not negative
	else:
		if len(char_set.difference(set(["1"]))) == 1:
			result = sorted(chars)[1]
		else:
			result = q_dict[reduce(str.__add__,chars)]
	if negative:
		if len(result) == 0:
			result = "-"
		elif result[0] == "-":
			result = result[1:]
		else:
			result = "-" + result
	return result + quaternion_string[offset:]
	
def Q4(filename):
	num_cases, test_cases = get_cases(filename)
	output = open(filename + ".solution", "w")
	for case in range(num_cases):
		X, R, C = map(int, test_cases[case].split())
		print test_cases[case].split()
		if X == 1:
			winner = "GABRIEL"
		if X == 2:
			if R*C % 2:
				winner = "RICHARD"
			else:
				winner = "GABRIEL"
		if X == 3:
			if R * C % 3 == 0 and R * C >= 6:
				winner = "GABRIEL"
			else:
				winner = "RICHARD"
		if X == 4:
			if R*C >= 12:
				winner = "GABRIEL"
			else:
				winner = "RICHARD"
		output.write("Case #%d: %s\n" % (case + 1,winner)) 
	output.close()