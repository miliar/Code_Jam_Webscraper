#flipper
def flip(l):
	for i in range(len(l)):
		if l[i]=='-':
			l[i]='+'
		else:
			l[i]='-'
	return l
def checkme(l):
	for i in range(len(l)):
		if l[i]=='-':
			return False
	else:
		return True
def flipme(f,k):
	l=list(f)
	flips=0
	if(checkme(l)):
		return flips
	if(len(l)<k):
		return 'IMPOSSIBLE'
	for i in range(len(l)-k+1):
		if l[i]=='-':
			flips=flips+1
			l[i:i+k]=flip(l[i:i+k])
		if(checkme(l)):
                        return flips
	else:
		return 'IMPOSSIBLE'
t=int(input())
for i in range(1,t+1):
	f, k = [s for s in input().split(" ")]
	k=int(k)
	n=flipme(f,k)
	print("Case #{}: {}".format(i,n))
