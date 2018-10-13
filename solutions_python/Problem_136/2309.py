with open('input') as fin:
	num_cases = int(fin.readline())

	cases = []
	for i in range(num_cases):
		cases.append(map(float, fin.readline().strip().split()))

#
#
#
#
#
#
#
#
#
#
#

for index, case in enumerate(cases, 1):
	c, f, x = case

	rate = 2
	time = 0
	while (x / rate) > (x / (rate + f)) + (c / rate):
		time += (c / rate)
		rate += f

	time += (x / rate)

	print "Case #{}: {}".format(index, time)
