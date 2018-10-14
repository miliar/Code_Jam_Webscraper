def solve_problem(case_number):
	solution_number = ''
	prev = '0'
	dup = 0
	index = 0
	total_length = len(case_number)
	for current in case_number:
		if current > prev:
			solution_number += (prev * dup)
			prev = current
			dup = 1
		elif current == prev:
			dup += 1
		else:
			lower_prev = chr(ord(prev)-1)
			if lower_prev is not '0':
				solution_number += lower_prev
			solution_number += '9' * (total_length - index + dup - 1)
			dup = 0
			break
		index += 1
	solution_number += (prev * dup)
	return solution_number

def get_parameters():
	return raw_input().split()

def get_case_input():
	parameters = get_parameters()
	case_number	= str(parameters[0])
	return case_number,

def print_result(index, result):
	print("Case #{0}: {1}".format(index+1, str(result)))

def process():
	t = input()
	for i in xrange(t):
		args = get_case_input()
		case_result = solve_problem(*args)
		print_result(i, case_result)

if '__main__' == __name__:
	process()
