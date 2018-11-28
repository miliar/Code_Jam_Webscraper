
#open file
f = open('./input.in', 'r')

def solve(first, second):
	result = set(first) & set(second)
	if len(result)==0:
		return "Volunteer cheated!"
	if len(result)==1:
		return result.pop()
	if len(result)>1:
		return "Bad magician!"

numcases = int(f.readline())
for casenum in range(1,numcases+1):
	firstRow = []
	secondRow = []
	firstRowNumber = int(f.readline())
	for line in range (1,5):
		if line==firstRowNumber:
			firstRow = f.readline().split()
		else:
			f.readline()

	secondRowNumber = int(f.readline())
	for line in range (1,5):
		if line==secondRowNumber:
			secondRow = f.readline().split()
		else:
			f.readline()

  	print 'Case #' + repr(casenum) + ': ' + solve(firstRow, secondRow)
