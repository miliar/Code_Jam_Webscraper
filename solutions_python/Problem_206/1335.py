def run():
	k,n = map(int,raw_input().split(' '))
	time = 0
	for _ in xrange(n):
		l,a = map(float,raw_input().split(' '))
		time = max(time, (k-l)/a)
	print "{:.6f}".format(k/time)


t = input()
for i in range(1,t+1):
	print "Case #"+str(i)+":",
	run()
