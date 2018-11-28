def solve(cost, ecps, toWin):
	time = 0
	cps = 2.0
	while toWin / cps > (cost / cps) + (toWin / (cps + ecps)):
		time += cost / cps
		cps += ecps
	time += toWin / cps
	return time


for t in range(int(input())):
	cost, ecps, toWin = tuple(float(s) for s in input().split(" "))
	print("Case #" + str(t+1) + ": " + str(solve(cost, ecps, toWin)))
