f = file('B-large.in', 'r')
fo = file('B-large.out', 'w')

stdio = False

def get_input():
	if stdio:
		return raw_input()
	return f.readline()
	
def put_input(s):
	if stdio:
		print s
	else:
		fo.write(s)

num_cases = int(get_input())

for case in range(num_cases):
	cookie_farm_amount, cookie_farm_rate, win_amount = [float(item) for item in get_input().split(" ")]
	current_rate = 2.0
	total_time = 0.0
	while True:
		total_time += cookie_farm_amount / current_rate
		if (win_amount - cookie_farm_amount) / current_rate < win_amount / (current_rate + cookie_farm_rate):
			total_time += (win_amount - cookie_farm_amount) / current_rate
			break
		else:
			current_rate += cookie_farm_rate
	put_input("Case #{}: {}\n".format(case+1, total_time))