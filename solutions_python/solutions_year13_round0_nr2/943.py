import sys

def main(filename):
	result = ''
	file = open(filename)
	numberOfTests = int(file.readline())
	for i in range(numberOfTests):
		nm = [int(num) for num in file.readline().split()]
		n = nm[0]
		m = nm[1]
		lawn = []
		for rows in range(n):
			lawn.append([int(num) for num in file.readline().split()])
		result += 'Case #%d: %s\n' % (i+1,solveLawnMower(lawn))
	file.close()
	return result
	
def solveLawnMower(lawn):
	result = [[100]*len(lawn[0])]*len(lawn)
	numbers = [cell for rows in lawn for cell in rows]
	uniqueNumbers = sorted(list(set(numbers)), reverse=True)
	for num in uniqueNumbers:
		mowRows(num, result, lawn)
		mowColumns(num, result, lawn)
	if result == lawn:
		return 'YES'
	else:
		return 'NO'

def mowRows(num, result, lawn):
	for rowIndex in range(len(lawn)):
		hasNum = False
		isLargest = True
		for cell in lawn[rowIndex]:
			if cell == num:
				hasNum = True
			if cell > num:
				isLargest = False
		if hasNum and isLargest:
			result[rowIndex] = [num] * len(lawn[0])
	
def mowColumns(num, result, lawn):
	for columnIndex in range(len(lawn[0])):
		hasNum = False
		isLargest = True
		for rowIndex in range(len(lawn)):
			cell = lawn[rowIndex][columnIndex]
			if cell == num:
				hasNum = True
			if cell > num:
				isLargest = False
		if hasNum and isLargest:
			for rowIndex in range(len(lawn)):
				result[rowIndex][columnIndex] = num
		
if __name__ == '__main__':
	if len(sys.argv) < 3:
		print 'Not enough files specified'
		sys.exit(1)
	inputfilename = sys.argv[1]
	outputfilename = sys.argv[2]
	result = main(inputfilename)
	outputfile = open(outputfilename, 'w')
	outputfile.write(result)
	outputfile.close()
	print result