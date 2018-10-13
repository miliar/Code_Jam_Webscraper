import sys

v=open(sys.argv[1],"r");
ot=open(sys.argv[2],"w");

z=v.readlines()
n=int(z[0]);
for ind in xrange(1,len(z)):
	i=z[ind][:-1];
	print "Dealing with",i
	s=set(i)
	print s
	if len(s)==1:
		s=[0,1]
	t={i[0]:1}
	n=0;
	ndig=0
	for j in i:
		if j in t.keys():
			n=n*len(s)+t[j]
			print 'just got a digit',t[j]
		else:
			if ndig==0:
				n=n*len(s)
				t[j]=0
				ndig=2
			else:
				n=n*len(s)+ndig
				t[j]=ndig
				ndig=ndig+1
			print 'just mapped',j,'to',t[j]
	ot.write("Case #%i: %i\n"%(ind,n))

ot.close()
