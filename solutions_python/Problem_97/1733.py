import collections;
import sets
import sys

_A= 1111
_B= 2222

#print "A= %d, B= %d" % (_A,_B);
A= _A
B= _B

P= [];

def right_shift(a):
	g= a[-1]+a[:-1];
	return (g);

def left_shift(a):
	g= a[1:]+a[0];
	return (g);

def test(x):
	cnt= 0;
	S= sets.Set();
	len_x= len(str(x)); 
	s= str(x);
	for i in range(len_x):	  
		s= left_shift(s);
		q= int(s);
		if(len(str(q))!=len_x):
#			print "\t reject (x,q)= (%d,%d)"%(x,q);
			continue;
#		print "\t s= %s, q= %d"% (s,q);
		if x<q and q<=B:
			pair= "\t\t (x,q)= (%d,%d)"% (x,q);
#			print pair;
			P.append(pair);
			S.add(pair);
			cnt= cnt+1;
	return len(S); # cnt;

def proc(uid,A,B):
	total= 0;
	x= A;
	len_A= len(str(A));
	len_B= len(str(B));
	if len_A==len_B:
		while x<=B:
#		print "x= %d"%x;
			total= total+ test(x);
			x=x+1;
#	print "A= %d,\tB= %d,\t"%(A,B),
	print "Case #%d: %d"% (uid,total);
	return;
'''
'''

#N= argv[0];
raw= raw_input();
if raw.strip() == "": 
	print "N error.";
N= int(raw);
u= 1;
while u<=N:
	raw= raw_input();
	if raw.strip() == "": print "(A,B) error.";
	param= raw.split();
	if len(param)!=2:  print "A and B error.";
	A=int(param[0]);
	B=int(param[1]);
	proc(u,A,B);
	u=u+1;
#
'''
proc(0,_A,_B);
print "A= %d, B= %d" % (_A,_B);
#for pr in P: print pr;
#C= collections.Counter(P);
#print C.most_common(3);
#print cnt;


'''

