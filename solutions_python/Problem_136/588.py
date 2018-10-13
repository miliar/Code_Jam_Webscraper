filename = raw_input("filename: ")
f = open(filename,"r")
g = open("B.out","w")
num_tests = int(f.readline().rstrip())
for i in range(num_tests):
	line = f.readline().split()
	farm_cookies_required = float(line[0])
	farm_rate = float(line[1])
	win = float(line[2])
	time_needed = [] # element 0 is time taken with 0 farms etc
	timer = 0
	current_farms = 0
	def get_current_rate(num_farms):
		return 2 + current_farms*farm_rate
	def time_to_farm():
		return farm_cookies_required / get_current_rate(current_farms)
	def time_to_win():
		return win / get_current_rate(current_farms)
	win_time = timer + time_to_win()

	time_needed.append(win_time)
	while True:
		win_time = timer + time_to_win()
		timer += time_to_farm()
		
		if win_time > time_needed[current_farms]:
			g.write("Case #" + str(i+1) + ": " + str("{0:.7f}".format(time_needed[current_farms])))
			break
		else:
			time_needed.append(win_time)
			current_farms += 1
	if i < (num_tests-1):
		g.write("\n")
f.close()
g.close()


