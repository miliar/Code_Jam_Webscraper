import sys;
import pprint;

def CheckRow(rowNum, lawn, val):
	for sqare in lawn[rowNum]:
		if(sqare > val):
			return False
	return True

def CheckCol(colNum, lawn, dimensions, val):
	for row in range(dimensions[0]):
		if(lawn[row][colNum] > val):
			return False
	return True
	
def solveLawn(ld, lh):
	if(1 in ld):
		return "YES"
	
	for row in range(ld[0]):
		for col in range(ld[1]):
			if(not(CheckRow(row, lh, lh[row][col])) and not(CheckCol(col, lh, ld, lh[row][col]))):
				return "NO"
	
	return "YES"
				

numberOfCases = int(sys.stdin.readline())
for caseNumber in range(1, numberOfCases + 1):
	result=""
	ld = [int(i) for i in sys.stdin.readline().split()]
	lh = [[int(s) for s in sys.stdin.readline().split()] for i in range(ld[0])]
	result = solveLawn(ld, lh)
	sys.stdout.write("Case #" + str(caseNumber) + ": " + result)
	if(caseNumber != numberOfCases):
		sys.stdout.write("\n")
		