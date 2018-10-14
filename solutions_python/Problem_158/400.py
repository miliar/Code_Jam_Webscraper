f = open('D-small-attempt0.in', 'r')
o = open('omino.out', 'w')

T = int(f.readline().strip('\n'))
for _ in range(T):
	X, R, C = map(int, f.readline().strip('\n').split(' '))

	answer = ''
	if R*C % X != 0:
		answer = 'RICHARD'
	else:
		if X < 3:
			answer = 'GABRIEL'
		elif X == 3:
			if R > 1 and C > 1:
				answer = 'GABRIEL'
			else:
				answer = 'RICHARD'
		elif X == 4:
			if R > 2 and C > 2:
				answer = 'GABRIEL'
			else:
				answer = 'RICHARD'

	o.write('Case #' + str(_+1) +': ' + answer + '\n')