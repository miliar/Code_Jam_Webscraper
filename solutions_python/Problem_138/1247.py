import copy

fi = open("input.txt")
fo = open("output.txt", "r+")

cases = int(fi.readline())

for c in range(cases):
	blocks = int(fi.readline())
	naoBlocks = map(float, fi.readline().rstrip().split())
	naoBlocks.sort()
	kenBlocks = map(float, fi.readline().rstrip().split())
	kenBlocks.sort()

	warNaoBlocks = copy.deepcopy(naoBlocks)
	warKenBlocks = copy.deepcopy(kenBlocks)
	warPoints = 0

	deceitNaoBlocks = copy.deepcopy(naoBlocks)
	deceitKenBlocks = copy.deepcopy(kenBlocks)
	deceitPoints = 0
	
	for b in range(blocks):
		nao = warNaoBlocks.pop(0)
		if(nao > warKenBlocks[-1]):
			ken = warKenBlocks.pop(0)
			warPoints += 1
		else:
			warKenBlocks.remove(next(x for x in warKenBlocks if x > nao))

	for b in range(blocks):
		nao = deceitNaoBlocks.pop(0)
		if (nao > deceitKenBlocks[0]):
			deceitKenBlocks.pop(0)
			deceitPoints += 1
		else:
			deceitKenBlocks.pop(-1)
	
	fo.write("Case #" + str(c + 1) + ": " + str(deceitPoints) + " " + str(warPoints) + "\n")