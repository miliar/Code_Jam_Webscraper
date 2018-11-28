import sys
#sys.stdin = open ('A-small.in')
#sys.stdout = open ('A-small.out', 'w')

T = input ()
for i in xrange (T):
	test = raw_input ().split ()
	n = int (test[0])
	robots = test[1::2]
	buttons = map (int, test[2::2])
	leeway = 0
	time, posO, posB, hallway = 0, 1, 1, -1
	for robot, button in zip (robots, buttons):
		if robot == hallway:
			if robot == 'O':
				time += abs (posO - button) + 1
				leeway += abs (posO - button) + 1
				posO = button
			else:
				time += abs (posB - button) + 1
				leeway += abs (posB - button) + 1
				posB = button
		else:
			if robot == 'O':
				time += max (0, abs (posO - button) - leeway) + 1
				leeway = max (0, abs (posO - button) - leeway) + 1
				posO = button
			else:
				time += max (0, abs (posB - button) - leeway) + 1
				leeway = max (0, abs (posB - button) - leeway) + 1
				posB = button
			hallway = robot
			
	print 'Case #{}: {}'.format (i + 1, time)
