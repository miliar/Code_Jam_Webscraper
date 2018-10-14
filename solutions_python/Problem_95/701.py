#!/usr/bin/python
import os,sys

mp=('y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q')

cs=int(raw_input())
for cs in xrange(cs):
	x=raw_input()
	opt=[]
	for c in x:
		if(ord(c)<=ord('z') and ord(c) >=ord('a')):
			opt.append(mp[ord(c)-ord('a')])
		else:
			opt.append(c)
	print "Case #%d: %s\n"%(cs+1,''.join(opt)),
"""

	except:
		pass

while True:
	x=raw_input()
	y=raw_input()
	l=-1
	for c in x.strip():
		l+=1
		if(ord(c)<=ord('z') and ord(c) >=ord('a')):
			ld[ord(c)-ord('a')]=y[l]
	print('\',\''.join(ld))
"""

