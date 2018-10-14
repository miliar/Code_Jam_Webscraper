from math import floor, ceil

number = raw_input()

def parseInput(example):
	stripped_example = example.strip()
	l = stripped_example.split(" ")
	return(int(l[0]), int(l[1]))

def split(free_spaces, people_left):
	if not free_spaces:
		return (0, 0)
	best = max(free_spaces)
	L = int(floor((best - 1)/2.0))
	R = int(ceil((best - 1)/2.0))

	trim_count = min(people_left - 1, free_spaces[best])

	free_spaces[best] -= trim_count
	if(free_spaces[best] == 0):
		del free_spaces[best]
	if(L != 0):
		if(L not in free_spaces):
			free_spaces[L] = 0
		free_spaces[L] += trim_count
	if(R != 0): 
		if(R not in free_spaces):
			free_spaces[R] = 0
		free_spaces[R] += trim_count
	return(max(R, L), min(L, R), trim_count)

def solve(example):
	(size, people) = parseInput(example)
	free_spaces_sizes = dict()
	free_spaces_sizes[size] = 1
	while people > 1:
		(_, _, trimmed) = split(free_spaces_sizes,people)
		people -= trimmed
	rez = split(free_spaces_sizes,1)
	return rez


for n in xrange(int(number)):
	example = raw_input()
	sol = solve(example)
	print "Case #" + str(n + 1) +":",sol[0],sol[1]