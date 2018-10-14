def is_tidy(input):
	in_str = str(input)
	for i in range(1, len(in_str)):
		if int(in_str[i]) < int(in_str[i-1]):
			return False
	return True 

def find_largest_tidy(input):
	pos = -1
	while not is_tidy(input):

		input = (int(str(input)[:pos])-1) * (10**abs(pos)) + int('9'*abs(pos))
		pos -= 1
	return input

in_file = 'B-large.in'
out_file = 'B-large.out'

file = open(in_file, 'r')
problems_num = int(file.readline())
problems = []
for i in xrange(problems_num):
	problems.append(int(file.readline()))

solutions = []

for i in xrange(problems_num):
	solutions.append(find_largest_tidy(problems[i]))
	

output = open(out_file, 'w')

for i in xrange(len(solutions)):
	output.write('Case #' + str(i+1) + ': ' + str(solutions[i]) + '\n')