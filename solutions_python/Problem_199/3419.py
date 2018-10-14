def mod_parent(parent, idx, width):
	result = []
	result += parent[:idx]
	for i in xrange(width):
		#print parent
		#print len(parent)
		result += [int(not parent[idx+i])]
	result += parent[idx+width:]
	return result

def solve_this(problem):
	pancakes = problem[0]
	width = problem[1]
	branching_factor = len(pancakes) - width + 1

	depth = 1
	children = [[[1]*len(pancakes), 0]]
	added = True

	while len(children) < 2**len(pancakes) and added:
		added = False
		for sol in children:
			if sol[0] == pancakes:
				return sol[1]
		for parent in filter(lambda x: True if x[1] is depth-1 else False, children):
			for i in xrange(branching_factor):
				temp = [mod_parent(parent[0], i, width), depth]
				if temp[0] not in [x[0] for x in children]:
					added = True
					children.append(temp)
		depth += 1

	"""
	def generate_children(parent):
		for i in xrange(branching_factor):
			generate_children(mod_parent(parent, i, width))
	generate_children(pancakes)
	"""
	return 'IMPOSSIBLE'
	

filename = 'A-small-attempt0'
in_filename = filename + '.in'
out_filename = filename + '.out'

in_file = open(in_filename, 'r')

problems_num = int(in_file.readline())
problems = []

for i in xrange(problems_num):
	curr_problem = in_file.readline().split()
	problems.append([ map(lambda x: 0 if x is '-' else 1, curr_problem[0]), int(curr_problem[1]) ])

solutions = []
for p in problems:
	#print p
	solutions.append(solve_this(p))

out_file = open(out_filename, 'w')

for i, solution in enumerate(solutions):
	out_file.write('Case #' + str(i+1) + ': ' + str(solution) + '\n')

print 'done'

