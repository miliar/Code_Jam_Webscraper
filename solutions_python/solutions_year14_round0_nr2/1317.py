n=int(raw_input(""))
for y in range(1,n+1):
	c,f,x=map(float,raw_input("").split(" "));
	r=2
	initial=x/r
	buy=c/r+x/(r+f)
	time=0
	while (buy<initial):
		time+=c/r;
		r+=f
		initial=x/r
		buy=c/r+x/(r+f)
	print "Case #"+str(y)+": "+str(time+x/r)
