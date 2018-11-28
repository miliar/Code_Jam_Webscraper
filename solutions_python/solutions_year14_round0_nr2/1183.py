test = int(input())
#def ans(c,f,x,i):
#	t0 = x/f
#	t1 = c/f
#	if (t1 + x/(f+i)) > t0 :
#		return t0
#	t2 = t1+ans(c,i+f,x,i)
#	return min(t0,t2)
	
for i in range(1,test+1):
	a = list(map(float,input().split()))
	c = a[0]
	f = a[1]
	x = a[2]
	r = 2
	t = float(0)
	while True:
		t0 = x/r
		t1 = c/r
		r = r+f
		if ( t1 + x/r) > t0:
			t = t+ t0
			break
		t = t + min(t0,t1)
	print("Case #"+str(i)+": "+"{0:.7f}".format(t))
	
