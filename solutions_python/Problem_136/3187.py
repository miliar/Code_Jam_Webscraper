import sys

rl = lambda: sys.stdin.readline()
n = int(rl())

for i in range(n):
	line = rl().strip().split(' ')
	c = float(line[0])
	f = float(line[1])
	x = float(line[2])
	r = 2

	#print "%f %f %f" % (c, f, x)

	min_t = x/r

	farm_t1 = c/r 
	r += f
	farm_tt1 = x/r
	time = farm_t1

	#print farm_tt1
	
	while True:
		farm_t2 = c/r
		r2 = r + f
		#r2 += farm_t1
		farm_tt2 = x/r2

		if farm_tt2+farm_t2 > farm_tt1:
			time += farm_tt1
			break
		else:
			farm_t1 = c/r 
			r += f
			farm_tt1 = x/r
			time += farm_t1

	print "Case #%d: %.7f" % (i+1, min_t if min_t < time else time)		