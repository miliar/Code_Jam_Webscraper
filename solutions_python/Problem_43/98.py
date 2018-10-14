cases = int(raw_input())

strmap = '1023456789abcdefghijklmnopqrstuvwxyz'

for i in xrange(0,cases):

	num = raw_input()
	num_map = {}

	mn = 0
	for x in xrange(0,len(num)):
		if num[x] in num_map:
			continue
		num_map[num[x]] = strmap[mn]
		mn+=1
	
	num = ''.join(map(lambda x: num_map[x], num))


	best = 10**18+1
	for b in xrange(2,37):
		try:
			n = int(num,b)
			if n < best:
				best = n
		except ValueError:
			pass

	print "Case #%d: %d" % (i+1,best)
