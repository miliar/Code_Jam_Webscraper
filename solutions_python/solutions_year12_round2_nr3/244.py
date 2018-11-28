import sys
import itertools

for tc in xrange(1, int(sys.stdin.readline())+1):
  line = [int(w) for w in sys.stdin.readline().split()]
  n = line[0]
  nos = []
  for a in xrange(0, len(line)):
   if a == 0:
	continue
   nos.append(line[a])
	
  nos = sorted(nos)
  for i in xrange(1, sum(nos) - 1, nos[0]):
	count = 0
	res = []
	msg = ''
	for j in xrange(1, len(nos) - 1):
		#print i, j
		min_s, max_s = 0, 0
		for l in xrange(0, j):
			min_s += nos[l]
			max_s += nos[-l]
		if i < min_s or i > max_s:
			continue
		obj = itertools.combinations(nos, j)
		#print 'Combi'
		for a in obj:
			if i == sum(a):
				count += 1
				res.append(a)
				if count >= 2:
					break
		if count >= 2:
			msg = 'Case #%d: \n' % tc
			for b in res:
				#print b
				for c in b:
					msg += str(c) + ' '
				msg += '\n'
			break
	if msg != '':
		print msg.strip('\n')
		break
  if msg == '':
	print 'Case #%d: Impossible' % tc
	#print i, j, res, count