#!/usr/bin/python2
ra=lambda:sorted(map(lambda x:round(float(x)*100000),raw_input().split()),reverse=True)
for ti in range(input()):
	n=input()
	a,b=ra(),ra()
	x,y=a[:],b[:]
	ans1,ans2=0,0
	while len(a):
		if a[0]>b[0]:
			ans1+=1
			del a[0]
		else:
			del a[-1]
		del b[0]

	while len(x):
		if x[0]>y[0]:
			ans2+=1
			del y[-1]
		else:
			del y[0]
		del x[0]
	print "Case #%d: %d %d"%(ti+1,ans1,ans2)
	
