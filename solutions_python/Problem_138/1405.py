Output = []
T = int(raw_input())
for i in range(T):
	N = int(raw_input())
	Naomi = raw_input().split()
	#print Naomi
	Naomi = [float(x) for x in Naomi]
	Ken = raw_input().split()
	Ken = [float(x) for x in Ken]
	Naomi.sort()
	Ken.sort()
	
	Wscore = 0
	Dscore = 0
	
	i=0
	j=0
	while i<N and j<N:
		if Ken[-1-i]>Naomi[-1-j]:
			i += 1
		else:
			Dscore += 1
			i += 1
			j += 1
			
	j=0
	for i in range(len(Ken)):
		if Ken[-1-j]<Naomi[-1-i]:
			Wscore += 1
		else:
			j += 1
			
#		if Naomi[i]>Ken[i]:
#			Dscore += 1
		
	Output += ["%d %d" % (Dscore, Wscore)]

		
for i in range(len(Output)):
	print 'Case #%d: %s' % (i+1, Output[i])