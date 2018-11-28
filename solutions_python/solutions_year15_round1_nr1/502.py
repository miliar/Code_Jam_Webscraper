from sys import stdin

cases = int(stdin.readline())

for case in xrange(cases):
	n = int(stdin.readline())
	mushroomtimes = map(lambda x: int(x), stdin.readline().split(' '))
	first = 0
	second = 0
	last = 0
	rate = 0
	for i in mushroomtimes:
		if last > i:
			first += (last-i)
		if (last - i) > rate:
			rate = last - i
		last = i

	last = 0
	for i in mushroomtimes[:-1]:
		if i > rate:
			second += rate
		else:
			second += i
	
		last = i

	

	print "Case #%d: %d %d" % (case+1, first, second)

