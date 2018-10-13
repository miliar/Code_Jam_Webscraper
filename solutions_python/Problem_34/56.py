#!/usr/bin/env python
import re, sys
#f=open('a.in').readlines()
f=sys.stdin.readlines()
#read L, D N
L,D,N=map(int,f[0].rstrip('\n').split(' '))

#build alien words dictionary
words=[]
for i in range(D):
		words.append(f[i+1].rstrip('\n'))
#for each word, test possibility
for i in range(1,N+1):
		rule=f[D+i].rstrip('\n').replace('(','[').replace(')',']')+'$'
		count = 0
		for word in words:
				if not re.match(rule,word)==None:
						count += 1
		print 'Case #%d: %d' % (i, count)

