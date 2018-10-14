import sys
def unit_check(u):
	u= list(set(u));
	if 'T' in u:
		u.remove('T')
	s= ''.join( sorted(u) )
	if s in ['O','X']:
		return s;
	if '.' in s:
		return 'G';
	return None;

def tic_tac_toe_tomek(m):
	M= len(m)
	sig= ['O','X'];
	col=[ [] for i in xrange(M) ]
	diag=[ [], [] ]
	for j,row in enumerate(m):
		for i,t in enumerate(row):
			col[i]+= t;
		diag[0]+= m[j][j]
		diag[1]+= m[(M-1)-j][j]
	U =[ u for u in m]
	U+=[ u for u in col]
	U+=[ u for u in diag]
	#
	flag= 'D';
	for u in U:
		r= unit_check( u );
		if r==None:
			continue;
		flag= r;
		if flag in sig: 
			return flag
	return flag

if __name__=='__main__':
	response={\
		'O':'O won',\
		'X':'X won',\
		'D':'Draw',\
		'G':'Game has not completed',\
	}
	T= int(sys.stdin.readline());
	for t in xrange(1,T+1):
		x= list( sys.stdin.readline().strip() ) 
		m= [ x ]
		for i in xrange( 1, len(m[0]) ):
			x= list( sys.stdin.readline().strip() )	
			m.append( x )
		sys.stdin.readline()
		r= tic_tac_toe_tomek(m)
		print 'Case #%d: %s' % (t,response[r]);
##

	
