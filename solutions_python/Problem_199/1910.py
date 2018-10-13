GOOD_STATE	= '+'
BAD_STATE	= '-'

FLIP_XOR = ord(GOOD_STATE) ^ ord(BAD_STATE)

def switch_state(state):
	return chr(ord(state) ^ FLIP_XOR)

def get_amount_of_flips(current_state, k):
	current_state = list(current_state)
	s = len(current_state)
	flips = 0

	for i in xrange(s-k+1):
		if BAD_STATE == current_state[i]:
			flips += 1
			for j in xrange(k):
				current_state[i+j] = switch_state(current_state[i+j])

	if BAD_STATE in current_state:
		return "IMPOSSIBLE"
	return flips

def get_case_input():
	parameters = raw_input().split()
	initial_state	= str(parameters[0])
	k 				= int(parameters[1])
	return initial_state, k

def print_result(index, result):
	print("Case #{0}: {1}".format(index+1, result))

def process():
	t = input()
	for i in xrange(t):
		initial_state, k = get_case_input()
		case_result = get_amount_of_flips(initial_state, k)
		print_result(i, case_result)

if '__main__' == __name__:
	process()
