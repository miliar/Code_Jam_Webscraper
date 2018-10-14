def calculate(inital_positions, speeds, dest):
	min_time = 0
	dest = float(dest)
	for x in xrange(0,len(initial_positions)):
		initial_pos = float(inital_positions[x])
		speed = float(speeds[x])
		time = (dest - initial_pos) / speed
		if time > min_time:
			min_time = time
	return dest / min_time
	"""
	print min_time
	print 'dest', dest
	print 'pos', inital_positions
	print "speed", speeds
	"""

initial_positions = []
speeds = []
count = 0
case_count = 1

fh = open('A-large.in', 'r')
fwh = open('result.large.ouput', 'w+')
first_line = True


for line in fh:
	if first_line:
		num_cases = int(line.strip())
		first_line = False
	else:
		if count == 0:
			destination = int(line.strip().split()[0])
			num_of_horses = int(line.strip().split()[1])
			count += 1
		else:
			initial_position = initial_positions.append(int(line.strip().split()[0]))
			speed = speeds.append(int(line.strip().split()[1]))
			if count == num_of_horses:
				ans = calculate(initial_positions, speeds, destination)
				fwh.write('Case #' + str(case_count) + ': ' + str(ans) + '\n')
				initial_positions = []
				speeds = []
				count = 0
				case_count += 1
			else:
				count += 1