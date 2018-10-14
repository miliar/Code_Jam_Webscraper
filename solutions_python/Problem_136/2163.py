a =  open('B-large.in')
num_cases = int(a.readline())

case = "Case #"
output_string = ""
def function(c, f, x):
	cookie_income = 2
	total_time = 0
	total_cookies = 0

	max_bound_attempts = int(x//c)
	minimum_time = (x/cookie_income)
	time = 0

	for j in range(max_bound_attempts):
		time += c/cookie_income
		cookie_income += f
		next_min_time = calculate_min_time(time, cookie_income, x)
		if(next_min_time < minimum_time):
			minimum_time = next_min_time
	return minimum_time
def calculate_min_time(time_passed, cookie_rate, cookies_to_win):
	time_left = (cookies_to_win/cookie_rate)
	return (time_passed + time_left)

for i in range(num_cases):
	settings = a.readline()
	settings_array = settings.split()

	cookie_cost = float(settings_array[0])
	cookie_raise = float(settings_array[1])
	cookie_win = float(settings_array[2])

	m_time = function(cookie_cost, cookie_raise, cookie_win)

	output_string += (case + str(i+1) + ": " + str("%.7f" % m_time) + "\n")

output = open('out_cookie_large.txt', 'w')
output.write(output_string)
output.close
a.close