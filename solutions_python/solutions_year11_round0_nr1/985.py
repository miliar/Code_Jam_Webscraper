#!/usr/bin/python

T = int(raw_input())
for case in range(1, T + 1):
	series = raw_input().split()
	time = 0
	pos = {'O' : 1, 'B' : 1}
	other = {'O' : 'B', 'B' : 'O'}
	
	timeDiff = -1
	i = 0
	del series[0]
	while i < len(series) / 2:
		[color, switch] = [series[2 * i], int(series[2 * i + 1])]
		
		# Since the opposite color just moved, do as much as possible during
		# his move
		if timeDiff != -1:
			timeDiff = max(abs(switch - pos[color]) - timeDiff, 0) + 1
		else:
			timeDiff = abs(switch - pos[color]) + 1
		pos[color] = switch
		
		j = i + 1
		while j < len(series) / 2 and series[2 * j] == color:
			timeDiff = timeDiff + abs(int(series[2 * j + 1]) - pos[color]) + 1
			pos[color] = int(series[2 * j + 1])
			j += 1
		
		time = time + timeDiff
		i = j
	
	print "Case #" + str(case) + ": " + str(time)

