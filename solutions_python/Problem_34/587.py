#Read input file
import sys
from searchword import searchword

def main(fileName):
	setting, known, testData = fileOpen(fileName)
	i = 0
	for t in testData:
		i += 1
		count = searchword(known,t)
		print "Case #%d: %d" % (i,count)

def fileOpen(fileName):
	f = open(fileName)
	i = 0
	setting = {}
	known = []
	testData = []
	for line in f:
		if i == 0:
			#parse first line
			setting = parseFirstLine(line[:-1])
		elif i < int(setting["D"]+1):
			#known alien language
			known.append(line[:-1])
		elif i < int(setting["N"])+int(setting["D"]+1):
			testData.append(line[:-1])
		i += 1
	return setting, known, testData

def parseFirstLine(str):
	"""
		>>> parseFirstLine("3 5 4")
		{'N': 4, 'L': 3, 'D': 5}
	"""
	result={}
	(result["L"],result["D"],result["N"]) = str.split()
	for i in result.keys():
		result[i] = int(result[i])
	return result 

if __name__ == "__main__":
	if len(sys.argv) > 1:
		main(sys.argv[1])
	else:
		import doctest
		doctest.testmod(verbose=True)
		#"usage: exefile inputfile"
