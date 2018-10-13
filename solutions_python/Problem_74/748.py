import sys

file = open(sys.argv[1],"r")
output = ""
input = file.readlines()
file.close()
# print input
caseNo = 1
# caseNo = int(input[0])
input = input[1:]


while len(input) > 0:
	orangePos = 1
	bluePos = 1
	line = input.pop(0)
	line = line.split(" ")
	
	numberOfButtons = line.pop(0)
	oStepSinceMove = 0
	bStepSinceMove = 0
	totalsteps = 0
	while len(line) > 0:
		currentRobot = line.pop(0)
		requiredButton = int(line.pop(0))
		steps = 0
		if (currentRobot == "O"):
			dist = abs(requiredButton - orangePos)
			if dist > oStepSinceMove:
				steps = (dist-oStepSinceMove)+1
			else:
				steps = 1
			bStepSinceMove += steps
			oStepSinceMove = 0
			orangePos = requiredButton
		else:
			dist = abs(requiredButton - bluePos)
			if dist > bStepSinceMove:
				steps = (dist-bStepSinceMove)+1
			else:
				steps = 1
			oStepSinceMove += steps
			bStepSinceMove = 0
			bluePos = requiredButton
		totalsteps += steps
	output = output + "Case #" + str(caseNo) + ": " + str(totalsteps) + "\n"
	caseNo +=1

file = open(sys.argv[2],"w")
file.write(output)
file.close