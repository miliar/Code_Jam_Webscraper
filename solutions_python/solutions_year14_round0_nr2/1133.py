#!/usr/bin/env python
input = "B-small-attempt0.in"
with open(input) as myfile:
	lines = myfile.read().splitlines();

count = int(lines[0]);

myfile = open('B-small-attempt0.out','w')

for i in range(count):
	cfx = lines[i + 1].split(" ")
	c = float(cfx[0])
	f = float(cfx[1])
	x = float(cfx[2])

	time = 0.0
	rate = 2

	if (x <= c):
		time = round(x / rate, 7)
	else:
		#print "new!!!!!!!!!!!!!!!!", f
		newfarm = x/(rate+f) + c/rate - x/rate
		while (newfarm < 0):
			time += round(c / rate, 7)
			#print round(c / rate, 7), "   time:", time, "        rate:", rate
			rate += f

			newfarm = x/(rate+f) + c/rate - x/rate
		time += round(x / rate, 7)

	myfile.write("Case #{0}: {1:.7f}\n".format(i + 1, time))

myfile.close()