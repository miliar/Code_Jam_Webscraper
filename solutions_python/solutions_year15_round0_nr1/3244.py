#!/usr/bin/python2
def ssum(s):
	i = 0
	for x in s:
		i += int(x)
	return i
for i in xrange(input()):
	smax,data = raw_input().split()
	smax = int(smax)
	#print smax,data
	add = 0
	for x in xrange(smax+1):
		if ssum(data[:x]) + add < x:
			add += 1
	print 'Case #%d:'%(i+1),add