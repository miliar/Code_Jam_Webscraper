import copy, sys

def load(file):
	with open(sys.argv[1], 'r') as f:
		infile = f.read()

	infile = infile.splitlines()

	testcase_count = int(infile[0])
	infile = infile[1:]

	states = []

	for case in infile:
		case = case.split()
		states.append((case[0], case[1]))
	return states

def happy_count(state):
	count = 0
	for p in state:
		if p == '+':
			count += 1
	return count

def flip(state, spatula_sz, index):
	new_state = state[:index]
	for i in range(index, index + spatula_sz):
		new_state += '-' if state[i] == '+' else '+'
	new_state += state[index + spatula_sz:]
	return new_state

def all_happy(state):
	return all([x == '+' for x in state])

def smart_solution(state, spatula_sz):
	current_state = state
	i = 0
	flips = 0
	happy_no = prev_happy_no = 0
	while not all_happy(current_state):
		prev_happy_no = happy_no
		happy_no = happy_count(current_state)
		if prev_happy_no < happy_no:
			break
		if current_state[i] != '+':
			flips += 1
			current_state = flip(current_state, spatula_sz, i)
			i += 1
	return str(flips) if all_happy(current_state) else 'IMPOSSIBLE'

def brute_force_solution(state, spatula_sz):
	def recur(current_state):
		if current_state in states:
			return -1 if states[current_state] == -1 else (states[current_state] + 1)
		if current_state in states_stack:
			return -1
		if all_happy(current_state):
			return 0
		states_stack.add(current_state)
		result = None
		for i in range(len(current_state) - spatula_sz + 1):
			res = recur(flip(current_state, spatula_sz, i))
			if res >= 0:
				result = res if result is None else min(result, res)
		if result is None:
			result = -1
		states[current_state] = result
		states_stack.remove(current_state)
		return (result + 1) if result != -1 else result

	states = {}
	states_stack = set()
	result = recur(state)
	return 'IMPOSSIBLE' if result == -1 else str(result)

def run_test(states, index):
	testcase = states[index][0]
	spatula_sz = int(states[index][1])
	if all_happy(testcase):
		result = '0'
	elif spatula_sz == len(testcase) and any([x == '+' for x in testcase]):
		result = 'IMPOSSIBLE'
	else:
		result = brute_force_solution(testcase, spatula_sz)
		#result = smart_solution(testcase, spatula_sz)
	print('Case #{0}: {1}'.format(index + 1, result))
	
def _main(args):
	states = load(args[1])
	for i in range(len(states)):
		run_test(states, i)

if __name__ == "__main__":
	_main(sys.argv)
