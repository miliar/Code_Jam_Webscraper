from itertools import islice
from functools import reduce

def parse_lines(lines) :
	return map(lambda s : problem_parse_line(s.strip()), 
		islice(lines, 1, None))

def format_solution(case, solution) :
	return f'Case #{case}: {solution}'

def problem_parse_line(line) :
	return int(line)

def solve(N) :
	digits = [int(d) for d in str(N)]
	
	def last_increasing() :
		for i in range(len(digits) - 1) :
			if digits[i + 1] < digits[i] :
				return digits.index(digits[i])
		return -1

	def digits_to_num() :
		return reduce(lambda x,y : 10*x+y, digits)

	pivot = last_increasing()
	if pivot != -1 :
		digits = digits[:pivot] + [digits[pivot]-1] + [9]*len(digits[pivot+1:])
	return digits_to_num()


sol_file = open('solved_large.txt', 'w')
with open('B-large.in') as lines :
	for case, N in enumerate(parse_lines(lines), start=1) :
		print(format_solution(case, solve(N)), file=sol_file)
