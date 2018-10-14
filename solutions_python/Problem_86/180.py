from sys import stdin

t = int(stdin.readline())

for tc in xrange(t):
	line = stdin.readline().strip().split()

	n = int(line[0])
	l = int(line[1])
	h = int(line[2])

	x = [int(y) for y in stdin.readline().strip().split()]

	s = -1
	for i in xrange(l,h+1):
		ok = True
		for j in x:
			if max(i,j) % min(i,j) != 0:
				ok = False
				break
		if ok:
			s = i
			break

	if s == -1:
		print "Case #%d: NO" % (tc+1)
	else:
		print "Case #%d: %d" % (tc+1,s)
