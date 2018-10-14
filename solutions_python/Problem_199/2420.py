for _ in range(int(input())):
	s,k=input().split()
	k=int(k)
	ans1='IMPOSSIBLE'
	ans='Case #'+str(_+1)+': '
	s=list(s)
	n=len(s)
	num=0
	for i in range(n-k+1):
		if s[i]=='-':
			num+=1
			for j in range(i,i+k):
				if s[j]=='+':
					s[j]='-'
				else:
					s[j]='+'
	# print(s)
	if ''.join(s)=='+'*n:
		print(ans+str(num))
	else:
		print(ans+ans1)