input = open('./B-large.in', 'r')
output = open('./out', 'w')

num_cases = int(input.readline())
for i in range(num_cases):
	output.write("Case #"+str(i+1)+": ")
	params = input.readline().split()
	C = float(params[0])
	F = float(params[1])
	X = float(params[2])
	num_farms = 0
	rate = 2 + num_farms*F
	waiting_time = 0
	prev_time = X/rate
	while True:
		waiting_time += C/rate
		num_farms += 1
		rate = 2 + num_farms*F
		time_to_win = X/rate
		if time_to_win+waiting_time >= prev_time:
			break
		else:
			prev_time = time_to_win+waiting_time
	output.write(str("%.7f" % prev_time))
	output.write("\n")
input.close()
output.close()