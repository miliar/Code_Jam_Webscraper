for m in range(int(input())):
	s,k = input().split()
	k = int(k)
	l = len(s)
	s = list(s)
	i = 0
	count=0
	while(i<l):
		if(s.count('+')==l):
			print('Case #{0}: {1}'.format(m+1,count))
			break
		if(s.count('-')==1):
			print('Case #{0}: {1}'.format(m+1,'IMPOSSIBLE'))	
			break
		if(s[i]=='-'):
			count+=1
			if(i>l-k):
				print('Case #{0}: {1}'.format(m+1,'IMPOSSIBLE'))	
				break
			for j in range(i,i+k):
				if(s[j]=='-'):
					s[j]='+'
				elif(s[j]=='+'):
					s[j]='-'
		
		i+=1					

