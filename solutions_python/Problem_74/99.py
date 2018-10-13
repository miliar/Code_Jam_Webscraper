T = input()
for t in range(T):
	line = raw_input().split()
	op = []
	N = int(line[0])
	for i in range(N):
		op += [(line[i*2+1],int(line[i*2+2]))]
	c = 0
	oo,bo = 0,0
	od,bd = 1,1
	while oo<N or bo<N:
		while oo<N and op[oo][0]!='O': oo+=1
		while bo<N and op[bo][0]!='B': bo+=1
		if oo<N:
			if od<op[oo][1]: od+=1
			elif od>op[oo][1]: od-=1
			elif oo<bo: oo+=1
		if bo<N:
			if bd<op[bo][1]: bd+=1
			elif bd>op[bo][1]: bd-=1
			elif bo<oo: bo+=1
		c += 1
	print "Case #%s: %s" % (t+1,c)

				

