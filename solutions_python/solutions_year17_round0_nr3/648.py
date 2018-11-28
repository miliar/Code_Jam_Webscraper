import sys


if len(sys.argv) < 2:
	print "provide input file"
	exit ()

class ProblemInstance():

	def __init__(self, n, k):
		self.n = int(n)
		self.k = int(k)

	def __str__(self):
		return self.n + " : " + str(self.k)


def load_problem():
	input_file = open(sys.argv[1])
	cases = []
	n = int(input_file.readline())
	for i in range (0, n):
		n, k = input_file.readline().split()
		cases += [ProblemInstance(n, k)]
	input_file.close()
	return cases


def divide(number, times):
	if number == 1:
		return {}
	if number == 2:
		return {1 : times}
	if number % 2 == 0:
		return {number/2 : times, number/2-1 : times}
	else:
		return {number/2: 2 * times}

def min_distance(number):
	if number % 2 == 0:
		return number/2 - 1
	return number/2

def max_distance(number):
	return number/2

def solve(case):
	n = case.n
	k = case.k
	solution = {n:1}
	m1 = 0
	m2 = 0
	while k > 0:
		# print solution
		# print k
		largest = max(solution.keys())
		largest_problems = solution[largest]
		times = min(k, largest_problems)
		if times == largest_problems:
			solution.pop(largest)
		divided = divide(largest, times)
		for i, j in divided.iteritems():
			solution[i] = solution[i] + j if i in solution else j
		k -= times
		m1 = min_distance(largest)
		m2 = max_distance(largest)
	# print solution
	# print k
	return(m2, m1)
	

def compute_output():
	cases = load_problem()
	output = open(sys.argv[1] + ".out", "w")
	for i in range(0, len(cases)):
		res = solve(cases[i])
		output.write("Case #{}: {} {}\n".format(i + 1, res[0], res[1]))
	output.flush()
	output.close()


if __name__ == "__main__":
	compute_output()
