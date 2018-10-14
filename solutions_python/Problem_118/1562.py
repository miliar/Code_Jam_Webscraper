from math import sqrt
T = input()
def findfsq():
	tmp = []
	i = 1
	k = 1
	while k < 10**14:
		s = str(k)
		n = sqrt(k)
		if str(s) == str(s)[::-1] and n == int(n) and str(int(n)) == str(int(n))[::-1]:
			tmp.append(k)
		i += 1
		k = i**2
	return set(tmp)
fsq = findfsq()
for t in xrange(T):
	tmp = raw_input().split(' ')
	n, m = int(tmp[0]), int(tmp[1])
	#c = fsq & set(xrange(n, m+1))
	c = 0
	for z in fsq:
		if z >=n and z <=m:
			c += 1
	print 'Case #%d: %d' % (t+1, c)
