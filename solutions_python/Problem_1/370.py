#!/usr/bin/python

#usage:
# ./savingUniv.py > A.out


def getNextEngine (engines, queries):
	maxIndex = 0
	engine = engines[0]
	
	#print engines
	#print queries
	
	for k in range(len(engines)):
		#print k
		found = 0
		for i in range(len(queries)):
			if (engines[k] == queries[i]) and (i > maxIndex):
				#print i
				maxIndex = i
				engine = engines[k]
				#print engine
				found = 1
				break
			elif engines[k] == queries[i]:
				found = 1
				break
		if found == 0:
			engine = engines[k]
			#print 'asdxxx  '+engine
			break
	
	return engine
	
def getNoChanges(engines, queries):
	noChanges = 0
	index = 0
	
	engine = getNextEngine(engines, queries)
	#print engine
	
	while (len(queries) > 0) :
		if engine == queries[0]:
			noChanges = noChanges + 1
			engine = getNextEngine(engines, queries)
			#print engine
		query = queries.pop(0)
		
	return noChanges
	

f = open('A-large.in','r')
noCases = f.readline()
noCases = int(noCases.strip())


for i in range(noCases):
	noEngines = f.readline()
	noEngines = int(noEngines.strip())
	engines = list()
	for e in range(noEngines):
		engine = f.readline()
		engine = engine.strip()
		engines.append(engine)

	#print engines
	
	noQueries = f.readline()
	noQueries = int(noQueries.strip())
	queries = list()
	for q in range(noQueries):
		query = f.readline()
		query = query.strip()
		queries.append(query)
	
	#print queries
	
	if len(queries) > 0:
		noChanges = getNoChanges(engines, queries)
	else:
		noChanges = 0
	
	print 'Case #' + str(i+1) + ': ' + str(noChanges)
	

f.close()