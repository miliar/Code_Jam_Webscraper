t = int(input())
for j in range(t):
	n=list(input().strip())
	c=0
	if(len(n)==1):
		print("Case #"+str(j+1)+":",n[0])
		continue
	ii=len(n)
	for i in range(len(n)-1):
		if(n[i]>n[i+1]):
			n[i] = str(int(n[i])-1)
			ii=i+1
			break
	for i in range(ii,len(n)):
		n[i]='9'
	for i in range(ii-1,0,-1):
		if(n[i-1]>n[i]):
			n[i] = '9'
			n[i-1] = str(int(n[i-1])-1)
	ans = int(''.join(n))
	
	print("Case #"+str(j+1)+":",ans)