import sys

try: 
	f = open(sys.argv[1])
	out = open(sys.argv[1].rpartition("\\")[2]+".out", 'w')

	numTests = int(f.readline())

	for i in range(0,numTests):
		vals = f.readline()[0:-1].split(" ")
		
		farm_cost = float(vals[0])
		farm_rate = float(vals[1])
		win_val = float(vals[2])

		COOKIES_PS = 2

		farms = 0.0
		time = 0.0

		while (True):
			fps = farms * farm_rate
			next_farm_n_win = (farm_cost/(COOKIES_PS + fps)) + (win_val/(COOKIES_PS + fps + farm_rate))
			next_win = win_val/ (COOKIES_PS + fps)
			if next_win < next_farm_n_win:
				time += win_val/(COOKIES_PS + fps)
				break
			else:
				time += farm_cost/(COOKIES_PS + fps)
				farms += 1
		print "Test " + str(i+1) + " finished"
		out.write("Case #" + str(i+1) +": " +"%.7f" %time + "\n")



except IOError, e:
	print "Error %d: %s"%(e.args[0], e.args[1])

