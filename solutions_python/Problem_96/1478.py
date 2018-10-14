
def calcAlgo(scores, surpNum, p):
	count = 0
	for score in scores:
		if score == 0 and p != 0:
			continue
		elif score >= 3 * p - 2:
			count += 1
		elif score >= 3 * p - 4 and surpNum > 0:
			count += 1
			surpNum -= 1

	return count

def main():
	import sys
	infilename = sys.argv[1]
	with open(infilename, 'r') as infile, open('output', 'w') as outfile:
		firstLine = infile.readline()
		testCasesNum = int(firstLine)
		outlines = []
	 	for i in range(testCasesNum):
			inpLine = infile.readline().strip()			 
			lineParams = inpLine.split()
			surpNum = int(lineParams[1])
			p = int(lineParams[2])
			scores = [int(x) for x in lineParams[3:]]
			scores.sort()
			scores.reverse()
			result = calcAlgo(scores, surpNum, p)
			outlines.append('Case #' + str(i+1) + ': ' + str(result) + '\n')
		outfile.writelines(outlines)

if __name__ == "__main__":
	main()
