from sys import stdin
import pandas as pd
f = open('large.out','w')

T = int(stdin.next())

for i in xrange(1,T+1):
	N = int(stdin.next())
	m = map(int,stdin.next().split())
	m = pd.Series(m,index = range(N))
	m_new = m.copy()
	m_new.index = range(1,N+1)
	diff = m_new - m
	resultA = int(diff[diff > 0].sum())
	rate = diff.max()
	m[m >= rate] = rate
	resultB =  m[:-1].sum()

	print 'Case #%d:' %i,resultA,resultB
	print>>f, 'Case #%d:' %i,resultA,resultB
