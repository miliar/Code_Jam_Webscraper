import sys

filename = sys.argv[1]

# Get other robot's name
def other(who):
	return {'O': 'B', 'B': 'O'}[who]

# Cut off case count
caselines = open(filename).readlines()[1:]

for case_no, line in enumerate(caselines, 1):

	# Cut off step num
	case = line.split()[1:]

	# steps of format [('O',2), ('B',4), ...]
	steps = zip(case[::2], map(int, case[1::2]))

	pos = {'O': 1, 'B': 1}   # Starting postion
	free = {'O': 0, 'B': 0}  # No. of "free" steps (parallel to needed steps of other)

	time_sum = 0             # Result

	for who, dest in steps:

		walk_time = abs(pos[who]-dest)
		time_used = max(0, walk_time - free[who]) + 1  # Walk time - "free" time + button press
		free[other(who)] += time_used                  # Other one can move in parallel
		
		free[who] = 0
		pos[who] = dest      # Update postion
		last = who           # Update who moved last
		
		time_sum += time_used  # Add used time
		
	print "Case #%d: %d" % (case_no, time_sum)
