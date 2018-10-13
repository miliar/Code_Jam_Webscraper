sol=''
for test in range(int(input())):
	S,k=input().split()
	k=int(k)
	s=[]
	l=0
	for x in S:
		s.append(x)
		l+=1 
	c=0
	i=0
	while i<l:
		while i<l and s[i]=='+':
			i+=1
		if i>=l:
			sol+='Case #'+str(test+1)+": "+str(c)+'\n'
			break
		j=i
		#print(i,j,k,l)
		#print(s)
		if j+k<=l:
			for x in range(j,j+k):
				if s[x]=='-':
					s[x]='+'
				else:
					s[x]='-'
			c+=1
		else:
			sol+='Case #'+str(test+1)+": IMPOSSIBLE"+'\n'
			break
print(sol[:-1])
