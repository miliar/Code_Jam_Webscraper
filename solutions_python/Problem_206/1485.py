def solve_problem(D, N, K, S):
	max_time = 0
	for i in xrange(N):
		current_time = float((D-K[i]))/S[i]
		if max_time < current_time:
			max_time = current_time

	return float(D) / max_time,

def format_solution(max_speed):
	return "{0}".format(max_speed)

def get_parameters():
	return raw_input().split()

def get_case_input():
	parameters = get_parameters()
	D	= int(parameters[0])
	N	= int(parameters[1])
	K = []
	S = []
	for i in xrange(N):
		parameters = get_parameters()
		K.append(int(parameters[0]))
		S.append(int(parameters[1]))
	return D, N, K, S

def print_result(index, result):
	print("Case #{0}: {1}".format(index+1, str(result)))

def process():
	t = input()
	for i in xrange(t):
		args = get_case_input()
		case_result = solve_problem(*args)
		formatted_result = format_solution(*case_result)
		print_result(i, formatted_result)

if '__main__' == __name__:
	process()
