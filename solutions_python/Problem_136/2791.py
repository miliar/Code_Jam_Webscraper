from __future__ import division
from cjlib.input import *
from cjlib.runner import TaskRunner, DummyRunner
from itertools import permutations

get("""5
500.0 4.0 2000.0
30.0 1.0 2.0
30.0 2.0 100.0
30.50000 3.14159 1999.19990
500.0 4.0 2000.0""")

def process(data):
	farm, farmGrow, target = [float(x) for x in data.split(" ")]
	cookie = 0.0
	cookieRate = 2.0
	timeTaken = 0.0
	while cookie < target:
		timeToTargetIfFarm = (target - max(0, cookie-farm))/(cookieRate + farmGrow)
		timeToTargetNoFarm = (target-cookie)/cookieRate
		timeToNextFarm = (farm-cookie)/cookieRate
		if timeToNextFarm > 0:
			timeToTargetIfFarm += timeToNextFarm

		#print "Has:", cookie, "Decision:", timeToTargetNoFarm, "no farm", timeToTargetIfFarm, "if farm"

		if timeToTargetIfFarm < timeToTargetNoFarm:
			if cookie < farm:
				timeTaken += timeToNextFarm
				cookie += timeToNextFarm * cookieRate
				#print "Waiting", timeToNextFarm, "to get", cookie, "cookies to buy farm", farm
			else:
				cookie -= farm
				cookieRate += farmGrow
				#print "Farm bought! Cookie rate is", cookieRate
		else:
			# we could reach target?
			timeTaken += timeToTargetNoFarm
			cookie += timeToTargetNoFarm * cookieRate
			#print "Waiting", timeToTargetNoFarm, "to target."
	#print "out", "%0.7f"%timeTaken
	#print
	return "%0.7f"%timeTaken

r = TaskRunner(process, DummyRunner)

while neof():
	r.add(line())

r.run(True)