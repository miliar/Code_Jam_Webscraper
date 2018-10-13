T = input()

for case in range(1, T + 1):
	qa = input()
	a = []
	for i in range(4):
		a.append(set(map(int, raw_input().split())))
	qb = input()
	b = []
	for i in range(4):
		b.append(set(map(int, raw_input().split())))

	c = a[qa - 1] & b[qb - 1]
	if len(c) == 0:
		ans = 'Volunteer cheated!'
	elif len(c) == 1:
		ans = str(list(c)[0])
	else:
		ans = 'Bad magician!'

	print 'Case #%d:' % case, ans