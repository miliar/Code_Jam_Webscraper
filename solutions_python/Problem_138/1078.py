import sys

filename = "D-large"

def solve_case(blocks, naomis, kens):
	naomis.sort()
	kens.sort()
	kens.reverse()

	deciet_wins = 0
	kens_worst = blocks - 1
	for naomi in naomis:
		if naomi > kens[kens_worst]:
			kens_worst -= 1
			deciet_wins += 1

	naomis.reverse()

	kens_war = kens[:]
	war_wins = 0
	for naomi in naomis:
		if naomi > kens_war[0]:
			war_wins += 1
		else:
			# remove min card ken has to play
			for i in range(len(kens_war)):
				if kens_war[i] < naomi:
					del kens_war[i-1]
					break

	ret = (deciet_wins, war_wins)
	return ret

def readInt(inFile):
	return int(inFile.readline())

def readFloats(inFile):
	return [float(n) for n in inFile.readline().split(" ")]

def readInts(inFile):
	return [int(n) for n in inFile.readline().split(" ")]

with open(filename + ".in", 'r') as inFile:
	output_data = []

	# parse input
	T = readInt(inFile)
	for t in range(T):
		blocks = readInt(inFile)
		naomi = readFloats(inFile)
		ken = readFloats(inFile)
		(deciet_wins, war_wins) = solve_case(blocks, naomi, ken)
		output_data.append("Case #%s: %s %s" % (t+1, deciet_wins, war_wins))

	if len(output_data) > 0:
		with open(filename + ".out", 'w') as outFile:
			outFile.write("\n".join(output_data))
	else:
		print("no output")




