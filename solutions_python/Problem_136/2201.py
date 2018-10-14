for t in range(1,int(input())+1):
	c,f,x=map(float,input().split())
	r,ans=2,0
	while(x/r > (c/r + x/(r+f))):
		ans+=c/r
		r+=f
	ans+=x/r
	print("Case #{}: {:.7f}".format(t,ans))