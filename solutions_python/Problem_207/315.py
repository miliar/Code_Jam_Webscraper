def get_largest(unicorns):
	return sorted(unicorns, key=lambda tup: tup[1])

def match_colors(insert, prev):
	if not prev:
		return False
	for c in list(insert[0]):
		if c in list(prev[0]):
			return True
	return False

def reduce_type(unicorns, insertion):
	for i, u in enumerate(unicorns):
		if u[0] == insertion[0]:
			unicorns[i] = (u[0], u[1] - 1, u[2])
			return


def solve_case(N, R, O, Y, G, B, V):
	result = ""
	unicorns = [('R', R, 'R'), ('RY', O, 'O'), ('Y', Y, 'Y'), ('YB', G, 'G'),('B', B, 'B') ,('BR', V, 'V')]
	prev = None
	for i in range(N):
		insertion = None
		ordered = get_largest(unicorns)
		if i == N - 2:
			u1 = ordered.pop()
			u2 = ordered.pop()
			if u2[1] < 1:
				return "IMPOSSIBLE"
			if match_colors(u1, prev) and match_colors(u1, first):
				return "IMPOSSIBLE"
			elif match_colors(u1, prev) and match_colors(u2, prev):
				return "IMPOSSIBLE"
			elif match_colors(u1, prev) and not match_colors(u2, prev) and not match_colors(u1, first):
				insertion = u2
			elif match_colors(u2, first) and not match_colors(u1, first) and not match_colors(u2, prev):
				insertion = u2
			else:
				insertion = None
				ordered = get_largest(unicorns)


		while not insertion:
			if len(ordered) == 0:
				return "IMPOSSIBLE"
			insertion = ordered.pop()
			if insertion[1] == 0 or match_colors(insertion[0], prev):
				insertion = None

		result += insertion[2]
		reduce_type(unicorns, insertion)
		prev = insertion
		if i == 0:
			first = insertion

	if match_colors(first, insertion):
		return "IMPOSSIBLE"
	return result

with open("B-small-attempt1.in", "r") as dataset:
	nb_cases = int(dataset.readline().rstrip("\n"))
	out = []
	for i in range(nb_cases):
		N, R, O, Y, G, B, V = [int(x) for x in dataset.readline().rstrip("\n").split(' ')]
		out.append("Case #" + str(i + 1) + ': ' + solve_case(N, R, O, Y, G, B, V))


with open("result.txt", "w+") as output_file:
		for line in out:
			output_file.write(line + "\n")