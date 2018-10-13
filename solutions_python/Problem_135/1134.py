input = open('A-small-attempt0.in', 'r')
output = open('output.txt', 'w')

test_case_count = int(input.readline())

#process test case one by one
for i in range(test_case_count):
	#store relevant data
	selected_row_1 = int(input.readline())-1
	arrangement_1 = []
	for j in range(4):
		arrangement_1.append(str.strip(input.readline()))
	selected_row_2 = int(input.readline())-1
	arrangement_2 = []
	for j in range(4):
		arrangement_2.append(str.strip(input.readline()))

	#find match
	match_count = 0
	match_case = None
	for number_1 in arrangement_1[selected_row_1].split(' '):
		for number_2 in arrangement_2[selected_row_2].split(' '):
			if number_1 == number_2:
				match_count += 1
				match_case = number_1

	if (match_count == 0):
		y = 'Volunteer cheated!'
	elif (match_count == 1):
		y = match_case
	else:
		y = 'Bad magician!'
	#print output
	output.write("Case #%d: %s\n" %(i+1, y))