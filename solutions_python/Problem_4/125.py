#!/usr/bin/python

import sys


# parsing

lines = [line.strip() for line in open(sys.argv[1]).readlines()]
consumed = 0

def consumeSome(num):
	consumedLines = lines[:num]
	lines[:] = lines[num:]
	return consumedLines

def consumeOneDigit():
	return int(consumeSome(1)[0])

def consumeClause():
	length = consumeOneDigit()
	return (length, consumeSome(length))


# main logic

numCases = consumeOneDigit()

for caseId in range(numCases):
	dim = consumeOneDigit()
	vec1, vec2 = consumeSome(2)
	vec1 = [int(word) for word in vec1.split()]
	vec2 = [int(word) for word in vec2.split()]

	sorts = zip(sorted(vec1), sorted(vec2, reverse=True))

	result = sum(a*b for (a,b) in sorts)
	print 'Case #%i: %i' % (caseId+1, result)

	

"""
	gains = {}
	for i in range(dim):
		for j in range(i,dim):
			gains[(i,j)] = (vec1[i]*vec2[j]+vec1[j]*vec2[i]) - (vec1[i]*vec2[i]+vec1[j]*vec2[j])

	bestGain = sorted(gains.items(), cmp=lambda a,b:cmp(a[1],b[1]))[0]
	toSwap = bestGain[0]
	

	print bestGain
"""
"""

	if numQueries==0:
		print 'Case #%i: 0' % (caseId+1)
	else:
		optimal = [0]*numEngines; optimal[engines.index(queries[0])] = None
		for queryId in range(1,numQueries):
			#print queryId, [x if x!=None else 9 for x in optimal]
			oldBlockerId = optimal.index(None)
			newBlockerId = engines.index(queries[queryId])
			if oldBlockerId!=newBlockerId:
				newOptimal = optimal
				newOptimal[oldBlockerId] = min(optimal[:oldBlockerId]+optimal[oldBlockerId+1:])+1
				newOptimal[newBlockerId] = None
	
"""
	# case1: different engine
	# optimality: 

	# case2: same engine

