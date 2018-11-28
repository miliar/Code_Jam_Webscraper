tst=int(input())
for tt in range(0,tst):
	s=input()
	t=s.split(' ')
	n=int(t[1])
	str=list(t[0])
	flag=0
	ans=0
	if str.count('-')==0:
		print("Case #%d: 0" %(tt+1))
	
	else:
		#print(str)
		for k in range(0,len(str)):
			for i in range(0,len(str)-n+1):
				
				if str[i]=='-':
					for j in range(i,i+n):
						if str[j]=='-':
							str[j]='+'
						elif str[j]=='+':
							str[j]='-'
					break
			#print(str)
			if str.count('-')==0:
				ans=k
				flag=1
				break
			#print(str)
		if flag==1:
			print("Case #%d: %d" %(tt+1,ans+1))
		else:
			print("Case #%d: IMPOSSIBLE" %(tt+1))