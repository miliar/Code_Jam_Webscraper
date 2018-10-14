#!/usr/bin/env python

t = []

T = int(raw_input())
for case in xrange(1,T+1):
	n,m = tuple([int(x) for x in raw_input().split()])
	t = ['/']
	ans = 0

	for i in xrange(n):
		dir = raw_input()
		t.append(dir)

#	print t
			

	for j in xrange(m):
		dir = raw_input()
	 	s = dir.split('/')
#		print s

		new = ''
		for d in s[1:]:
			new += '/'+d
#			print "dir: ",new
			if new not in t:
				t.append(new)
				ans += 1

	print "Case #%d: %s" % (case, ans)
