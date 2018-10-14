fi=open("/home/baralnischal/Downloads/B-large.in",'r')
g=open("/home/baralnischal/Downloads/ouptput.txt","w")
t=int(fi.readline())

for i in range(t):
	c,f,x=[float(a) for a in fi.readline().split()]
	c11=0
	cir=2
	tu=0
	pto=x/cir
	while 0==0:
		tu+=c/cir
		cir+=f
		tr=x/cir
		to=tu+tr
		if to>pto:
			c11=1
			g.write("Case #%d: %.7f\n"%(i+1,pto))
			break
		pto=to