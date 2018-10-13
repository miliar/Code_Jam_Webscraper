import sys
data = sys.stdin.readlines()
n = int(data[0])
for i in range(1,len(data)):
	a,b = map(lambda x: int(x), data[i].split(" "))
	s = set([])
	l = len(data[i].split(" ")[0])
	BIG = 10**(l-1)

	for c in range(a,b):
		d = c
		for j in range(1,l):
			d = BIG*(d%10)+d/10
			if d > c and d <= b:
				s.add((c,d))

	print "Case #%i: %i"%(i,len(s))
