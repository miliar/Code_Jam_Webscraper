import fileinput

def estimateTime(goal, speed):
	return goal/speed

def achieveFarm(C,speed):
	return C/speed

case = 0
C = -1
F = -1
X = -1
for line in fileinput.input():
	if case==0:
		case=1
		continue
	C,F,X = line.split()
	C = float(C)
	F = float(F)
	X = float(X)
	
	prevSpeed = 2
	speed = 2+F
	prevTime = estimateTime(X,prevSpeed)
	farmsTime = 0
	while prevTime > farmsTime + achieveFarm(C,prevSpeed) + estimateTime(X,speed):
		prevTime = farmsTime + achieveFarm(C,prevSpeed) + estimateTime(X,speed)
		farmsTime += achieveFarm(C,prevSpeed)
		prevSpeed = speed
		speed += F
	print "Case #"+str(case)+": "+str(prevTime)
	case+=1