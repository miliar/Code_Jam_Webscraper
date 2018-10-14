
Dijkstra = dict()
Dijkstra[('1','1')] = [1,'']   #second argument isPositif
Dijkstra[('1','i')] = [1,'i']
Dijkstra[('1','j')] = [1,'j']
Dijkstra[('1','k')] = [1,'k']

Dijkstra[('i','1')] = [1,'i']
Dijkstra[('i','i')] = [-1,'']
Dijkstra[('i','j')] = [1,'k']
Dijkstra[('i','k')] = [-1,'j']

Dijkstra[('j','1')] = [1,'j']
Dijkstra[('j','i')] = [-1,'k']
Dijkstra[('j','j')] = [-1,'']
Dijkstra[('j','k')] = [1,'i']

Dijkstra[('k','1')] = [1,'k']
Dijkstra[('k','i')] = [1,'j']
Dijkstra[('k','j')] = [-1,'i']
Dijkstra[('k','k')] = [-1,'']

def OneFunction(stringGiven):
	signPositif = 1
	lookfor = 'ijk'
	posLookFor = 0

	if len(stringGiven)<3:
		return "NO"

	if stringGiven == 'ijk':
		return 'YES'

	while(len(stringGiven)) > 3 and posLookFor < 3:
		#print 'stringGiven[0]', stringGiven[0]
		#print 'stringGiven[1]', stringGiven[1]
		#print posLookFor
		if lookfor[posLookFor] == stringGiven[posLookFor]:
			posLookFor +=1
			continue
		else:
			oneD = Dijkstra[(stringGiven[posLookFor+0],stringGiven[posLookFor+1])]
			stringGiven = lookfor[:posLookFor] + oneD[1]+ stringGiven[posLookFor+2:]
			signPositif *= oneD[0]
	#print 'stringGiven', stringGiven

	while len(stringGiven[posLookFor:]) >1:
		oneD = Dijkstra[(stringGiven[posLookFor+0],stringGiven[posLookFor+1])]
		stringGiven = lookfor[:posLookFor] + oneD[1]+ stringGiven[posLookFor+2:]
		signPositif *= oneD[0]

	#print 'stringGiven', stringGiven
	#print signPositif, stringGiven
	if len(stringGiven) == 3:
		#print stringGiven
		if stringGiven == 'ijk' and signPositif == 1:
			return "YES"
		else:
			return "NO"
	
	else:
		#print stringGiven
		return "NO"

	return y




for tc in xrange(1, int(raw_input())+1):
	signPositif = 1
	#print 
	y = ''

	L, X = map(int, raw_input().split())

	stringGiven = raw_input()
	stringGiven = stringGiven * X
	#stringGiven, signPositif, stop = reducestringGiven(stringGiven)
	
	#print 'stringGiven', stringGiven

	y = OneFunction(stringGiven)

	

	#y = oneFunc(stringGiven,'',0, signPositif)

	









	#if y != ''
	print "Case #{}: ".format(tc) + str(y)
	#else:
	#print "Case #{}".format(tc) + stry(y)
		
	

# print 'Y ijk', OneFunction('ijk')
# print 'N ijki', OneFunction('ijki')
# print 'Y ijkiiii', OneFunction('ijkiiii')
# print 'N ijjjjjki', OneFunction('ijjjjjki')
# print 'Y ijjjjjk', OneFunction('ijjjjjk')
# print 'N ij', OneFunction('ij')
# print 'N ikj', OneFunction('ikj')
# print 'N ikkkkj', OneFunction('ikkkkj')






