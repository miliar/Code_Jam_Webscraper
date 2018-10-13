tn = input()
def ispalindrome(n):
	s = str(n)
	for i in xrange(len(s)):
		if s[i] != s[-1-i]:
			return False
		if i > len(s)-i-1:
			return True
	return True
def isq(x):
	l = 1
	r = x
	vm = 1
	while l<=r:
		m = (l+r)/2
		if m**2 == x:
			return m
		elif m**2 < x:
			l = m + 1
			vm = m
		else:
			r = m - 1
	return vm

#print [(i,isq(i)) for i in xrange(1000)]
for loop in xrange(tn):
	print 'Case #%d:'%(loop+1),
	A,B=[int(x) for x in raw_input().split()]
	i = isq(A)
	while i*i < A:
		i += 1
	c = 0
	while i*i <= B:
		if ispalindrome(i) and ispalindrome(i*i):
			c+=1
		i += 1
	print c
	
