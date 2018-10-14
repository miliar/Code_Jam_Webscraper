#! /usr/bin/python
import math
ip=open('in.in','r')
op=open('out.out','w')
cases=int(ip.readline().rstrip())
for x in range(0,cases):
	count=0;
	rng=ip.readline().rstrip().split()
	n1=int(rng[0])
	n2=int(rng[1])
	print n1,n2
	for y in range(n1,n2+1):
		if str(y)==str(y)[::-1]:
			sqrt=math.sqrt(y);
			if int(sqrt)==sqrt:
				sqrt=int(sqrt)
				if str(sqrt)==str(sqrt)[::-1]:
					count=count+1;
				
	op.write("Case #"+str(x+1)+": "+str(count)+"\n")
op.close();
