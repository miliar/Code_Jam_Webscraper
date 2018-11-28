t = int(input())
for tt in range(1,t+1):
	x, r, c = map(int, input().split())
	if r > c:
		r, c = c, r

	if x == 1:
		ans = 'GABRIEL'
	elif x == 2:
		if r*c % 2 == 0:
			ans = 'GABRIEL'
		else:
			ans = 'RICHARD'
	elif x == 3:
		if r*c % 3 == 0 and r != 1:
			ans = 'GABRIEL'
		else:
			ans = 'RICHARD'
	elif x == 4:
		if r == c == 4 or r == 3 and c == 4:
			ans = 'GABRIEL'
		else:
			ans = 'RICHARD'

	print('Case #{}: {}'.format(tt, ans))