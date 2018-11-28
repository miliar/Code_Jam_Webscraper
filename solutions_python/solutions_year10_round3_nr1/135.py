def isIntersect(a1, b1, a2, b2):
	slope1 = b1 - a1
	slope2 = b2 - a2
	if slope1 == slope2:
		return False
	elif slope1 * slope2 >= 0:
		return (b2 - b1 > 0 and a1 - a2 > 0) or (b1 - b2 > 0 and a2 - a1 > 0)
	else:
		return (a1 > a2 and a1 <= b2) or (a1 < a2 and a1 >= b2) or (a2 > a1 and a2 <= b1) or (a2 < a1 and a2 >= b1)

T = int(raw_input().strip())
T_counter = 1
while T_counter <= T:
	N = int(raw_input().strip())
	N_counter = 0
	pos = list()
	while N_counter < N:
		line = raw_input().strip().split(' ')
		pos.append([int(line[0]), int(line[1])])
		N_counter = N_counter + 1
	ans = 0
	i = 0
	while i < N - 1:
		j = i + 1
		while j < N:
			if isIntersect(pos[i][0], pos[i][1], pos[j][0], pos[j][1]):
				ans = ans + 1
			j = j + 1
		i = i + 1
	print "Case #%d: %d" % (T_counter, ans)
	T_counter = T_counter + 1
	
		
