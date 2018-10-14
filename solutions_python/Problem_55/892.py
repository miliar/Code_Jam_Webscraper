from Queue import Queue

f = open('input3', 'r')

cases = int(f.readline())
trips = []


for i in range(cases):
	euros = 0

	(r,k,n) = f.readline().split()
	groups = f.readline().split()

	for arf in range(int(n)):
		groups[arf] = int(groups[arf])

	#print groups

	groups.reverse()

	for trip in range(int(r)):
		toenqueue = []
		remaining = int(k)
		#print "quedan "+str(remaining)+" plazas"
		
		while(len(groups) and remaining >= groups[-1]):
			g = groups.pop()
			#print "subiendo a "+str(g)
			euros += g
			remaining -= g
			toenqueue.append(g)
			#print groups

		groups.reverse()
		for e in toenqueue:
			groups.append(e)
		groups.reverse()

	print "Case #"+str(i+1)+": "+str(euros)
		
		
