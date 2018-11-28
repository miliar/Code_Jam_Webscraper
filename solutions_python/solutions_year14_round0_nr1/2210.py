def get_line():
	a = int(raw_input())
	for i in range(4):
		if i+1 == a:
			line = [int(s.strip()) for s in raw_input().split()]
		else:
			raw_input()

	return line

T = int(raw_input())

for t in range(T):
	l1 = get_line()
	l2 = get_line()
	
	r = [i for i in l1 if i in l2]
	if not r:
		res = 'Volunteer cheated!'
	elif len(r) > 1:
		res = 'Bad magician!'
	else:
		res = r[0]

	print 'Case #%d: %s' % (t+1, res)