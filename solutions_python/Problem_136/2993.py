#https://code.google.com/codejam/contest/2974486/dashboard#s=p1

def time_to_get(target, rate):
	return target / rate

def cookies_in_time(time, rate):
	return time / rate

def get_time(farm_price, farm_rate, win_score):
	cookies = 0.0
	rate = 2.0
	time = 0.0
	while cookies < win_score:
		if time_to_get(win_score - cookies, rate) <= time_to_get(farm_price - cookies, rate) + time_to_get(win_score - cookies, rate + farm_rate):
			time += time_to_get(win_score - cookies, rate)
			return time
		else:
			if cookies < farm_price:
				cookies += farm_price
				time += time_to_get(farm_price, rate)
			else:
				cookies -= farm_price
				rate += farm_rate
	return time

with open('input.in', 'r') as raw:
	lines = raw.readlines()[1:]
	with open('output.out', 'w') as output:
		for index, line in enumerate(lines):
			arguments = line[:-1].split(' ')
			output.write('Case #%i: %.7f\n' % (index + 1, get_time(float(arguments[0]), float(arguments[1]), float(arguments[2]))))