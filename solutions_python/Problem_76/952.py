#!/usr/bin/python

a=raw_input ();
a = int(a);

for i in range(1,a+1):
	b = raw_input();
	b = int(b);
	xor = 0;
	minm = 1000000;
	sum = 0;
	x = raw_input();
	x = x.split();
	for s in x:
		s = int(s);
		xor = xor ^ s;
		sum = sum + s;
		minm = min(minm, s);

	if xor is not 0:
		print "Case #"+ str(i) +": NO";
	else:
		print "Case #"+ str(i) +": " + str(sum - minm) ;
