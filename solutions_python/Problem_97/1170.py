#!/usr/bin/python2.5
# Google Code Jam 2012 - Qualification Round - Problem C - Mateusz Kurek

t = int(raw_input())
for i in xrange(1,t+1):
	count = 0
	l,r = [int(x) for x in raw_input().split()]
	digits = len(str(l))
	for n in xrange(l,r):
		nStr = str(n)
		# for every digit-pack of length d
		for d in xrange(1,digits):
			newNumber = int("".join([nStr[-d:], nStr[0:-d]]))
			if newNumber > n and newNumber <= r: 
				count += 1
				#break
	print "Case #%d: %d" %(i,count)
