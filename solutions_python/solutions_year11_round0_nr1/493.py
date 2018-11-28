import sys

T = int(sys.stdin.readline())

for case in range(T):
	print "Case #%d: " % (case+1),
	
	actions = sys.stdin.readline().strip().split(' ')[1:]
	actions = [[actions[i], int(actions[i+1])] for i in range(0, len(actions), 2)]
	
#	print actions
	pos = {'O': 1, 'B': 1}
	others = {'O': 'B', 'B': 'O'}
	idle = {'O': 0, 'B': 0}
	total = 0
	for step in actions:
		robot = step[0]
		newpos = step[1]
		dist = abs(pos[robot] - newpos)
		other = others[robot]
		time = dist - idle[robot]
		if time < 0: time = 0
		time += 1
		idle[other] += time
		idle[robot] = 0
		pos[robot] = newpos
		total += time
	print total