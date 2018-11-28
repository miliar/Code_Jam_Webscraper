t=raw_input()
i=0
while i<int(t):
	gotUp=0
	ToAdd=0
	sm,s=raw_input().split()
	s=map(lambda x:int(x),s)
	for need,j in enumerate(s):
		#print 'BEFORE: gotUp: '+str(gotUp)+' ToAdd: '+str(ToAdd)
		#print 'Shyness: '+str(need)+' Total person: '+str(j)
		if need<=(gotUp+ToAdd) or not j:
			gotUp+=j
		else:
			ToAdd+=(need-(gotUp+ToAdd))
			gotUp+=j
		#print 'AFTER: gotUp: '+str(gotUp)+' ToAdd: '+str(ToAdd)+'\n'
	print 'Case #'+str(i+1)+': '+str(ToAdd)
	i+=1
#raw_input()

