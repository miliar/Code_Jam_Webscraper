import random 

fileIn = open("B-large.in", "r")
fileOut = open("output.in", "w")



loop = fileIn.readline().split()
#print loop[0], type(int(loop[0]))

for i in range(0, int(loop[0]) ):


	#First read in both card grids
	problem = fileIn.readline().split()
	C = float(problem[0])
	F = float(problem[1])
	X = float(problem[2])

	rate = 2
	minTime = X / rate
	
	sumC = 0

	while(1):
		sumC = sumC + (C / rate)
		rate = rate + F
		newTime = sumC + (X / rate)
	
		if( newTime < minTime ):
			minTime = newTime
		else:
			break

	

	#print(C, F, X, minTime)



	fileOut.write( "Case #" + str(i + 1) + ": " + str("%.7f" % minTime)  + "\n")

fileIn.close()
fileOut.close()
