from itertools import islice

def parse_lines(lines) :
	return map(lambda s : problem_parse_line(s.strip()), 
		islice(lines, 1, None))

def format_solution(case, solution) :
	return f'Case #{case}: {solution}'

def problem_parse_line(line) :
	
	def pancakes_to_boolean_array(pancakes) :
		return list(map(lambda s : s == '+', pancakes))
	
	pancakes, flipper_size = line.split()
	return pancakes_to_boolean_array(pancakes), int(flipper_size)


def solve(p, f, flips = 0) :

	def flip_first() :
		p[:] = [not b for b in p[:f]] + p[f:]

	def flip_last() :
		p[:] = p[:-f] + [not b for b in p[-f:]]

	if f > len(p) :
		return flips if all(p) else'IMPOSSIBLE'

	# The 1st and last can only be flipped in one way.
	if not p[0] :
		flip_first()
		flips += 1
	if not p[-1] :
		flip_last()
		flips += 1
	
	if f == len(p) :
		return flips if all(p) else 'IMPOSSIBLE'

	return solve(p[1:-1], f, flips)

print()

sol_file = open('solved.txt', 'w')
with open('A-small-attempt2.in') as lines :
	for case, (pancakes, flipper_size) in enumerate(parse_lines(lines), start=1) :
		print(pancakes, flipper_size)
		print(format_solution(case, solve(pancakes,
				flipper_size)), file=sol_file)
