import math

input = open("C-small-1-attempt4.in")
numberOfInputs = int(input.readline())
t = 1


def updateDistances(stalls):
	for i in range(1, len(stalls) - 1):
		if (stalls[i][0] == "o"):
			L = 0
			while (stalls[i - L - 1][0] != "x"):
				L += 1
			R = 0
			while (stalls[i + R + 1][0] != "x"):
				R += 1
			stalls[i] = ("o", L, R, min(L, R), max(L, R))
			

def chooseStall(stalls):
	for j in range(1, len(stalls) - 1):
		if (stalls[j][0] == "o"):
			maxDistance = stalls[j]
			maxDistanceIndex = j
			break
	i = 1
	for stall in stalls[1:-1]:
		if stall[3] > maxDistance[3] or (stall[3] == maxDistance[3] and stall[4] > maxDistance[4]):
			maxDistance = stall
			maxDistanceIndex = i
		i += 1
	return maxDistanceIndex
			


def occupyStall(stalls, i):
	stall = stalls[i]
	stalls[i] = ("x", 0, 0, 0, 0)
	updateDistances(stalls)
	return (stall[3], stall[4])


for line in input:
	tokens = line.split()
	N = int(tokens[0])
	K = int(tokens[1])
	stalls = list()
	stalls.append(("x", 0, 0, 0, 0 ))
	for i in range(N):
		L = i
		R = N - i - 1
		stalls.append(("o", L, R, min(L, R), max(L, R)))
	stalls.append(("x", 0, 0, 0, 0 ))
	for i in range(K):
		# print "Step" + str(i)
		# print stalls
		nextStall = chooseStall(stalls)
		# print "Choosing stall: " + str(nextStall)
		result = occupyStall(stalls, nextStall)
	print "Case #" + str(t) + ": " + str(result[1]) + " " + str(result[0])
	t += 1
