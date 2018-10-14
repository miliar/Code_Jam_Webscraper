rate = 2

def mintime(cost, bonus, goal):
	rate = 2
	mintime = goal/rate
	maxfarms = 0
	while True:
		maxfarms += 1
		farms = 0
		time = 0
		rate = 2
		while farms < maxfarms:
			time += cost/rate
			farms += 1
			rate += bonus
		time += goal/rate
		if time < mintime:
			mintime = time
		else:
			break
	return mintime

infile = open("2014B.in")
outfile = open("2014B.out", "w")

for i in range(int(infile.readline())):
	args = tuple(map(float, infile.readline().split()))
	outfile.write("Case #" + str(i+1) + ": " + str(round(mintime(*args), 7)) + "\n")

outfile.close()
