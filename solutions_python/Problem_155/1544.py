from sys import stdin
import numpy as np
f = open('large.out','w')

T = int(stdin.next())

for i in xrange(1,T+1):
	(mShy,ltShy) =  stdin.next().split()
	mShy = int(mShy)
	ltShy = map(int,list(ltShy))
	nPerson = []
	result = 0
	for j in xrange(mShy+1):
		nPerson.append(sum(ltShy[:j]))

	for k in xrange(mShy+1):
		needperson = k - nPerson[k]
		if needperson <= 0:
			continue
		else:
			result += needperson
			for l in xrange(k+1,mShy+1):
				nPerson[l] += needperson


	print 'Case #%d:' %i,result
	print>>f, 'Case #%d:' %i,result
