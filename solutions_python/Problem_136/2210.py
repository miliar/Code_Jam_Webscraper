def solve(T):
	arg = raw_input()
	c,f,x = [float(i) for i in arg.split(' ')]
	t = 0.0
	speed = 2.0

	while True:
		t += c / speed
		time_no_buy = (x - c) / speed
		time_buy = x / (speed + f)
		if time_no_buy < time_buy:
			t += time_no_buy
			break
		else:
			speed += f


	print 'Case #{T}: {pr}'.format(T=T+1, pr=t)

if __name__ == '__main__':
	T = int(raw_input())
	for i in range(T):
		solve(i)