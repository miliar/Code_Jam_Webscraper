# Codejam Problem C: Fair And Sqaure

import math

# Define The Functions For Use In Problem

def is_palendrome(num):
	forward = str(num)
	backward = forward[::-1]
	if forward == backward:
		return True
	else:
		return False

def is_square(num):
	sqrt = int(math.sqrt(float(num)))
	if sqrt**2 == num:
		return True
	else:
		return False

def is_fair_square(num):
	if is_palendrome(num) and is_square(num):
		if is_palendrome(int(math.sqrt(float(num)))):
			return True
	return False

cj_input = open("c.txt")
cj_output = open("c_out.txt", 'w')
num_checks = int(cj_input.readline()) # Get The Number Of Fair Square Inqueries

for check_num in range(num_checks):
	case_num = check_num + 1
	case_counter = 0

	boundaries = cj_input.readline().strip().split()
	lower = int(boundaries[0])
	upper = int(boundaries[1])

	current_num = lower
	while current_num <= upper:
		case_counter += is_fair_square(current_num)
		current_num += 1

	case_string = "Case #{}: {}\n".format(case_num, case_counter)
	cj_output.write(case_string)

cj_output.close()