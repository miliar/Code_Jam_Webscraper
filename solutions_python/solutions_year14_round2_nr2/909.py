F = open('B-small-attempt0.in').read()

f = F.split('\n')
T = f[0]
c = 1

for t in range(0,int(T)):
	l = f[t+1].split(' ')
	A = int(l[0])
	B = int(l[1])
	K = int(l[2])
	c = 0
	for a in range(0,A):
		for b in range(0,B):
			#print "<%d,%d> %d" % (a,b,a&b)
			if(a&b < K):
				c += 1

	print "Case #%d: %d" % (t+1,c)