import sys
import math

argList = sys.argv
filename = argList[1]
f = file(filename, 'r')
out = file('output.txt', 'w')
lines = f.readlines()
f.close()
cases = int(lines[0])

for case in range(1, cases+1) :
	cps = 2.0 #cookies per second
	timeElapsed = 0.0 #init time

	inputs = lines[case].strip().split(' ')	
	farmCost = float(inputs[0])
	cookieGain = float(inputs[1])
	cookieGoal = float(inputs[2])

	timeToReach = cookieGoal/cps
	timeToFarm = farmCost/cps
	cpsIfFarm = cps + cookieGain
	timeIfFarm = timeToFarm + cookieGoal/cpsIfFarm

	while timeToReach - timeIfFarm > 1e-8 :
		#print cps,'\t',  timeToFarm, '\t', timeToReach, '\t', timeIfFarm, '\n', 
		#do it
		timeElapsed = timeElapsed + timeToFarm
		cps = cpsIfFarm

		#update
		timeToReach = cookieGoal/cps
		timeToFarm = farmCost/cps
		cpsIfFarm = cps + cookieGain
		timeIfFarm = timeToFarm + cookieGoal/cpsIfFarm

	out.write('Case #' + str(case) + ': ' + str(timeToReach + timeElapsed) + '\n')
