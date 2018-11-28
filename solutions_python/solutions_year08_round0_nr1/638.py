import re
import os

debug = False # debug condition
geninput = False
fname = "A-small-attempt10.in"
#fname = "codejam1_case_7"
#fname = "A-large.in"

def findUnusedEngine(engines, queries):
	return [e for e in engines if queries.count(e) == 0]

def findBestEngineByCounter(engines, queries):
	engine = engines[0]
	
	freeEngines = findUnusedEngine(engines, queries)
	if freeEngines:
		engine = freeEngines[0]
	else:
		try:
			bestOccur = queries.count(engine)
		except ValueError:
			return engine
		for q in engines:
			try:
				c = queries.index(q)
				if c <= bestOccur:
					c = bestOccur
					engine = q
			except ValueError:
				return q

	if debug:
		print "best engine: " + engine
	return engine

def findBestEngine(engines, queries):
	freeEngines = findUnusedEngine(engines, queries)
	if freeEngines:
		engine = freeEngines[0]
	else:
		bestOccur = 0
		for q in engines:
			try:
				c = queries.index(q)
				if c >= bestOccur:
					bestOccur = c
					if debug:
						print "> " + q + ": " + str(bestOccur)
					engine = q
			except ValueError, e:
				raise e
				#return q

	if debug:
		print "best engine: " + engine
	return engine

def doProcess(engines, queries, engineOptimizer, debug):
	sw = 0
	#best = findBestEngine(engines, queries)
	best = engineOptimizer(engines, queries)
	#queries = set(queries)	
	for i, query in enumerate(queries):
		if debug:
			print query, " <-> ", best
		if query == best:
			if debug:
				print query, " == ", best
			sw += 1
			#best = findBestEngine(engines, queries[i + 1:])
			best = engineOptimizer(engines, queries[i:])
			if debug:
				print query, " -> ", best
	return sw

f = open(fname)
line = f.readline().strip()
caseNo = int(line) # number of cases
lineNo = 1

for i in range(caseNo):
	if geninput:
		fw = open("codejam1_case_" + str(i + 1), "w")
		fw.write("1\n")
	#debug = i == 12
	if debug:
		print "line=" + str(lineNo)
	engines = []
	queries = []
	line = f.readline().strip()
	if geninput:
		fw.write(line + "\n")
	engineNo = int(line) # number of engines
	for j in range(int(engineNo)):
		line = f.readline().strip()
		engines.append(line)
		if geninput:
			fw.write(line + "\n")

	queriesNo = int(f.readline().strip()) # number of quries
	if geninput:
		fw.write(str(queriesNo) + "\n")

	for j in range(int(queriesNo)):
		line = f.readline().strip()
		queries.append(line)
		if geninput:
			fw.write(line + "\n")

	lineNo = lineNo + engineNo + queriesNo + 2
	answer = doProcess(engines[:], queries[:], findBestEngine, debug)
	#answer = min(doProcess(engines[:], queries[:], findBestEngine, debug), doProcess(engines[:], queries[:], findBestEngineByCounter, debug))
	print "Case #%d: %d" % (i + 1, answer)
