


def TimeWithFarm(farmNumber, C, F, X) :
	bR = 2.0
	R = 0
	time = 0
	for i in xrange(farmNumber) :
		R = bR + i*F
		time += C / R
		# print time
	R = bR + farmNumber*F 
	time += X / R
	# print X / R
	return time

#print TimeWithFarm(3, 500.0,4.0,2000.0)

# Suppose that when time goes up, optimization stops
def MinimumTime(C, F, X) :
	temp = TimeWithFarm(0, C, F, X)
	optimal = temp
	i = 0
	while ( True  ) :
		i = i + 1
		temp = TimeWithFarm(i, C, F, X)
		if temp < optimal :
			optimal = temp
		else :
			return optimal



# print MinimumTime( 500.0,4.0,2000.0)

f = open("B-small-attempt0.in")
lines = map(lambda x : x.strip("\n"),f.readlines())
outputlines = []

# parse input
testCases = int(lines[0])
for i in range(testCases) :
	# print lines[i+1]
	infos = map(lambda x : float(x), lines[i+1].split(" "))
	# base cookies/s
	R = 2.0 
	C = infos[0]
	F = infos[1]
	X = infos[2]
	print ("%.7f" % MinimumTime(C, F, X))
	outputlines.append("Case #{0}: {1:.7f}".format((i+1),  MinimumTime(C, F, X)) )


print outputlines

outputfile = open("output.txt","w")
outputfile.writelines(map(lambda x : str(x) + "\n", outputlines))