def solve_case(case):

	def count_min_people_necessary(crowd):

		standing_people = 0
		extra_people = 0

		for curr_shy_level, curr_crowd in enumerate(crowd):

			if curr_shy_level > standing_people:
				extra_people += 1
				standing_people += 1

			standing_people += curr_crowd

		return extra_people




	shy_people = case[1]

	return count_min_people_necessary(shy_people)


input_file = open('A-large.in', 'r+')
text = input_file.readlines()

text = [x.replace('\n','') for x in text]

num_cases = int(text[0]) # get case number from header row

del text[0] # delete header row


if num_cases is not 0:

	formatted_input = []

	for idx, case in enumerate(text):

		curr_line = case
		curr_line = curr_line.split(' ')
		curr_line[0] = int(curr_line[0])
		curr_line_int_array = []

		for char in curr_line[1]:
			char = int(char)
			curr_line_int_array.append(char)
			# [int(char) for char in curr_line]

		del curr_line[1]
		curr_line.append(curr_line_int_array)

		formatted_input.append(curr_line)


	output_file = open("output.txt","w")
	for idx, case in enumerate(formatted_input):
		case_solution = solve_case(case)
		output_file.write('Case #' + str(idx + 1) + ': ' + str(case_solution) + '\n')

	output_file.close()