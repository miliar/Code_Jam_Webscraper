#!/usr/bin/python3

def readInputFile():
	l = [line.rstrip('\n') for line in open('in.in')]
	return l

def putOutputFile(testCaseResults):
	f = open('out.out', 'w')
	i = 1
	for row in testCaseResults:
 		f.write('Case #' + str(i) + ': ' + row + '\n')
 		i += 1




def splits(num):
	""" :: [[]] 
	eg. 6 → [[1,5], [2,4], [3,3]] """
	r = list()
	for i in range(1, num//2+1):
		r.append([i, num-i])
	return r


def minute3(pans, mins):
	""" pans := number of pancakes on the plates of D diners :: Int-List
		mins := number of minutes already passed
	"""

	if len(pans) == 0:
		return mins

	if sum(pans) == 0:
		return mins

	if max(pans) == 1:
		return mins+1;

	# remove zeros
	pans = list(filter(lambda x: x != 0, pans))

	pans.sort(reverse=True)

	
	# hash table lookup
	if str(pans) in hashtable:
		return hashtable[str(pans)]+mins


	strategies = list()

	# Strategy 1
	pans3 = list(pans)
	strategyEating = minute3([p-1 for p in pans3 if p >= 1], 0)
	strategies.append(strategyEating)

	# Strategy 2
	for s in splits(pans[0]):
		pans2 = list(pans[1::])
		strategies.append(minute3(pans2 + s, 0)) # add splitted to strategies
		

	#save current pans min(minutes)
	mymin = min(strategies)
	hashtable[str(pans)] = mymin+1

	return mymin+1+mins


lines = readInputFile()[2::2]

testCaseResults = list()
hashtable = dict()

for l in lines:
	l = list(map(int, l.split()))
	testCaseResults.append(str(minute3(l, 0)))

putOutputFile(testCaseResults)