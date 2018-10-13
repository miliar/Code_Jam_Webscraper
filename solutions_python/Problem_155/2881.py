import fileinput
import sys


limit = 0
count = 0
caseNum = 1
sMax = 0
for line in fileinput.input(sys.argv[1:]):
	
	line = line[:len(line)-1]
	arr = line.split()


	if count == 0:
		count += 1
		limit = int(line)
		# print("limit " + str(limit))
		continue

	sMax = int(arr[0])

	i = 0
	firstCountNum = 0
	soln = 0
	if sMax == 0:
		print("Case #" + str(caseNum) + ": " + str(soln))
		caseNum += 1
		continue

	while i <= sMax:
		
		# print(str(firstCountNum) + " " + str(i))
		if firstCountNum < i:
			soln += i - firstCountNum 
			firstCountNum += i - firstCountNum
		firstCountNum += int(arr[1][i])
		i+= 1

	print("Case #" + str(caseNum) + ": " + str(soln))
	caseNum += 1


	