from sys import stdin

for case in xrange(int(input())):
	c, f, x = [float(x) for x in stdin.readline().split()]
	rate = 2.0
	time = c / rate
	while ((x - c) / rate > x / (rate + f)):
		rate += f
		time += c / rate
	time += (x - c) / rate
	print('Case #{}: {:10.7f}'.format(case + 1, time))
