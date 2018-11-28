#! python3

from os import system

import sys
sys.stdout = open("A-small-attempt0-output.txt", "w")

f = open("A-small-attempt0.in", "r")
input = f.read().strip()
input = input.split('\n')

firstRow = []
secondRow = []
firstArrangement = []
secondArrangement = []
caseNb = 1
firstRowId = 1
secondRowId = 6

while caseNb <= int(input[0]):
	firstRow.append(input[firstRowId])
	secondRow.append(input[secondRowId])
	firstArrangement.append(input[firstRowId + int(input[firstRowId])])
	secondArrangement.append(input[secondRowId + int(input[secondRowId])])
	caseNb += 1
	firstRowId += 10
	secondRowId += 10
	
for caseKey, case in enumerate(firstRow):
	intersection = list(set(firstArrangement[caseKey].split()) & set(secondArrangement[caseKey].split()))
	intersectionLen = len(intersection)
	if intersectionLen == 1:
		print("Case #" + str(caseKey + 1) + ": " + intersection[0])
	elif intersectionLen > 1:
		print("Case #" + str(caseKey + 1) + ": Bad magician!")
	else:
		print("Case #" + str(caseKey + 1) + ": Volunteer cheated!")
		
system("pause")
