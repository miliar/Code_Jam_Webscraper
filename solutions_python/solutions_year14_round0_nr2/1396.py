input_file = open('input', 'r')

num_cases = int(input_file.readline().strip())

def updated_cookies_per_sec():
	return cookies_per_sec + f

for i in xrange(num_cases):
	line = input_file.readline().strip().split(" ")
	c, f, x = map(float, line)
	cookies_per_sec = 2
	acctime = 0
	prev_time = x / cookies_per_sec

	while True:
		
		curr_time = acctime + (c / cookies_per_sec) + (x / updated_cookies_per_sec())
		
		if(curr_time > prev_time):
			print "Case #" + str(i+1) + ": " + str(prev_time)
			break

		acctime += (c / cookies_per_sec) 
		cookies_per_sec += f
		prev_time = curr_time




def calc_time(cookies_per_sec):
	return (c / cookies_per_sec) + (x / (cookies_per_sec + f))