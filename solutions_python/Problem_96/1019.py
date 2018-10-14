#!/usr/bin/env python

import string

ipt = open("q2l.i", "r")
opt = open("q2l.o", "w+")

cases = int(ipt.readline())
print cases

for case in range(cases) :
	print 
	args = ipt.readline().rsplit()
	N = int(args[0])
	print( "N=%d" % N )
	S = int(args[1])
	print( "S=%d" % S )
	p = int(args[2])
	print( "p=%d" % p )
	list = []
	ans = 0
	for i in range(N) :
#		print args[i+3]
		list.append(int(args[i+3]))
		a = list[i]/3
		min = max = a
		max_count = 1
		b = (list[i] - a)/2
		if b == max : max_count += 1
		if b < min : min = b
		if b > max : 
			max = b
			max_count = 1
		c = list[i] - a - b
		if c == max : max_count += 1
		if c < min : min = c
		if c > max : 
			max = c
			max_count = 1
		if a >= p or b >= p or c >= p :
			ans=ans+1
		elif max == p-1 and max-min < 2 and max_count > 1 and S > 0 and list[i] > 1:
			ans=ans+1
			S=S-1
		print max-min, a, b, c

#	list.sort()
#	list.reverse()

	print list, ans
		
	print( "Case #%d: %d" % (case+1, ans))

	opt.write("Case #%d: %d\n" % (case+1, ans))

ipt.close()
opt.close()




