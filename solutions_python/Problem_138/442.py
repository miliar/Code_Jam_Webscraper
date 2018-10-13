import math

def playWar(n, naomiBlocks, kenBlocks):
	score = 0
	for i in range(0, n):
		n = naomiBlocks[0]
		beatingBlocks = [x for x in kenBlocks if x > n]
		if len(beatingBlocks):
			k = beatingBlocks[0]
		else:
			score += 1
			k = kenBlocks[0]
		naomiBlocks.remove(n)
		kenBlocks.remove(k)
	return score

def playDeceitfulWar(n, naomiBlocks, kenBlocks):
	score = 0
	for i in range(0, n):
		n = naomiBlocks[0]
		if n > kenBlocks[0]:
			k = kenBlocks[0]
		else:
			k = kenBlocks[-1]
		if (n > k):
			score += 1
		naomiBlocks.remove(n)
		kenBlocks.remove(k)
	return score

def solve(n, naomiBlocks, kenBlocks):

	return playWar(n, naomiBlocks, kenBlocks)

name = "D-large"
fi = open(name + ".in", "r")

fout = open(name + ".out", "w")

numTestCases = int(fi.readline())
print "#TestCases: ", numTestCases

for i in range(0, numTestCases):
	n = int(fi.readline())
	naomiBlocks = fi.readline().strip().split(" ")
	kenBlocks = fi.readline().strip().split(" ")

	naomiBlocks = map(float, naomiBlocks)
	kenBlocks = map(float, kenBlocks)
	naomiBlocks.sort()
	kenBlocks.sort()

	#fout.write("Case #" + str(i + 1) + ": " + str(solve(n, naomiBlocks, kenBlocks)) + "\n")
	fout.write("Case #" + str(i + 1) + ": " + str(playDeceitfulWar(n, naomiBlocks[:], kenBlocks[:])) + " " + str(playWar(n, naomiBlocks, kenBlocks)) + "\n")

fi.close()
fout.close()