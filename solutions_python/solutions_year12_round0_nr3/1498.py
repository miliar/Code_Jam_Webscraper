import sys
from collections import Counter

inputFile = open(sys.argv[1])
outputFile = open("output.txt", "w")

caseNums = int(inputFile.readline())

def rearrange(n, m):
	for x in range(len(n)-1):
		test = n[x+1:] + n[:x+1]
		if test == m:
			return True

for case in range(caseNums):
	outputFile.write("Case #%d: "%(case+1))
	nums = inputFile.readline().split()
	num1, num2 = int(nums[0]), int(nums[1])

	total = 0
	for n in range(num1,num2):
		for m in range(n+1,num2+1):
			if rearrange(str(n), str(m)):	
				total += 1

	outputFile.write("%d\n"%total)

inputFile.close()
outputFile.close()
			

