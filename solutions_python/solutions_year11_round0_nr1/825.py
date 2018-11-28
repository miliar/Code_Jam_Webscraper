T = int(raw_input())

for t in range(T):
	arr = raw_input().split(" ")[1:]
	robot = arr[::2]
	button = arr[1::2]	
	l = len(robot)
	o_steps = b_steps = 0
	o_pos = b_pos = 1
	for i in xrange(l):
		if robot[i] == 'O':
			o_steps += abs(int(button[i]) - o_pos) + 1
			if o_steps <= b_steps:
				o_steps = b_steps + 1
			o_pos = int(button[i])
 		else:
			b_steps += abs(int(button[i]) - b_pos) + 1
			if b_steps <= o_steps:
				b_steps = o_steps + 1
			b_pos = int(button[i])
	print "Case #%d: %d" % (t+1,max(b_steps, o_steps))