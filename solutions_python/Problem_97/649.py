from sys import stdin

for cs in xrange(1, 1+int(stdin.readline().strip())):
	(a,b)= [int(z) for z in stdin.readline().split()]
	c=0
	for x in xrange(a,b+1):
		s = str(x)
		n=len(s)
	#	print nn,xd,(x-nn*xd)*10+xd
		seen=set()
		si=x
		nn=10**(n-1)
		for rr in xrange(n-1):
			xd=si/nn
			si = (si-nn*xd)*10+xd
#			s=s[n-1] + s[0:n-1]
#			si=int(s)
			if si<=x or si>b or si in seen:
				continue
			#print ".. "+s
			seen.add(si)
			c+=1
	print "Case #{0}: {1}".format(cs, c)
