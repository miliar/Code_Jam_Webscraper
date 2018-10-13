n = int(raw_input())
for i in range(0,n):
	line = raw_input()
	line = line.split()
	
	cost = float(line[0])
	plus = float(line[1])
	totl = float(line[2])

	time_f = 0.0
	num_f = 0.0
	frec = 2.0

	res = totl / frec
	while(True):
		num_f += 1
		time_f += cost / frec

		frec += plus

		time_t = totl / frec

		if((time_f + time_t) < res):
			res = time_f + time_t
		else:
			break

	print 'Case #' + str(i+1) + ': ' + '{0:.7f}'.format(res)