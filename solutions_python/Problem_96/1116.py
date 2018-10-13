f1=open('B-large.in','r')
f2=open('goog.out','w')

a=f1.readline()
a=a.rstrip('\n')
t=1
while t<=int(a):
	s=f1.readline()
	s=s.rstrip('\n')
	s=s.split(' ')
	n=int(s[0])
	b=int(s[1])
	m=int(s[2])
	c=0

	for i in range(0,n):
		if(int(s[i+3])>=(m*3-2)):
			c+=1
			continue

		
		elif((m*3-4)>=0 and int(s[i+3])>=(m*3-4)):
			if(b!=0):
				b-=1
				c+=1
				

	temp='Case #'+str(t)+': '+str(c)+'\n'
	f2.write(temp) 
	
	t+=1		
			
			
