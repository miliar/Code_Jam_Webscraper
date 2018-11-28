import sys
def gcd(x, y):
	# euclidean algorithm
	while y <> 0:
		t = y
		y = x % y
		x = t
	return x
def maxRemainder(divisor, list):
	if not list:
		return 0
	#print "got", (list[0] % divisor), "for list[0]=", list[0], "divisor=", divisor
	blah = 0
	for c in list:
		blah = max(blah, c % divisor)
	return blah
#
C = long(raw_input())
for c in range(0, C):
	stuff = raw_input().split(' ')
	N = long(stuff[0])
	# convert to longs
	ts = map(lambda x: long(x), stuff[1:])
	ts.sort()
	# calculate differences
	diffs = map(lambda x,y: y-x, ts[:-1], ts[1:])
	# calculate gcd of differences
	T = reduce(gcd, diffs)
	#print "T is", T
	# determine smallest value of y
	y = 0
	while 1:
		#print "trying with y=",y 
		md = maxRemainder(T, map(lambda x: x + y, ts))
		#print "md=",md
		if md == 0:
			print "Case #%d: %d" % (c + 1, y)
			break
		else:
			y += T-md
