
inp = open('input.dat','r')
out = open('output.dat','w')

for case in xrange(int(inp.readline())):
	
	input_info = [float(x) for x in inp.readline().split(' ')]
	C = input_info[0] # Cost per farm
	F = input_info[1] # Rate per farm
	X = input_info[2] # Cookies to get

	Rate = 2.0
	f_Rate = 0.0
	time = 0.0
	n_farms = 0

	if case!=0:
		out.write('\n')

	while True:
		time_to_goal = (X/Rate) + time
		time_to_farm = (C/Rate)

		f_Rate = Rate + F

		time_if = (X/f_Rate) + time + time_to_farm

		if time_if < time_to_goal:
			Rate = f_Rate
			n_farms+=1
			time+=time_to_farm
		else:
			out.write("Case #{}: {:0.7f}".format(case+1,time_to_goal))
			break