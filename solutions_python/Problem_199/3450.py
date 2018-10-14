t=input()
#t=1
t1=0
while t1<t:
	#s="++------++--++"
	inp=raw_input()
	s=inp.split(" ")[0]
	#k=input()
	k=int(inp.split(" ")[1])
	t1=t1+1
	l=list(s)
	
	len1= len(l)
	count=0
	flag_imp=False
	pos=-1
	for i in range(len(l)):
		if l[i]=='-':
			j=0
			
			
			if k>(len1-i):
				
				print "Case #%d:"%t1,"IMPOSSIBLE"
				flag_imp=True
				break
			count=count+1
			while j<k :
				
				if l[i]=='-':
					l[i]='+'
				else:
					l[i]='-'
					if pos==-1:
						pos=i
				i=i+1
				j=j+1
			if pos !=-1:
				i=pos
				
				pos=-1
			
		else:
			i=i+1
	#print l
	if (flag_imp==False):
		print "Case #%d: %d"%(t1,count)