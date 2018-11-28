# Function which finds the best search engine choice, based on how far it can get from the starting position without running into that engine's name
def findBestChoice(engineList, remainingQuerys):
	for query in remainingQuerys:
		#print "test", query, len(engineList), engineList.count(query)
		if (len(engineList) == 1):
			return engineList.pop()
		
		if (engineList.count(query)): # If it's in the list
			#print "test"
			engineList.remove(query)
	
	#print engineList
	return engineList.pop()
	

# Main Method Starts Here
in_file = open("A-large.in", "r")
out_file = open("output.txt", "w")

num_cases = int(in_file.readline()) # First line's the number of cases
caseNum = 1

for i in range(num_cases):
	tests = ""
	engines = ""
	numSwitches = 0
	
	#print "Stating Case"
	num_engines = int(in_file.readline()) # Second line's the number of engines
	
	for i in range(num_engines):
		engines += in_file.readline() # N lines after that are all the engines
	
	enginList = engines.strip().split('\n') # Remove spaces, then split the string into a list, seperating wherever there's a newline
	
	#print engines, enginList, num_engines
	
	num_tests = int(in_file.readline()) # The next line is the number of tests
	
	#print num_tests
	
	for i in range(num_tests):
		tests += in_file.readline() # S lines after that are the tests
	
	testList = tests.strip().split('\n') # Same as the enginList, but with the tests this time. Thankfully lists keep the order, unlike dicts
	
	curEngine = findBestChoice(list(enginList), testList) # Make an initial choice
	
	#print curEngine

	for i in range(len(testList)):
		#print testList[i], curEngine#, enginList
		if (testList[i] == curEngine): # Then we have to make a switch
			numSwitches += 1
			curEngine = findBestChoice(list(enginList), testList[i:])
			
	print numSwitches
	
	out_file.write("Case #" + str(caseNum) + ": " + str(numSwitches) + "\n")
	caseNum += 1

in_file.close()
out_file.close()