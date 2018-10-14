f = open('A-large.in').read().split('\n')

n=int(f[0])
#print f
line=1
for i in range(n):
	s = int(f[line])
	line=line+1	
	engines = f[line:line+s]
	line = line+s
	
	q = int(f[line])
	line=line+1
	queries = f[line:line+q]
	line=line+q
	
	start = 0
	dist = {}
	switches = 0
	while(True):
		
		for l in engines:
			dist[l] = q
	
		for l in range(start,len(queries)):
			if queries[l] in engines:
				dist[ queries[l] ] = min(l, dist[ queries[l] ])	
		
		if(max(dist.values()) == q):
			break
		else:
			start=max(dist.values())
			switches=switches+1
	
	print "Case #%i: %i" % (i+1,switches)
	
	
