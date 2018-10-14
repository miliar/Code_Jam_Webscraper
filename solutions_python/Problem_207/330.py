from random import choice
number = raw_input()

def parseInput(example):
	stripped_example = example.strip()
	return map(int, stripped_example.split(" "))

def solve(N, unicorns):
	sol = []
	multicolor_options = {'O': 'B', 'G': 'R', 'V': 'Y'}
	number_of_multicolor_types = 0
	single_type = None
	for m in multicolor_options:
		if unicorns[m] > 0:
			number_of_multicolor_types += 1
			single_type = m
	if number_of_multicolor_types == 1:
		if(unicorns[single_type] == unicorns[multicolor_options[single_type]]):
			sol = [multicolor_options[single_type], single_type]*unicorns[single_type]
			return ''.join(sol)
	else:
		single_type = None

	for m in multicolor_options:
		if unicorns[m] > 0 and (unicorns[multicolor_options[m]] < unicorns[m] + 1):
			return 'IMPOSSIBLE'

	last = None
	count = N
	for m in multicolor_options:
		if unicorns[m] > 0:
			sol.append(multicolor_options[m])
			unicorns[multicolor_options[m]] -= 1

			sol.extend([m, multicolor_options[m]] * unicorns[m])
			count -= unicorns[m]*2 + 1
			unicorns[multicolor_options[m]] -= unicorns[m]
			unicorns[m] = 0

			last = multicolor_options[m]

	last = None
	for i in range(N):
		selection = ['R', 'Y', 'B']
		selection = (sorted(selection, key=lambda x:unicorns[x]))[::-1]
		for x in selection:
			if x != last and unicorns[x] != 0:
				sol.append(x)
				last = x
				unicorns[x] -= 1
				break;
	if len(sol) == N and sol[len(sol) - 1] != sol[0]:
		return ''.join(sol)
	if len(sol) == N and sol[len(sol) - 1] == sol[0]:
		problem = sol[0]
		selection = ['R', 'Y', 'B']
		for i in range(N - 1):
			if sol[i] in selection and sol[i + 1] in selection and sol[i] != problem and sol[i + 1] != problem:
				sol = sol[:i + 1] + [problem] + sol[i + 1:N - 1]
				return ''.join(sol)
	return 'IMPOSSIBLE'



for n in xrange(int(number)):
	example = raw_input()
	(N, R, O, Y, G, B, V) = parseInput(example)
	unicorns = {'R' : R,
	'G': G,
	'B': B,
	'O': O,
	'Y': Y,
	'V': V}
	print "Case #" + str(n + 1) +": " + solve(N, unicorns)
