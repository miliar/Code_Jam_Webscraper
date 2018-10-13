searchEngines = dict()
searchEngineSwitches = 0
numSearchEngines = 0

def openfile():
    input = open("C:\\A-large.in", "r")
    output = open("C:\\outputAlarge.txt", "w")
    tests = int(input.readline().strip())
    global searchEngines
    global searchEngineSwitches
    global numSearchEngines
    searchEngines.clear()
    for i in xrange(tests):    	
    	searchEngines.clear()
    	searchEngineSwitches = 0
    	numSearchEngines = 0
    	readTestCase(input, output)
    	processTestCase(input, output)
        output.write("Case #" + str(i + 1) + ": " + str(searchEngineSwitches))
        if (i + 1) < tests:
            output.write("\n")                
    input.close()
    output.close()
    
def readTestCase(input, output):
	global numSearchEngines	
	numSearchEngines = int(input.readline().strip())
	for i in xrange(numSearchEngines):		
		searchEngine = input.readline()

def processTestCase(input, output):
	numQueries = int(input.readline().strip())	
	global searchEngines
	global searchEngineSwitches
	global numSearchEngines
	for i in xrange(numQueries):
		searchEngine = input.readline().strip()
		if((len(searchEngines) == (numSearchEngines - 1)) and (searchEngine not in searchEngines)):			
			searchEngines.clear()
			searchEngines[searchEngine] = 1
			searchEngineSwitches += 1			
		else:
			searchEngines[searchEngine] = 1	

openfile()
