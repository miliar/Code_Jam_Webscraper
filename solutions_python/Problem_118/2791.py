import sys

def checkPalin(n):
	s = str(n)
	l = len(s)
	if l == 0:
		return False
	elif l == 1 and n != 0:
		return True
	elif l == 2:
		return s[0] == s[1]
	else:
		for i in xrange(l/2):
			if s[i] == s[l-1-i]:
				continue
			break
		if i == l/2 - 1 and s[i] == s[l-1-i]:
			return True
		else:
			return False

def findSquare(n):
	start = 1
	stop = n/2
	while start < stop:
		m = start + (stop - start)/2
		t = m*m
		if t > n:
			stop = m
		elif t < n:
			start = m+1
		else:
			return m
	if start * start == n:
		return start
	return 0

for rc in xrange(1, int(sys.stdin.readline())+1):
	A, B = [int(w) for w in sys.stdin.readline().split()]
	count = 0
	for p in xrange(A, B+1):
		if checkPalin(p) == True:
			sq = findSquare(p)
			if sq != 0:
				if checkPalin(sq) == True:
					count += 1
	print 'Case #%d: %d' %(rc, count)

