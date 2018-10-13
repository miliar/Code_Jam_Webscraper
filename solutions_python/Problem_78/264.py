inp = file("input")
T = inp.readline()
out = file("output", "w")
case = 0

for line in inp.readlines():
	case += 1
	line = line.split()
	N = int(line[0])
	Pd = int(line[1])
	Pg = int(line[2])
	i = 1
	calc = 'Broken'
	if (Pd != 100 and Pg == 100) or (Pd != 0 and Pg == 0):
		i = N + 1
	while i <= N:
		if i*(Pd/100.0) == int(i*(Pd/100.0)):
			calc = 'Possible'
		i += 1
	out.write("Case #" + str(case) + ": " + calc + "\n")
