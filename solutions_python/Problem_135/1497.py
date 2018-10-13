

from sys import stdin


T = int(stdin.readline())

for t in range(1, T+1):
	s1 = set()
	s2 = set()
	r1 = int(stdin.readline())
	for y in range(4):
		s = stdin.readline().strip('\n')
		if y == r1-1:
			s1 = set(s.split(' '))
	r2 = int(stdin.readline())
	for y in range(4):
		s = stdin.readline().strip('\n')
		if y == r2-1:
			s2 = set(s.split(' '))
	inter = s1 & s2
	if len(inter) == 1:
		print 'Case #' + str(t) + ': ' + str(list(inter)[0])
	elif len(inter) == 0:
		print 'Case #' + str(t) + ': ' +  'Volunteer cheated!' 
	else:
		print 'Case #' + str(t) + ': ' +  'Bad magician!'


		
