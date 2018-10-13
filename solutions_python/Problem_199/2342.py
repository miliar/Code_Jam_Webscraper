def flip(s,k):
	l=len(s)
	#print(l,s,k)
	c=0
	for i in range(l-k+1):
		if s[i]=='-':
			for j in range(i,i+k):
				s[j]=['+','-'][s[j]=='+']
			c+=1
			#print(s)
	i+=1
	while i<l:
		if s[i]=='-':
			return -1
		i+=1
	return c
for i in range(int(input())):
	s,k=input().split()
	s,k=list(str(s)),int(k)
	ans=flip(s,k)
	if ans==-1:
		print('Case #%d: %s'%(i+1,'IMPOSSIBLE'))
	else:
		print('Case #%d: %d'%(i+1,ans))
