import sys

another_robot = {'O': 'B', 'B': 'O'}

def solve(objectives):
	position = {'O': 1, 'B': 1}
	time = {'O': 0, 'B': 0}
	for objective in objectives:
		robot, place = objective

		time_interval = abs(position[robot] - place) + 1
		new_time = max(time[robot] + time_interval, time[another_robot[robot]] + 1)

		position[robot] = place
		time[robot] = new_time

	return max(time.values())

with open(sys.argv[1]) as f:
	T = int(f.readline())
	for testcase in xrange(T):
		line = f.readline().split()
		n = int(line[0])
		objectives = []
		for i in xrange(n):
			objectives.append( (line[2 * i + 1], int(line[2 * i + 2])) )
		
		answer = solve(objectives)
		
		print 'Case #%d: %d' % (testcase + 1, answer) 