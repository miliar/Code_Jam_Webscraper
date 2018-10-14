number = raw_input()

def parseInput(example):
	stripped_example = example.strip()
	return map(int, stripped_example.split(" "))

def solve(N, Q, horses, connections, quests):
	pos = 0
	current_horse = 0
	left_energy = horses[current_horse][0]
	times = [-1] * N
	times[N - 1] = 0
	for i in range(N - 2, -1, -1):
		best_time = times[i]
		dist = 0
		dest = i
		while dest < N - 1:
			dist += connections[dest][dest + 1]
			dest += 1
			if(dist > horses[i][0]):
				break
			if(best_time == -1):
				best_time = times[dest] + float(dist)/horses[i][1]
			else:
				best_time = min(best_time, times[dest] + float(dist)/horses[i][1])
		times[i] = best_time
	return times[0]


for n in xrange(int(number)):
	example = raw_input()
	(N, Q) = parseInput(example)
	horses = []
	for i in range(N):
		(E, S) = parseInput(raw_input())
		horses.append((E,S))
	connections = []
	for i in range(N):
		connections.append(parseInput(raw_input()))

	quests = []
	for q in range(Q):
		(U, V) = parseInput(raw_input())
		quests.append((U, V))

	print "Case #" + str(n + 1) +": " + str(solve(N, Q, horses, connections, quests))