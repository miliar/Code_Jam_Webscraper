t=int(input())
for ij in range(1,t+1):
	d1,n1=input().split(' ')
	n=int(n1)
	d=int(d1)
	k=[]
	s=[]
	maxi=0
	for i in range(1,n+1):
		a,b=[int(s) for s in input().split(" ")]
		if((d-a)/b>maxi):
			maxi=(d-a)/b
		ans=d/maxi
		
	print("Case #{}: {}".format(ij, ans))
