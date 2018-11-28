def solve_small(horses, routes, N):
	paths = [[horses[0][:], 0, 0]]
	for i in range(0, N - 1):
		newPath = []	
		best = [-1 for x in horses]
		for j, p in enumerate(paths):
			if p[0][0] >= routes[i][i+1]:
				p[0][0] -= routes[i][i+1]
				p[1] += routes[i][i+1]/float(p[0][1])
				if best[p[2]] == -1 or p[1] < best[p[2]]:
					best[p[2]] = p[1]
					newPath.append(p)
				p2 = [horses[i + 1][:], p[1], i + 1]
				newPath.append(p2)
		paths = newPath[:]

	paths.sort(key=lambda tup: tup[1])
	return str(paths[0][1])


with open("C-small-attempt2.in", "r") as dataset:
	nb_cases = int(dataset.readline().rstrip("\n"))
	out = []
	for i in range(nb_cases):
		N, Q = [int(x) for x in dataset.readline().rstrip("\n").split(' ')]
		horses = []
		for j in range(N):
			horses.append([int(x) for x in dataset.readline().rstrip("\n").split(' ')])
		routes = []
		for j in range(N):
			routes.append([int(x) for x in dataset.readline().rstrip("\n").split(' ')])
		res = "Case #" + str(i + 1) + ': ' + str(solve_small(horses, routes, N))
		dataset.readline()
		out.append(res)

with open("result.txt", "w+") as output_file:
		for line in out:
			output_file.write(line + "\n")