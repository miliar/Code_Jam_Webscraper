def rowcheck(line):
	prevItem = line[0]
	result = []
	h = max(line)
	for x in range(0,len(line)):
		if line[x] !=h:
			result.append(x)
	return result
	
def colcheck(line):
	prevItem = line[0]
	for item in line[1:]:
		if prevItem != item:
			return False
		prevItem = item
	return True

	
input = open('c:\\users\\snuff\\desktop\\codeJam\\B-small-attempt0.in','r+')
output = open('c:\\users\\snuff\\desktop\\codeJam\\b-small.out','w+')

n = int(input.readline())
count = 0
while n>0:
	possible = "YES"
	count += 1
	n-=1
	a,b = map(int, input.readline().split())
	matrix = []
	for x in range(a):
		rawline = input.readline().replace("\n","")
		line = [int(i) for i in rawline.split()]
		matrix.append(line)
	colsToCheck = []
	for i in range(a):
		toCheck = matrix[i]
		colsToCheck += (rowcheck(toCheck))
	colsToCheck = list(set(colsToCheck))
	for colnum in colsToCheck:
		col = []
		for row in matrix:
			col.append(row[colnum])
		if(colcheck(col) == False):
			possible = "NO"
			break
	print("Case #%i: %s"%(count, possible),file=output)		
	
		
	
	


	
	
	