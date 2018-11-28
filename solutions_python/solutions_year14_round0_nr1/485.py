f = open('A-small-attempt0.in', 'r')
fo = open('A-small.out', 'w')

t = int(f.readline())
for ti in range(1, t + 1):
	s1 = set()
	a1 = int(f.readline()) - 1
	for i in range(4):
		data = f.readline()
		if i == a1:
			data = data.rstrip().split()
			for j in range(4):
				s1.add(int(data[j]))

	s2 = set()
	a2 = int(f.readline()) - 1
	for i in range(4):
		data = f.readline()
		if i == a2:
			data = data.rstrip().split()
			for j in range(4):
				s2.add(int(data[j]))

	s = s1.intersection(s2)
	ans = ''
	if len(s) == 0:
		ans = 'Volunteer cheated!'
	elif len(s) > 1:
		ans = 'Bad magician!'
	else:
		ans = str(s.pop())

	fo.write('Case #' + str(ti) + ': ' + ans + '\n')

f.close()
fo.close()