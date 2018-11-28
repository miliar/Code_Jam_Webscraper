inputFile = raw_input("Input File: ")
with open(inputFile) as fin:
	content = fin.readlines()
fin.close()

def getFirst(stuff):
	return stuff.pop(0)

def checkMatched(l1, l2): #true if l1 > l2 pairwise
	l1.sort()
	l2.sort()
	for i in range(len(l1)):
		if l2[i] > l1[i]:
			return False
	return True

n = int(getFirst(content))
output = ""

#Ken's strategy: choose lightest block heavier than Naomi's
#if no such block exists, choose lightest block

#Naomi's deceit: wear down Ken, choose lightest but tell him
#they're almost as heavy as his heaviest
#when Naomi's lights > Ken's heaviest, start playing truthfully

#Naomi's honest: start light, go heavy

for i in range(n):
	blocksPer = int(getFirst(content))
	naomiBlocks = map(float, getFirst(content).split())
	kenBlocks = map(float, getFirst(content).split())

	#first try Naomi's deceit

	currentNaomi = naomiBlocks[:]
	currentKen = kenBlocks[:]

	while len(currentNaomi) > 0 and not checkMatched(currentNaomi, currentKen): # (min(currentNaomi) < max(currentKen)):
		currentNaomi.remove(min(currentNaomi))
		currentKen.remove(max(currentKen))

	deceitPoints = len(currentNaomi)

	#now, Naomi's honest

	currentNaomi = sorted(naomiBlocks)
	currentKen = sorted(kenBlocks)
	honestPoints = 0

	for j in range(blocksPer):
		if currentNaomi[j] > max(currentKen):
			honestPoints += 1
			currentKen.remove(min(currentKen))
		else:
			kensPlay = 1
			for num in currentKen:
				if num > currentNaomi[j] and num < kensPlay:
					kensPlay = num
			currentKen.remove(kensPlay)

	output += "Case #" + `i + 1` + ": " + `deceitPoints` + " " + `honestPoints` + "\n"

f = open("warOutput.txt", 'w')
f.write(output)
f.close()
