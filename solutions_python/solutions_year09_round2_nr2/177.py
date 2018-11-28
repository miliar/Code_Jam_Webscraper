from itertools import permutations

for C in xrange(input()):
	n = input()
	cn = str(n)
	cand = []
	for p in permutations(cn):
		a = ''
		for i in p:
			a = a+i
		if int(a) > n:
			cand.append(a)
	if len(cand):
		print 'Case #%d: %s' % (C+1, min(cand))
	else:
		cand = []
		cn = cn + '0'
		for p in permutations(cn):
			a = ''
			for i in p:
				a = a+i
			if int(a) > n:
				cand.append(a)
		print 'Case #%d: %s' % (C+1, min(cand))
	
