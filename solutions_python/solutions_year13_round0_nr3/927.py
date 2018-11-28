import sys
import math
import operator

def check_palidrom(d):
	s= list(str(d));
	if len(s)==1:
		return True;
	w= len(s)/2;
	return s[:w]==s[-w:][::-1];


def fair_and_square(X):
	X= map( math.sqrt, X )
	X= [ int(math.ceil(X[0])), int(X[1]) ]
	cnt=0;
	#
	for d in range(4):
		if d==0:
			for i in range(1,3+1):
				if X[0]<=i and X[1]>=i:
					cnt+= 1;
			continue;
		for k in ['','0','1','2']:
			for j in [1,2]:
				for i in range(2**(d-1)):
					w= str(d-1);
					fmt= '%%%s.%sd'%(w,w)
					b= str(j)+(fmt % int(bin(i)[2:]) )
					v= int(b+k+b[::-1])
					#
					sq= v*v;
					r= check_palidrom(sq); 
					flag='';
					if r and ( X[0]<=v and X[1]>=v ):
						cnt+=1;
						flag='P';
	return cnt;

if __name__=='__main__':
	#
	T= int(sys.stdin.readline());
	for t in xrange(1,T+1):
		X= map( int, sys.stdin.readline().split() ) 
		r= fair_and_square(X)
		print 'Case #%d: %s' % (t,r);
	#
#


	
