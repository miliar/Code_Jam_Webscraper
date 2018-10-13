t=int(raw_input())
for tt in range(0,t):
	l=map(str,raw_input().split())
	s=list(l[0])
	k=int(l[1])
	n=len(s)
	i=0
	flag=1
	count=0
	while i<n:
		#print s[i:]
		if s[i]=='-' and i+k<=n:
			count+=1
			#print s[i:i+k],
			for j in range(i,i+k):
				if s[j]=='-':
					s[j]='+'
				else:
					s[j]='-'
			#print s[i:i+k]
		elif s[i]=='-' and i+k>n:
			for j in range(i,n):
				if s[j]=='-':
					flag=0
					break
		i+=1
	print 'Case #'+str(tt+1)+':',
	if flag==1:
		print str(count)
	else:
		print 'IMPOSSIBLE'