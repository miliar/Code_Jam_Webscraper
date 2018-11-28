input = open("B-small-attempt1.in", 'r')
lines = input.readlines()
lines = [line.replace('\n', '') for line in lines]

out = open("output.txt", 'w+')

no_of_cases = int(lines[0])
start_line = 1

for case_no in xrange(1, no_of_cases + 1):
	case = lines[start_line]

	values = case.split()
	c = float(values[0])
	f = float(values[1])
	x = float(values[2])

	#print c, f, x
	possibilities = 100000.0

	for i in range(0,10000):
		speed = 2
		possibility = 0.0
		for _ in range(0,i):
			possibility += c/speed
			speed += f
		possibility += x/speed
		if possibility < possibilities:
			possibilities = possibility
		#print speed, possibility
	#print possibilities
	print possibilities
	out.write("Case #" + str(case_no)  + ": " + "%.7f" % possibilities + '\n')
	
	start_line += 1