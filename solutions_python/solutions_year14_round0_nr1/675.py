from sys import stdin

cas = int(stdin.readline())

for _ in range(1, cas+1):
	f1 = int(stdin.readline())-1
	g1 = []
	for i in range(4):
		if i == f1:
			g1 = set(stdin.readline().split())
		else:
			stdin.readline()
	f2 = int(stdin.readline())-1
	g2 = []
	for i in range(4):
		if i == f2:
			g2 = set(stdin.readline().split())
		else:
			stdin.readline()

	s = 'Case #' + str(_) + ': '
	a = g1.intersection(g2)
	if len(a) == 1:
		(e,) = a
		s += e
	elif len(a) == 0:
		s += 'Volunteer cheated!'
	else:
		s += 'Bad magician!'
	print s