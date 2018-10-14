import sys

def main():
	in_file           = open(sys.argv[1], 'r')
	in_file_str       = in_file.read()
	in_file_list      = in_file_str.split('\n')
	
	out_file          = open('magic_trick.txt', 'w')
	
	num_test_cases    = int(in_file_list[0])
	case_counter      = 1
	in_file.close()
	
	for i in xrange(1, len(in_file_list) - 1, 10):
		counter = 0
		volunteer_first_ans = int(in_file_list[i])
		first_ans_row       = map(int, in_file_list[i + volunteer_first_ans].split())
		
		volunteer_second_ans = int(in_file_list[i + 5])
		second_ans_row       = map(int, in_file_list[i + 5 + volunteer_second_ans].split())

		for j in xrange(4):
			for k in xrange(4):
				if first_ans_row[j] == second_ans_row[k]:
					number   = str(first_ans_row[j])
					counter += 1
		if counter == 0:
			output_str = 'Volunteer cheated!'
		elif counter > 1:
			output_str = 'Bad magician!'
		elif counter == 1:
			output_str = number
		
		out_file.write('Case #' + str(case_counter) + ': ' + output_str + '\n')
		case_counter += 1
	out_file.close()

if __name__ == "__main__":
	main()
		
					          

