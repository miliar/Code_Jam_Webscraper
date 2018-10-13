f=open("A-small-attempt0.in","r")
f1=open("a-small.out","w")
data=f.readlines()
test=int(data[0])
for case in range(1,test+1):
	ech=data[case]
	ech=ech.split()
	r=int(ech[0])
	t=int(ech[1])
	count=0
	while (t>0):
		over=(2*r)+1
		if (t-over)<0:
			break
		else:
			t=t-over
			count=count+1
			r=r+2
	f1.write("Case #%d: %d\n"%(case,count))
f1.close()
f.close()
