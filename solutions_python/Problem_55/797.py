def rides( number_rides, max_person_ride, group, N ):

	s=0
	value=0
	
	#print max_person_ride
	#print group
	for i in xrange(0, number_rides):
		s=0
		c = len(group)-1
		c1 = 0
		while s+group[0]<=max_person_ride and c1<N:
			s = s+group[0]
			temp = group[0]
			group.pop(0)
			group.append(temp)
			
			c1=c1+1
			
		value = value + s
				
	return value
			
		
	
f = open('C-small.in','r')
w = open('C-small.oo','w')

i=0
x=1
l1=""
l2=""
g=[]
for line in f.xreadlines():
	if i>0:
	
		if i%2==0:
			l2 = line
			
			r,k,N = [int(v) for v in l1.split()]
			g= [int(v) for v in l2.split()]
			
			val = rides ( r, k, g, N)
			w.write('Case #%d: %d\n' % (x,val))
			
			x=x+1
			
		else:
			l1 = line
			
	
	i=i+1
	
w.close()
f.close()