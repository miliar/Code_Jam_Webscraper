def solve_problem(n, k):
	occupied = [0, n+1]
	for i in xrange(k):
		current_best = 0
		current_min = 0
		current_max = 0
		best_index = 0
		for s in xrange(len(occupied) - 1):
			temp_best = (occupied[s+1]+occupied[s])/2
			temp_min = temp_best-occupied[s]
			temp_max = occupied[s+1]-temp_best
			if (temp_min > current_min) or (temp_min == current_min and temp_max > current_max):
				current_best = temp_best
				current_min = temp_min
				current_max = temp_max
				best_index = s
		occupied.insert(best_index+1, current_best)
	return "{0} {1}".format(current_max-1, current_min-1)


def get_parameters():
	return raw_input().split()

def get_case_input():
	parameters = get_parameters()
	n	= int(parameters[0])
	k	= int(parameters[1])
	return n, k

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
