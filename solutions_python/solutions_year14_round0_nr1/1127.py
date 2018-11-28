import os

def solve(f_in):
	row1 = int(f_in.readline())
	board1 = []

	for i in range(4):
		board1.append([int(elem) for elem in f_in.readline().split()])

	possible_choices_1 = board1[row1 - 1]

	row2 = int(f_in.readline())
	board2 = []

	for i in range(4):
		board2.append([int(elem) for elem in f_in.readline().split()])

	possible_choices_2 = board2[row2 - 1]

	possible_choices = list(set(possible_choices_1).intersection(possible_choices_2))

	if len(possible_choices) == 0:
		return 'Volunteer cheated!'
	elif len(possible_choices) == 1:
		return str(possible_choices[0])
	else:
		return 'Bad magician!'

if __name__ == "__main__":
	input_filename = 'A-small-attempt0.in'
	output_filename = 'Qualification_ProblemA_Output.txt'

	f_in = open(input_filename)
	counter = 0
	while os.path.isfile(output_filename):
		counter += 1
		output_filename = output_filename.split('.')[0] + str(counter) + '.txt'
	f_out = open(output_filename, 'a')

	test_cases = int(f_in.readline())
	
	for i in range(test_cases):
		ans = solve(f_in)
		f_out.write('Case #' + str(i + 1) +': ' + str(ans) + '\n')

	f_in.close()
	f_out.close()

	print 'Problem completed!'




