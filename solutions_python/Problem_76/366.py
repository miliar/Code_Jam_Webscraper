import sys
T=int(sys.stdin.readline().strip())
for t in range(1,T+1):
	N=int(sys.stdin.readline().strip())
	Cs=map(int,sys.stdin.readline().strip().split(' '))
	xs = 0
	for c in Cs: xs ^=c
	
	if xs!=0:
		print 'Case #%d: NO' % t
		continue
	
	Cs.sort()
	print 'Case #%d: %d' % (t,sum(Cs[1:]))

