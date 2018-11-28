t = int(input())
for i in range(0, t):
	n, k = [int(x) for x in input().split()]
	snappers = [False] * n
	power = False
	for i2 in range(0, k):
		power = True
		for i3 in range(0, n):
			power = snappers[i3]
			snappers[i3] = not snappers[i3]
			if not power:
				break
	
	print('Case #{0}: {1}'.format(i + 1, 'ON' if snappers == [True] * n else 'OFF'))
