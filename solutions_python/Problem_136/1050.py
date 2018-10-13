lines = open('B-large.in', 'r').read().splitlines()
line = iter(lines)

numCases = int(line.next())

outputFile = open('B-large.out', 'w')

for i in range(numCases):
	row = line.next().split(" ")
	c = float(row[0]) # cost of cookie farm
	f = float(row[1]) # additional rate of cookies per cookie farm
	x = float(row[2]) # how many cookies total?

	current_rate = 2
	num_farms = 0

	# how many cookie farms
	while x  / current_rate > ((c / current_rate) + x / (current_rate + f)):
		current_rate = current_rate + f
		num_farms = num_farms + 1
	# print num_farms

	# how much time?

	current_rate = 2
	time = 0
	for j in range(num_farms):
		time = time + c / current_rate
		current_rate = current_rate + f
	time = time + x / current_rate
	outputFile.write("Case #" + str(i + 1) + ": " +  str(time) + "\n")