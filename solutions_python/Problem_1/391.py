f = file("A-small-attempt2.in")
result = file("A-small-attempt2.out", "w")


def search(currentEngine, engines, searches):
	if len(searches) == 0:
		return 0
		
	currentSearch = searches[0]
	searches = searches[1:]
		
	if currentSearch != currentEngine and currentEngine != None:
		return search(currentEngine, engines, searches)
		
	last = -1
	lastEngine = None
	
	for newEngine in engines:
		if newEngine == currentSearch:
			continue
		
		occ = 0
		while occ < len(searches) and searches[occ] != newEngine:
			occ += 1
		
		if occ > last:
			last = occ
			lastEngine = newEngine
			
			
	switches = 0
	if currentEngine != None:
		switches = 1
	print "switch to", lastEngine
	return search(lastEngine, engines, searches) + switches

cases = int(f.readline())
for case in range(cases):
	engineCount = int(f.readline())
	engines = []
	for i in range(engineCount):
		engines.append(f.readline().strip())
	searchCount = int(f.readline())
	searches = []
	for i in range(searchCount):
		searches.append(f.readline().strip())
		
	print engines
	print searches	
		
	switches = search(None, engines, searches)
	print switches
	result.write("Case #" + str(case + 1) + ": " + str(switches) + "\n")
	