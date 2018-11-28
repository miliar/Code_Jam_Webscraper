dump = open('dump', 'r').readlines()

test_cases = int(dump[0][:-1])

for i in xrange(1, test_cases*10, 10):
	print 'Case #{}:'.format(i/10 + 1),
	ans1 = int(dump[i][:-1])
	possible1 = set(map(int, dump[i+ans1][:-1].split(' ')))
	ans2 = int(dump[i+5][:-1])
	possible2 = set(map(int, dump[i+5+ans2][:-1].split(' ')))
	
	overlap = possible1.intersection(possible2)
	
	if len(overlap) == 0:
		print 'Volunteer cheated!'
	elif len(overlap) > 1:
		print 'Bad magician!'
	elif len(overlap) == 1:
		print list(overlap)[0]
