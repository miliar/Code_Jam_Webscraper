from math import fsum
T = input()
for i in xrange(T):
	N = input()
	sched = [raw_input() for j in xrange(N)]
	played = [sum(sched[j][k]!='.' for k in xrange(N)) for j in xrange(N)]
	print 'Case #%d:' % (i+1)
	OWP = [fsum(sum(sched[k][m]=='1' for m in xrange(N) if m!=j)/float(played[k]-(sched[k][j]!='.')) for k in xrange(N) if sched[j][k]!='.')/played[j] for j in xrange(N)]
	for j in xrange(N):
		print '%.6f' % (.25*sum(sched[j][k]=='1' for k in xrange(N))/(played[j]) + .5*OWP[j] + .25*fsum(OWP[k] for k in xrange(N) if sched[j][k]!='.')/(played[j]))