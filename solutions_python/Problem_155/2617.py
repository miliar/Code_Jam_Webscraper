import sys
sampleFile = open("input.txt", "r")
outFile = open("output.txt", "w")

r1=lambda:sampleFile.readline()

testCase = map(int, r1().split())

maxLevel = 0
num = 0
friend = 0

for i in range(testCase[0]):
	inString = map(str, r1().split())
	maxLevel = int(inString[0])
	for j in range(maxLevel+1):
		num = num + int(inString[1][j])
		if num < j+1:
			friend+= j+1-num
			num+= j+1-num

	data = "Case #"+str(i+1)+": "+ str(friend)+"\n"
	outFile.write(data)
	friend = 0
	num = 0

sampleFile.close()
outFile.close()