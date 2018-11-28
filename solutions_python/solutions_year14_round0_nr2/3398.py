def solve(C,F,X):
	r=2
	c=0
	tt=(X-c)/r
	nt=(C-c)/r
	nr=r+F
	c=-(nr*nt)
	tt2=(X-c)/nr
	while (tt2<tt):
		tt=tt2
		nt=(C-c)/nr
		nr=nr+F
		c=-(nr*nt)
		tt2=(X-c)/nr
	return str(tt)

def Cookie():
	f=open("B-small-attempt0.in")
	g=open("output.ou",mode='w')
	a=int(f.readline()[:-1])
	for l in range(a):
			(C,F,X)=f.readline()[:-1].split(' ')
			(C,F,X)=(float(C),float(F),float(X))
			o=solve(C,F,X)
			g.write("Case #"+str(l+1)+": "+o+"\n")
	f.close()
	g.close()
