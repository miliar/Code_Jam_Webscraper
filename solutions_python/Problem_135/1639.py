import sys

def intersect(a, b):
	return [x for x in a if x in b]
	
def getAnswer(row_a, row_b):
	commoncards =  intersect(row_a, row_b)
	if len(commoncards) == 1:
		return commoncards[0]
	elif len(commoncards) > 1:
		return 'Bad magician!'
	elif len(commoncards) == 0:
		return 'Volunteer cheated!'	

def extractInp(fyle):
	f = open(fyle)
	numCases = int(f.readline())
	for i in range(numCases):
		a = int(f.readline()) # first choice
		rowz = []
		for j in range(4):
			rowz.append([int(x) for x in f.readline().split()])	
		choiceA = rowz[a-1]
		b = 	int(f.readline()) # second choice
		rowz = []
		for j in range(4):
			rowz.append([int(x) for x in f.readline().split()])
		choiceB = rowz[b-1]
		anz = getAnswer(choiceA, choiceB)
		print 'Case #%s: %s' %(i+1, anz)
	


if len(sys.argv) != 2:
	print "Here's the format: <thisfilename.py> <inputstuff>  , Try again."
else:
	phile = sys.argv[1]
	extractInp(phile)




	


	
	
		
