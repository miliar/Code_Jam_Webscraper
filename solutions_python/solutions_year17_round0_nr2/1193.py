t=input()
for i in range(1,t+1):
	x=input()
	foo=list(str(x))
	c=0
	for j in range(len(foo)-1):
		if(int(foo[j])>int(foo[j+1])):
			c=j
			foo[j]=str(int(foo[j])-1)
			for k in range(j+1,len(foo),1):
				foo[k]='9'
			break
	while(c>0):
		if(int(foo[c])<int(foo[c-1])):
			foo[c]='9'
			foo[c-1]=str(int(foo[c-1])-1)
		c-=1
	if(foo[0]=='0'):
		foo=foo[1:]
	print "Case #"+str(i)+": "+"".join(foo)
		
			
