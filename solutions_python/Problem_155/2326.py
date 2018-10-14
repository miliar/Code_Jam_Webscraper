from __future__ import print_function
import sys
T=int(sys.stdin.readline())
def solve(smax,S):
	t=0;r=0
	for i in xrange(0, len(S)):
		ss=int(S[i])
		if ss+t<i+1:
			x=i+1-(ss+t)
			t+=ss+x
			r+=x
		else:
			t+=ss
	return r;
for i in xrange(0, T):
	(smax,S)=sys.stdin.readline().strip().split(' ')
	answer=solve(int(smax),S)
	print('Case #{0}: {1}'.format(i+1,answer))

	