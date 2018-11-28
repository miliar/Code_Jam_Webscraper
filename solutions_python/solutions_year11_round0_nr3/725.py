t=int(raw_input())
c=0;
while t:
	t-=1
	c+=1
	n=int(raw_input())
	l=[int(x) for x in raw_input().split()]
	flag=False;
	m=0;
	for i in range(0,2**n):
		s=i
		pete=0;
		savep=0;
		su=0;
		for j in range(0,n):
			if s%2==1:
				pete=pete^l[j]
				savep=savep+l[j]
			else:
				su=su^l[j]
			s/=2;
		if(pete==su and su!=0):
			flag=True
			if (savep>m):
				m=savep
	if flag==False:
	   print 'Case #%d: NO'%c
	else:
	   print 'Case #%d: %d'%(c,m)
