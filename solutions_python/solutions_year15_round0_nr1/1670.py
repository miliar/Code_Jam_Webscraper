import sys

def solve(smax,ppl):
	smax = int(smax)
	audience = []
	for char in ppl:
		audience.append(int(char))

	if smax == 0: 
		return 0 

	clappers = 0
	friends = 0
	for alevel in range(0,smax+1): 
		if clappers <= alevel: 
			# print alevel, clappers, friends
			friends += (alevel - clappers)
			clappers = alevel + audience[alevel]
			# print alevel, clappers, friends
		else: 
			clappers += audience[alevel]

	return friends


if __name__ == '__main__':
	if len(sys.argv) >= 2:
		fi = sys.argv[1]
		fo = sys.argv[2]
		# run from CLI, 2nd argument is input filename. 3rd is output filename. 

		solutions = []

		with open(fi , 'r') as infile: 
			# with open(fn) recommended b/c it handles file opening and closing
			n_cases = int(infile.readline())
			# read the first line to get number of test cases

			for case in range(n_cases):
				x, y = infile.readline().split()
				solutions.append(solve(x,y))
				
	# print solve('5','110011')
	# print solve('2', '2001')
	# print solve('6', '2001221')
	# print solve('4','21002')

		with open(fo, 'w+') as outfile:
			for n_case, solution in enumerate(solutions): 
				outfile.write("Case #" + str(n_case+1) + ": " + str(solution) + "\n")




