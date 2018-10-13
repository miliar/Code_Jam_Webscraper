def mov(R, state, task, next):
	if (next[R] >= len(task[R])):
		# no more goals
		return 'S'
	if (state[R] > task[R][next[R]]):
		state[R] -= 1
	elif (state[R] < task[R][next[R]]):
		state[R] += 1
	else:
		# no where to go
		return 'S'
	
	return 'M'
		
T = int(raw_input())
for _ in xrange(T):
	l = raw_input().split()
	N = int(l[0])
	Ss = 0
	state = {'O': 1, 'B': 1}
	next = {'O': 0, 'B': 0}
	move = {'O': '', 'B': ''}
	buts = []
	p = 0
	for n in xrange(0, N):
		buts.append((l[n*2+1], int(l[n*2+2])))
	task = dict()
	task['O'] = [P for R, P in buts if R == 'O']
	task['B'] = [P for R, P in buts if R == 'B']
	while p < N:
		move['O'] = mov('O', state, task, next)
		move['B'] = mov('B', state, task, next)
		(R, P) = buts[p]
		if (state[R] == P and move[R] == 'S'):
			# button pressed
			p += 1
			# set next goal for robot
			next[R] += 1
		Ss += 1
	print "Case #%d: %d" % (_+1, Ss)
	
