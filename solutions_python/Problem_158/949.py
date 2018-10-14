t = int(raw_input())
for ti in range(t):
	x, r, c = map(int, raw_input().split())
	ans = ''
	if (x == 1):
		ans = 'GABRIEL'
	elif (x == 2):
		if ((r * c) % 2 == 0):
			ans = 'GABRIEL'
		else:
			ans = 'RICHARD'
	elif (x == 3):
		if ((r == 3 and c == 2) or (r == 2 and c == 3) or (r == 3 and c == 3) or (r == 4 and c == 3) or (r == 3 and c == 4)):
			ans = 'GABRIEL'
		else:
			ans = 'RICHARD'
	elif (x == 4):
		if ((r == 4 and c == 4) or (r == 4 and c == 3) or (r == 3 and c == 4)):
			ans = 'GABRIEL'
		else:
			ans = 'RICHARD'
	print 'Case #' + str(ti + 1) + ': ' + ans