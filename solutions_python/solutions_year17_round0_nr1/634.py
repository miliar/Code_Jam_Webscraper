import sys


if len(sys.argv) < 2:
	print "provide input file"
	exit ()

class ProblemInstance():

	def __init__(self, pancakes, k):
		self.pancakes = pancakes
		self.k = int(k)

	def __str__(self):
		return self.pancakes + " : " + str(self.k)

def load_problem():
	input_file = open(sys.argv[1])
	cases = []
	n = int(input_file.readline())
	for i in range (0, n):
		pancakeString, k = input_file.readline().split()
		cases += [ProblemInstance(pancakeString, k)]
	input_file.close()
	return cases


# group is flippable if the minus group is entirelly to the left
def is_flippable(pancake_list):
	return pancake_list[0] == '-'
	# first_plus = len(pancake_list) - 1
	# has_minuses = False
	# for i in range(0, len(pancake_list)):
	# 	if pancake_list[i] == '+':
	# 		if first_plus > i:
	# 			first_plus = i
	# 	else:
	# 		has_minuses = True
	# 		if i > first_plus:
	# 			return False
	# return has_minuses


# flips the pancake string starting at a given index 
def flip_index(case, index):
	new_str = ""
	ind_range = range(index, index + case.k)
	for i in range(0, len(case.pancakes)):
		if i in ind_range:
			if case.pancakes[i] == '+':
				new_str += '-'
			else:
				new_str += '+'
		else:
			new_str += case.pancakes[i]
	return new_str

def find_first_flippable_group(case):
	for i in range(0, len(case.pancakes) - case.k + 1):
		if is_flippable(case.pancakes[i:i+case.k]):
			return i
	return -1


def solve_case(case):
	flips = 0
	solved = False
	while not solved:
		next_flip_index = find_first_flippable_group(case)
		if next_flip_index == -1:
			solved = True
		else:
			case.pancakes = flip_index(case, next_flip_index)
			flips += 1
	if '-' not in case.pancakes:
		return str(flips)
	else:
		return "IMPOSSIBLE"

def compute_output():
	cases = load_problem()
	output = open(sys.argv[1] + ".out", "w")
	for i in range(0, len(cases)):
		output.write("Case #{}: {}\n".format(i + 1, solve_case(cases[i])))
	output.flush()
	output.close()


if __name__ == "__main__":
	compute_output()
