
lines = open('A-small-attempt0.in', 'r').readlines()
count = 0
for line in lines[1:]:
	count += 1
	s = line.split()[-1].strip()
	n, s = 0, map(int, list(s))
	for i in xrange(1, len(s)):
		s[i] = s[i] + s[i-1]
		n = max(n, i - s[i-1])
	print 'Case #' + str(count) + ': ' + str(n)