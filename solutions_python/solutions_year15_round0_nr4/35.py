def func(K, X, Y):
	if X > Y:
		Z = X
		X = Y
		Y = Z
	if X * Y % K != 0:
		return 'RICHARD'
	if K <= 2:
		return 'GABRIEL'
	if K == 3 and X >= 2 and Y >= 3:
		return 'GABRIEL'
	if K == 4 and X >= 3 and Y >= 4:
		return 'GABRIEL'
	if K == 5 and X >= 3 and Y >= 5:
		if X > 3 or Y > 5:
			return 'GABRIEL'
	if K == 6 and X >= 4 and Y >= 6:
		return 'GABRIEL'
	return 'RICHARD'
	
T = int(raw_input())

for t in range(T):
	K, X, Y = map(int, raw_input().split(' '))
	print 'Case #' + str(t+1) + ': ' + func(K, X, Y)
