f=open("cj1/A-small-attempt0 (1).in","r")
o=open("cj1/A-small-attempt0 (1).out","w")
count=int(f.readline())
lines = f.readlines()
j=0
s=""
for line in lines:
	j=j+1
	x=line.split()
	r=int(x[0])
	t=int(x[1])
	c=0
		
	while t>0:
		t=t-(r*2+1)
		r=r+2
		if t>=0:c=c+1
	
	#print "Case #%d: %d" % (j, c)
	o.write("Case #%d: %d\n" % (j, c))
	
f.close()
o.close()
