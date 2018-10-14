def valid(s):
	for i in s:
		if i!='+':
			return False
	return True
f1=open('A-large.in','r')
f2=open('xx.txt','w')
for _ in range(int(f1.readline())):
	s,k=f1.readline().split()
	k=int(k)
	s=list(s)
	ans=0
	for i in range(len(s)-k+1):
		if s[i]=='-':
			for j in range(k):
				if s[i+j]=='-':
					s[i+j]='+'
				else:
					s[i+j]='-'
			ans+=1
	if not valid(s):
		print("Case #%d: %s"%(_+1,'IMPOSSIBLE'),file=f2)
	else:
		print("Case #%d: %d"%(_+1,ans),file=f2)
