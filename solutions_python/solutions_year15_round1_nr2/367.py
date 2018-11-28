for case in range(int(raw_input())):
	line = raw_input().split(' ')
	num_barbers = int(line[0])
	pos = int(line[1])
	waits = map(int, raw_input().split(' '))
	orig_waits = waits[:]
	current = len(waits)
	barber_order = []
	barber_index = -1
	while True:
		min_time = min(waits)
		for index in range(len(waits)):
			waits[index] -= min_time
		done = True
		for index in range(len(waits)):
			if waits[index] == 0:
				barber_order.append(index)
				waits[index] = orig_waits[index]
			else:
				done = False
		if done:
			break
	print 'Case #%d: %d' % (case + 1, barber_order[(pos-current - 1) % len(barber_order)] + 1)
