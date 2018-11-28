import sys

class Answers():
	found, not_found, multiple_found = range(3)

def compare_rows(first_row, second_row):
	answer_state = Answers.not_found
	answer = 0
	for j in first_row:
		for k in second_row:
			if j == k:

				if answer_state == Answers.found: 
					return (Answers.multiple_found, 0)
				answer_state = Answers.found
				answer = j
	return (answer_state, answer)

answer_string = \
{
	Answers.not_found : "Volunteer cheated!",
	Answers.multiple_found : "Bad magician!"
}

if len(sys.argv) != 2:
	print "Usage {} <input_file_name>".format(sys.argv[0])
	sys.exit()

input_file = open(sys.argv[1], 'r')
input_data = input_file.read().split('\n')
input_file.close()


num_of_test_cases = int(input_data[0])

TABLE_LENGTH = 4
TEST_CASE_LENGTH = 1 + TABLE_LENGTH + 1 + TABLE_LENGTH

for i in xrange(num_of_test_cases):
	curr_place = 1 + i * TEST_CASE_LENGTH
	first_ans = int(input_data[curr_place]) - 1
	first_chosen_row = input_data[curr_place + 1 + first_ans]

	curr_place = 1 + i * TEST_CASE_LENGTH + TABLE_LENGTH + 1
	second_ans = int(input_data[curr_place]) - 1	
	second_chosen_row = input_data[curr_place + 1 + second_ans]

	answer_state, answer = compare_rows(first_chosen_row.split(" "), second_chosen_row.split(" "))

	print "Case #{}: {}".format(i+1, answer if answer_state == Answers.found else answer_string[answer_state])