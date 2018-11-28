name='practice.in'
file = open(name, 'r')
cases = file.readline()
cases = int(cases)
for x in range(0, cases):
	line = file.readline()
	b = line.split(' ')
	seconds = 0;
	actions = int(b[0])
	robots = {'O':1,'B':1}
	pressed = 0
	'''for a in range(1, actions+1):
		ref = a*2;
		robot = b[ref-1]
		pos = int(b[ref])
		buttons[robot].append(pos)'''
	while(True):
		if(pressed == actions):
			break
		seconds = seconds+1
		ref = (pressed+1)*2;
		robot = b[ref-1]
		pos = int(b[ref])
		if(robots[robot] == pos):
			pressed = pressed+1
		else:
			if(pos > robots[robot]):
				robots[robot] = robots[robot]+1
			else:
				robots[robot] = robots[robot]-1
		for k in range(pressed, actions):
			next = (k+1)*2;
			robot2 = b[next-1];
			pos2 = int(b[next])
			if(robot2 != robot):
				if(robots[robot2] != pos2):
					if(pos2 > robots[robot2]):
						robots[robot2] = robots[robot2]+1
					else:
						robots[robot2] = robots[robot2]-1
				break
		
	print 'Case #',x+1,': ',seconds
			