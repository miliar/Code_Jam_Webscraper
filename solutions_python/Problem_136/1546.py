t=int(raw_input())
for i in range(0,t):
	a=raw_input().split()
	b=list()
	c=float(a[0])
	f=float(a[1])
	x=float(a[2])
	cr = 2
	cookie=0
	time =0 
	while (cookie!=x):
		nf=c/cr
		complete=x/cr
		totc=nf+x/(cr+f)
		if(complete<totc):
			time+=complete
			cookie=x
		else:
			cr+=f
			time+=nf
			cookie=0
	print 'Case #'+str(i+1)+': '+str(time)
