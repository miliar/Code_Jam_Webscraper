T = int(raw_input())

def makePair(combinaisons,a,b):
	if (a+b) in combinaisons:
		return combinaisons[a+b]
	else:
		return None
	
def isInconsistent(L,element,opposites):
	if element not in opposites:
		return False
	possibleInconsistentElements = opposites[element]
	for possibleInconsistentElement in possibleInconsistentElements:
		if possibleInconsistentElement in L:
			return True
	return False

def solveCase(combinaisons,opposites,invocations):
	L = []
	for element in invocations[0]:
		#print "Element : %s " % (element)
		if L:
			change = makePair(combinaisons,L[-1],element)
			if change:
				L.pop()
				L.append(change)
			elif isInconsistent(L,element,opposites):
				L = []
			else:
				L.append(element)
		else:
			L.append(element)
	#print "After element %s L is : %s" % (element,L)
	return L
		
for t in range(1,T+1):
	l = raw_input().split()
	pos = 0
	
	C = int(l[pos])
	combinaisonsA = l[pos+1:pos+C+1]
	pos += C+1
	#print "Combinaisons : %s " % (combinaisonsA)
	
	combinaisons = {}
	for combinaison in combinaisonsA:
		combinaisons[combinaison[0]+combinaison[1]] = combinaison[2]
		combinaisons[combinaison[1]+combinaison[0]] = combinaison[2]
	#print "Combinaisons dict : %s " % (combinaisons)
	
	D = int(l[pos])
	oppositesA = l[pos+1:pos+D+1]
	pos += D+1
	#print "Opposites : %s " % (oppositesA)
	opposites = {}
	for opposite in oppositesA:
		if opposite[0] not in opposites:
			opposites[opposite[0]] = set()
		opposites[opposite[0]].add(opposite[1])
		if opposite[1] not in opposites:
			opposites[opposite[1]] = set()
		opposites[opposite[1]].add(opposite[0])
			
	#print "Opposites : %s " % (opposites)
	
	N = int(l[pos])	
	invocations = l[pos+1:pos+N+1]
	#print "Invocations : %s " % (invocations)
	
	
	sol = solveCase(combinaisons,opposites,invocations)
	solFormatted = '['
	for i,e in enumerate(sol):
		solFormatted += e
		if i != len(sol)-1:
			solFormatted += ', '
	solFormatted += ']'
	print "Case #%d: %s" % (t,solFormatted)