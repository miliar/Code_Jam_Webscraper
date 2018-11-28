for t in range(int(input())):
	s,k=[i for i in input().split()]
	k=int(k)
	s=list(s)
	i=0
	n=0
	while i+k<len(s):
		if s[i]=='-':
			n+=1
			for m in range(i+1,i+k):
				s[m]='+'if s[m]=='-'else'-'
		i+=1
	d=s[i:].count("+")
	if d==0:n+=1
	print("Case #"+str(t+1)+":",n if d==0 or d==k else"IMPOSSIBLE")