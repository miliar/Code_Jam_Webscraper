#!/usr/bin/python

import sys;


t = list();
m = list();

def gcd(A, B):
   while B != 0:
      R = A % B
      A = B
      B = R
   return A


try_id =0;
my_end = 0;

md = 0;

min_diff = 0;

n = 0;

for line in sys.stdin:
	del t;
	t = list();
	ln = line.split();
	del m;
	m = list();
	if try_id > 0:
		for index in range(1,len(ln)):
			t.append(int(ln[index]));
		else: my_end=0;
		t.sort();
		t.reverse();
		
	
		for index in range(1,len(t)):
			diff = t[index-1]-t[index];
			if diff>0 : m.append(diff);
		else: my_end = 0;
			#print m;
		nod = m[0];
		for i in range(1,len(m)):
			nod = gcd(nod,m[i]);
		else: my_end = 0;

		y = nod-1-(t[0]-1)%nod;
		#if y==1 : y=0;
		print 'Case #%d: %d' % (try_id,y);
		#for i in range(len(t)):
		#	print " %d [%d : %d] " % (t[i],(t[i]+y)/nod,(t[i]+y)%nod);
		#print "nod %d\n" % nod;

		#else: print 'Case #%d: %d' % (try_id,0);
	else: my_end = 0;
	try_id = try_id+1;
else: my_end = 0;

#print t[0];
