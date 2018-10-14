from sys import stdin


def solve(c, f, x):
	cookies = 0	# cookies at the moment
	f0 = 2	# initial cookies per second
	time = 0
	for i in range(0, 100000):
		time_without_farm = (x - cookies) / (f0 + f * i)
		debug('twof: ' + str(time_without_farm))
		farm_time = (c - cookies) / (f0 + f * i)
		debug('ft: ' + str(farm_time))
		x_time = x / (f0 + f * (i + 1))
		debug('xt: ' + str(x_time))
		time_with_farm = farm_time + x_time
		debug('twf: ' + str(time_with_farm))
		if time_with_farm < time_without_farm:
			time += farm_time
		else:
			time += time_without_farm
			break
	return time


def debug(s):
	pass
	# print(s)


if __name__ == '__main__':
	t = int(stdin.readline())
	for i in range(0, t):
		s = stdin.readline().split(' ')
		c, f, x = [float(k) for k in s]
		print('Case #{}: {}'.format(i + 1, solve(c, f, x)))
