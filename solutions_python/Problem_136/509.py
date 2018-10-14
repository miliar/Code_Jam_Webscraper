import sys

t = int(raw_input())

for i in xrange(t):
	c, f, x = [float(a) for a in raw_input().split()]
	rate = 2
	time = prev_time = x/rate
	farm_time = 0
	while time <= prev_time:
		prev_time = time
		farm_time += c/rate
		rate += f
		time = farm_time + (x/rate)
	print 'Case #%d: ' %(i+1) + str(prev_time)