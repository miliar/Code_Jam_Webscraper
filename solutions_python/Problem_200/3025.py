t=int(raw_input())
for tt in range(0,t):
	#s = map(int,raw_input())
	#n=len(s)
	s=int(raw_input())
	while s>=0:
		flag=1
		l=map(int,str(s))
		for i in range(0,len(l)):
			if i+1 <len(l) and l[i]>l[i+1]:
				flag=0
				break
		if flag==1:
			break
		s-=1
	# s1=''
	# #for i in range(0,)
	# for i in s:
	# 	s1+=str(i)
	print 'Case #'+str(tt+1)+': '+str(s)