"""
doc
"""
from sys import stdin


def playgame(farmcost, farmoutput, limit):
	cookiecount = 0.0
	production = 2.0
	endtime = 0.0
	farm_count= 0
	acumulated_build_farm_time = 0.0
	# time to reach the goal if nothing is built
	bestTime = (limit) / production

	while True:
		farm_count +=1
		
		acumulated_build_farm_time += farmcost / production
		production += farmoutput
		new_time = limit/production + acumulated_build_farm_time
		if new_time < bestTime:
			bestTime = new_time
		else:
			return "%0.7f" % bestTime


lines = []

T = int(stdin.readline().split()[0])

for i in range(T):
	line = stdin.readline().split()
	c = float(line[0])
	f = float(line[1])
	x = float(line[2])
	#print c, f, x
	endtime = playgame(c,f,x)

	print "Case #"+str(i+1)+": "+endtime