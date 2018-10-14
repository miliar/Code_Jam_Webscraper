import sys
import math
file = sys.argv[1]

lines = open(file).readlines()
T = int(lines[0])

currentLine = 1

for case in range(T):
	N = int(lines[currentLine])
	currentLine = currentLine + 1
	strings = []
	for i in range(N):
		strings.append( lines[currentLine])
		currentLine = currentLine + 1

	split = []
	for string in strings:
		arrayFormat = []
		for letter in string:
			if len(arrayFormat) > 0 and arrayFormat[-1][0] == letter:
				arrayFormat[-1] += letter
			else:
				arrayFormat.append(letter)
		
		split.append(arrayFormat)
	
	length = len(split[1])
	for array in split:
		if len(array) != length:
			print "Case #{}: Fegla Won".format(case + 1 )
			break;
	else:
		for i in range(length):
			superbreak = 0
			letter = split[0][i][0]
			for array in split:
				if array[i][0] != letter:
					print "Case #{}: Fegla Won".format(case + 1 )
					superbreak = 1
					break;
			if superbreak:
				break
		else:
			moves = 0
			for i in range(length):
				array[0][0]
				count = 0
				totalLength = 0
				for array in split:
					count +=1
					totalLength += len(array[i])
				average = int(round(float(totalLength) / float(count)))

				for array in split:
					moves += int(math.fabs(len(array[i]) - average))
			else:	
				print "Case #{}: {}".format(case + 1 ,moves )