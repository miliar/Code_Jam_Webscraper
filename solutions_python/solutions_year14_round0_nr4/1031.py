from multiprocessing import *
import bisect

Cs = 2.0

def evaluateResults(testCaseNumber):
	naomi = dataset[testCaseNumber][1].split()
	ken = dataset[testCaseNumber][2].split()
	naomi.sort()
	ken.sort()
	naomiFair = list(naomi)
	kenFair = list(ken)
	scoreFair = 0
	score = 0
	for i in range(int(dataset[testCaseNumber][0])-1, -1, -1):
		if ( naomiFair[i] > kenFair[i]):
			scoreFair += 1
			del naomiFair[i]
			del kenFair[0]
		else:
			del naomiFair[i]
			del kenFair[i]
	for i in range(int(dataset[testCaseNumber][0])-1, -1, -1):
		if ( ken[i] > naomi[i]):
			del ken[i]
			del naomi[0]
		else:
			score += 1
			del naomi[bisect.bisect(naomi, ken[i])]
			del ken[i]
			
	print "Case #" + str(testCaseNumber+1) + ": ", score, scoreFair
	return testCaseNumber, "Case #" + str(testCaseNumber+1) + ": " + str(score) + " " + str(scoreFair)
		
#Initialise the execution of x parallel threads so to run the test for different values of k concurrently
def initialiseSystem(tests):
	po = Pool(processes=(cpu_count()-1 if cpu_count() > 2 else 2))
	res = po.map_async(evaluateResults,((k) for k in tests))
	results = res.get()
	
	return list(results)
	
def cookieClicker():
	global dataset
	dataset = loadFile('D-large.in')
	dataset = dataset.splitlines()
	testCases = int(dataset[0])
	dataset = list(chunks(dataset[1:], 3))
	results = initialiseSystem(range(0,testCases))
	results.sort()
	file = open("D-large.out", "w")
	for x,y in results:
		file.write(y + "\n")
	pass
	file.close()
	
def loadFile(filePath):
	file = open(filePath)
	fileData = file.read()
	file.close()
	return fileData

	pass	
	
def chunks(l, n):
	for i in xrange(0, len(l), n):
		yield l[i:i+n]
	
	pass
	
if __name__ == "__main__":
	cookieClicker()