infile = 'C-small-attempt0.in'
data = [line[:-1] for line in open(infile).readlines()]
for i,case in enumerate(data):
	if i>0:
		a,b=map(int,case.split(' '))
		pairs=[]
		for n in xrange(a,b+1):
			digits = str(n)
			for j in range(1,7):
				m = int(digits[j:]+digits[:j])
				if a<=n<m<=b: pairs.append((n,m))
		print "Case #%s: %s" % (i,len(set(pairs)))
		
		
