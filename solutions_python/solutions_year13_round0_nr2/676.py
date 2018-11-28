import sys
from itertools import chain

def lawnmower(N,M,L):
	S =[];
	for j,row in enumerate(L):
		for i,h in enumerate(row):
			if h!=0:
				 continue;
			xv= row;
			yv= [ L[jj][i] for jj in range(N) ]
			obstacle= min(max(xv),max(yv));
			if obstacle: 
				return False
	return True;

if __name__=='__main__':
	response= ['NO','YES'];
	T= int( sys.stdin.readline() );
	for t in xrange(1,T+1):
		[N,M]= map(int, sys.stdin.readline().split() ) 
		L=[]
		for j in xrange(N):
			row= map(int,sys.stdin.readline().split())
			L.append( row ) 
		f= list(chain.from_iterable(L));
		base= min(f);
		L= [ [x-base for x in row] for row in L]
		r= lawnmower(N,M,L);
		print 'Case #%d: %s' % (t,response[r]);
##

	
