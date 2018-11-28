


def solve(buttons):
	time = 0
	last_time = 0
	this_time = 0
	last_bot = None
	position = {'O': 1, 'B' : 1}
	for m in buttons:
		bot = m[0]
		target = m[1]
#		print bot, target
		if bot != last_bot:
#			print this_time, last_time
#			print "Bot changed to %s"  % bot
			time += this_time
			last_time = this_time
			this_time = 0
			last_bot = bot
		time_to_move = abs(target - position[bot])
#		print "Time to move %d" % time_to_move
		position[bot] = target
		if last_time:
			if time_to_move > last_time:
				# Only add the excess movement time
				this_time += time_to_move - last_time
			last_time = 0
		else:
			this_time += time_to_move
		this_time += 1
	time += this_time
	return time
	
T = int(raw_input())
for case in xrange(1, T + 1):
	line = raw_input().split()
	N = int(line[0])
	del line[0]
	buttons = [(line[2 * idx], int(line[2 * idx + 1])) for idx in xrange(0, N)]
#	print buttons
	ans = solve(buttons)
	print "Case #%d: %s" % (case, ans)