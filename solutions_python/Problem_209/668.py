from itertools import islice, combinations
from math import pi

def parse_lines(lines) :
	return map(lambda s : problem_parse_line(s.strip()), 
		islice(lines, 1, None))

def format_solution(case, solution) :
	return f'Case #{case}: {solution}'

def problem_parse_line(line) :
	return list(map(int, line.split()))


def solve(k, ps) :
	def max_func(ps) :
		C = sum(2 * r * h for (r,h) in ps)
		r = max(map(lambda xs : xs[0], ps))
		return r**2 + C
	return max_func(max(combinations(ps, k), key = max_func)) * pi

sol_file = open('solve_prac.txt', 'w')
with open('A-small-attempt0.in') as lines :
	n, k = 0, 0 ; ps = [] ; flag = False ; case = 1
	for (x1, x2) in parse_lines(lines) :
		if n == 0 :
			if flag :
				print(format_solution(case, solve(k, ps)), file=sol_file)
				case += 1
			else :
				flag = True
			n, k = x1, x2
			ps = []
			continue
		ps.append((x1,x2))
		n -= 1
	print(format_solution(case, solve(k, ps)), file=sol_file)