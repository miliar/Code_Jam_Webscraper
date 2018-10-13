t = int(input()) 
def istidy(N):
	s=str(N)
	tidy=True
	for i in range(1,len(s)):
		if s[i]<s[i-1]:
			tidy=False
	return tidy
def findtidy(N):
	if N<10:
		return N
	s=[int(s) for s in str(N)]
	
	for i in range(len(s)-1,0,-1):
		if s[i]<s[i-1]:
			for j in range(i,len(s)):
				s[j]=9
			s[i-1]=s[i-1]-1%10
	return(s)
def findtidy2(N):
	if N<10 or istidy(N):
		return N
	s=str(N)
		

for i in range(1, t + 1):
	N=int (input())
	#print(N)
	#print(istidy(N))

	if N<10:
		b=N
	else:
		a=map(str,findtidy(N))
		b=''.join(a)
		#print(b)
	print("Case #{}: {}".format(i,int(b)))