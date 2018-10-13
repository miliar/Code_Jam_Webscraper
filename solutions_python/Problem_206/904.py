def test():
	d,n = map(int,raw_input().split(' '))
	time = 0
	for _ in xrange(n):
		k,s = map(float,raw_input().split(' '))
		time = max(time, (d-k)/s)
	print "{:.6f}".format(d/time)


t = input()
for i in range(1,t+1):
	print "Case #"+str(i)+":",
	test()