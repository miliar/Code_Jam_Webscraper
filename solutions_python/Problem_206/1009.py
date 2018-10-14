t=input()
m=1
while m<=t:
	n,d=map(int,raw_input().split())
	ti=[]
	while d:
		d-=1
		a,v=map(int,raw_input().split())
		ti.append(float(n-a)/float(v))
	ti=max(ti)
	print "Case #"+str(m)+": {0:.6f}".format(round(float(n)/float(ti),6))
	m+=1