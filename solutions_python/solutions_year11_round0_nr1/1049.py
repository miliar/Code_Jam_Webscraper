lines = open('A-large.in').readlines()[1:]
case = 0
for line in lines:
	case += 1
	items = line.split()[1:]

	robots_todos = {'O': [], 'B': []}
	for item in items:
		if item == 'O' or item == 'B':
			robot = item
		else:
			robots_todos[robot].append(int(item))

	items.reverse()
	spent_time = 0
	robot_pos = {'O': 1, 'B': 1}
	opposite = {'O': 'B', 'B': 'O'}
	while items:
		robot = items.pop()
		button = int(items.pop())
		this_spent_time = abs(robot_pos[robot] - button) + 1
		robot_pos[robot] = button
		robots_todos[robot] = robots_todos[robot][1:]
		spent_time += this_spent_time

				
		another = opposite[robot]
		if robots_todos[another]:
			distance = robots_todos[another][0] - robot_pos[another]
			if this_spent_time >= abs(distance):
				robot_pos[another] = robots_todos[another][0]
			else:
				robot_pos[another] += cmp(distance, 0) * this_spent_time

	print "Case #%d: %d" % (case, spent_time)
