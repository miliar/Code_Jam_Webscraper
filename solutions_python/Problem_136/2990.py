def timeToBuy(farmRequirement, farmRate, currentRate, goal, furtherNeed):
	timeReq = farmRequirement / currentRate
	goalTimeReqA = goal / (currentRate)
	goalTimeReqB = goal / (currentRate + farmRate)
	if goalTimeReqA - goalTimeReqB < timeReq:
		done = 1
		timeReq = furtherNeed / currentRate
	else:
		done = 0
	furtherNeed = furtherNeed
	newRate = currentRate + farmRate
	return [done, timeReq, newRate, furtherNeed]

#fin_name = "p2_input.in"
#fin_name = "B-small-attempt0.in"
fin_name = "B-large.in"
#fout_name = "p2.out"
fout_name = "p2large.out"
with open(fin_name) as fin:
    content = fin.readlines()

fout = open(fout_name, 'r+')

num_cases = content[0]

for case_index in range(1,int(float(num_cases)) + 1): 
	[C, F, X] = content[case_index].split()
	C = float(C)
	F = float(F)
	X = float(X)
	startRate = 2
	totalTime = 0
	keepGoing = 1
	run = [0, 0, startRate, X]
	#print run
	while (run[0] == 0):
		run = timeToBuy(C, F, run[2], X, run[3])
		totalTime = totalTime + run[1]
		#print run,run[1]
	#print "DONE in " + str(totalTime)
	
	fout.write("Case #"+str(case_index)+": " + str(totalTime) + "\n")

