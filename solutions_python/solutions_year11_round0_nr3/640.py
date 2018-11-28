f = lambda l: reduce(lambda z, x: z + [y + [x] for y in z], l, [[]])
T = int(raw_input())
for i in range(T):
	# read input data
	N = int(raw_input())
	candies = [int(j) for j in raw_input().split()]
	if reduce(lambda x, y: x^y, candies) != 0:
		print 'Case #%d: NO' % (i+1)
		continue
		
	result = sum(candies) - min(candies)
	print 'Case #%d: %s' % (i+1,result)