"""
@author : ROUSSEAU Sylvain
@email  : sylvain (dot) rousseau93 ( at ) gmail (dot) com
"""

def write_problem(text, filename='out.txt') :
	with open(filename, 'w') as outputfile :
		outputfile.write(text)


# load input file
def read_problem(filename='in.txt') :
	testcases = []
	with open("in.txt") as inputfile :
		num_of_testcases = int(inputfile.readline())
		print "number of test case : ", num_of_testcases
		for i in range(num_of_testcases) :
			tmp = inputfile.readline()
			if tmp.endswith('\n') :
				tmp = tmp[:-1]
			testcases.append(tmp)
	return testcases

def solveProblem(problem) :
	problem = problem.split(' ')
	smax = int(problem[0])
	s = []
	for c in problem[1] :
		s.append(int(c))
	num_friends = 0
	num_ovation = 0
	for i in range(len(s)) :
		if num_ovation >= i : # no problem
			num_ovation = num_ovation + s[i]
		else :
			missing = i - num_ovation
			num_friends = num_friends + missing
			num_ovation = num_ovation + s[i] + missing
	return num_friends

problems =  read_problem()
out = ""
for i, problem in enumerate(problems) :
	out += "Case #%d: %d\n"%(i+1,solveProblem(problem))
write_problem(out)