t=int(input())
for j in range(1,t+1):

	ls=input().split()
	str=ls[0]
	k=int(ls[1])
	c=0
	n=len(str)
	while '-' in str:
		ind=str.index('-')
		if ind+k-1>=n:
			c=-1
			break
		ls=str[ind:k+ind]
		ls=ls.replace('-','#')
		ls=ls.replace('+','-')
		ls=ls.replace('#','+')
		c=c+1
		str=str[0:ind]+ls+str[k+ind:n]
	if c==-1:
		print("Case #%d: IMPOSSIBLE"%(j))
	else:
		print("Case #%d: %d"%(j,c))
