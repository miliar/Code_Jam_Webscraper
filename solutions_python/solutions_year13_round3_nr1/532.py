import sys

f = sys.stdin
cases = int(f.readline())

cons = "bcdfghjklmnpqrstvwxyz"

t = []
n = 0

def succ(a, b):
	if a < b:
		for i in t:
			if i >= a and i+n <= b:
				return 1
	
	return 0
		
for case in range(0, cases):
	l = f.readline().split(' ')
	s = l[0]
	n = int(l[1])
	t = []
	c = 0
	l = len(s)
	
	for i in range(0, len(s)-n+1):
		if s[i] in cons:
			b = True
			for j in range(1, n):
				if not s[i+j] in cons:
					b = False
					break
			if b:
				t.append(i)
				
	for x in range(0, l+1):
		for y in range(0, l+1):
			c += succ(x, y)
	
	
	print "Case #%s: %s" % (case+1, c)