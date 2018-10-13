import fileinput as f

def time_to_win(x, rate):
	return x / rate

def time_to_buy_farm(c, rate):
	return c / rate

def eval_case(cfx):
	rate = 2.0
	time = 0
	while 1:
		a = time_to_win(cfx[2],rate)
		b = time_to_buy_farm(cfx[0],rate)
		if (time_to_buy_farm(cfx[0],rate) + time_to_win(cfx[2],rate+cfx[1])) < time_to_win(cfx[2],rate):
			time += time_to_buy_farm(cfx[0],rate)
			rate += cfx[1]
		else:
			return time + time_to_win(cfx[2],rate)

def parse_input():
	cases  = 0
	case_n = 1

	for x in f.input():
		if f.isfirstline():
			cases = int(x)
		elif case_n > cases:
			break
		else:
			print "Case #%s: %s" % (case_n, eval_case([float(x) for x in x.split()]))
			case_n +=1

parse_input()