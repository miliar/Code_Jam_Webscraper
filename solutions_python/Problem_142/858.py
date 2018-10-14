
#!/usr/bin/python

import math

try:
	with open("A-small-attempt0.in") as inFile, open("output.txt", "w") as outFile:
		cases = int(inFile.readline().strip())
		for c in range(cases):
			outFile.write("Case #" + str(c+1) + ": ")
			strings = int(inFile.readline().strip())
			stringCompare = []
			for each in range(strings):
				thisRow = list(inFile.readline().strip())
				last = ""
				for letter in range(len(thisRow)):
					if letter == 0:
						stringCompare.append([[thisRow[letter], 1]])
					elif thisRow[letter] == stringCompare[each][len(stringCompare[each])-1][0]:
						stringCompare[each][len(stringCompare[each])-1][1] = stringCompare[each][len(stringCompare[each])-1][1] + 1
					else:
						stringCompare[each].append([thisRow[letter], 1])
			#possible
			firstPattern = ""
			for row in range(len(stringCompare[0])):
				firstPattern = firstPattern + stringCompare[0][row][0]
			newarr= []
			for each in list(firstPattern):
				newarr.append([each, 1])
			longway = 0

			possible = True
			for each in stringCompare:
				thisPattern = ""
				for column in each:
					thisPattern = thisPattern + column[0]
				if thisPattern != firstPattern:
					possible = False
			if possible == False:
				outFile.write("Fegla Won\n")
			#number of changes
			else:
				for remain in range(len(stringCompare)):
					for letter in range(len(stringCompare[remain])):
						longway = longway + int(math.fabs(newarr[letter][1]-stringCompare[remain][letter][1]))
				for each in range(len(stringCompare)):
					counter = int(0)
					for remain in range(len(stringCompare)):
						if remain != each:
							for letter in range(len(stringCompare[each])):
								counter = counter + int(math.fabs(stringCompare[each][letter][1]-stringCompare[remain][letter][1]))
					if counter < longway:
						longway = counter
				outFile.write(str(int(longway)) + "\n")
							
except IOError as err:
	print(str(err))
