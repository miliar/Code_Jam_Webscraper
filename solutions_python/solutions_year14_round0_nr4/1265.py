from __future__ import division

infile = """INPUT"""

def greaterThanXInList(x,aList):
	try:
		value = next(k[0] for k in enumerate(aList) if k[1] > x)
	except StopIteration:
		value = -1 # Play the smallest one, idgaf now
	return value
	
def normalTurn(opponent,myValues):
	value = myValues.pop(greaterThanXInList(opponent,myValues))
	return value, myValues

def optimalTurn(naomi,ken):
	# Ken has a block that's bigger than Naomi's biggest
	if greaterThanXInList(naomi[0],ken) != -1:
		nSay = ken[0]-0.00000001
		nPlay = naomi.pop(-1)
	else:
		nSay = ken[0]+0.00000001
		using = 0
		kenPlay = ken[-1]
		for i, v in enumerate(naomi):
			if v > kenPlay:
				using = i
		nPlay = naomi.pop(using)

	return nPlay, naomi, nSay

def _play(naomi,ken,optimal):
	naomi.sort(reverse=True)
	ken.sort(reverse=True)

	totalTurns = len(naomi)
	turn = 1

	nPts, kPts = 0, 0

	while turn <= totalTurns:
		#print turn
		if optimal:
			nPlay, naomi, nSay = optimalTurn(naomi,ken)
		else:
			nPlay = naomi.pop(0)
			nSay = nPlay

		kPlay, ken = normalTurn(nSay,ken)

		#print nSay, nPlay, kPlay

		if nPlay > kPlay:
			assert(nSay > kPlay)
			nPts += 1
		else:
			assert(nSay < kPlay)
			kPts += 1

		turn += 1
		#print nPts,kPts

	return nPts


def getResults(naomi,ken):
	return str(_play(list(naomi),list(ken),True)) + ' ' + str(_play(list(naomi),list(ken),False))

lines = infile.split('\n')

casenum = 0
index = 0
while len(lines) >= index+2:
	casenum += 1
	print 'Case #{}: {}'.format(casenum,getResults(
		[float(k) for k in lines[index+1].split(' ')],
		[float(k) for k in lines[index+2].split(' ')]))
	index += 3
