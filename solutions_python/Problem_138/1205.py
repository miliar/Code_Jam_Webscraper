
def read_input(filename):
	f = open(filename)
	T = int(f.readline())

	test_cases = [None] * T

	for i in range(T):
		N = f.readline()
		test_cases[i] = [None, None]
		test_cases[i][0] = [float(x) for x in f.readline().split()]
		test_cases[i][1] = [float(x) for x in f.readline().split()]

	return test_cases

def solve_war(first, second):
	first = sorted(first)
	second = sorted(second)

	i = 0
	j = 0

	loss = 0

	while i < len(first) and j < len(second):
		if first[i] < second[j]:
			loss += 1
			i += 1
			j += 1
		else:
			j += 1

	win = len(first) - loss

	return win

def solve_case(test_case):
	win_first = solve_war(test_case[0], test_case[1])
	win_second = solve_war(test_case[1], test_case[0])
	return (len(test_case[0]) - win_second, win_first)

def solve(testid):
	inputfile = testid + '.in'
	outputfile = testid + '.out'

	test_cases = read_input(inputfile)

	results = [None] * len(test_cases)

	g = open(outputfile, 'w')

	for i in range(len(test_cases)):
		results[i] = solve_case(test_cases[i])
		print results[i]

		g.write('Case #{}: {} {}\n'.format(i+1, results[i][0], results[i][1]))

	g.close()


if __name__ == '__main__':
#	solve('sample')
#	solve('D-small-attempt0')
	solve('D-large')


