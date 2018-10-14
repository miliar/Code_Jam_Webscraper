import sys

k = int(sys.stdin.readline())
for t in xrange(k):
	line = [sys.stdin.readline() for _ in xrange(10)]
	a = int(line[0])
	sa = set(int(x) for x in line[a].split())
	b = int(line[5])
	sb = set(int(x) for x in line[5+b].split())
	s = sa & sb
	print 'Case #%d:' % (t+1),
	if len(s) == 1:
		print s.pop()
	elif len(s) == 0:
		print 'Volunteer cheated!'
	else:
		print 'Bad magician!'
