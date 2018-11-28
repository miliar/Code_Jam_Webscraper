import math
f = open('in.txt', 'r')

num = int(f.readline())
for t in xrange(1, num+1):
	minS, maxS = ((f.readline()).split())
		
	min = int(math.ceil(math.sqrt(float(minS))))
	max = int(math.floor(math.sqrt(float(maxS))))
	
	count = 0
	for i in xrange(min, max + 1):
		if str(i) == str(i)[::-1]:
			num = i*i
			if str(num) == str(num)[::-1]:
				count += 1
	
	print 'Case #{0}: {1}'.format(t,count)
	