in_file = open('in.txt', 'r')
out_file = open('out.txt', 'w')

case_size = int(in_file.readline())

for i in range(case_size):
	case_input = in_file.readline().split()[1]
	case_sum = 0
	case_result = 0

	for j in range(len(case_input)):
		current_number = int(case_input[j])
		
		if current_number == 0:
			continue

		if j <= case_sum:
			case_sum += current_number
		else:
			current_extra = j - case_sum 
			case_sum += current_extra + current_number
			case_result += current_extra

	out_file.write('Case #' + str(i + 1) + ': ' +  str(case_result) + '\n')
