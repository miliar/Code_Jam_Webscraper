from operator import itemgetter
from itertools import permutations

for C in xrange(input()):
	num = raw_input()
	n = []
	for i in num:
		n.append(i)
	list = {}
	count = 0
	a = [1, 0, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F']
	for i in xrange(len(n)):
		if n[i] not in list:
			list[n[i]] = a[count]
			n[i] = a[count]
			count += 1
		else:
			n[i] = list[n[i]]
	a = ''
	for i in n:
		a += str(i)
	if len(list) == 1:
		base = 2
	else:
		base = len(list)
	print 'Case #%d: %d' % (C+1, int(a, base))
