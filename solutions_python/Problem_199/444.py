def opp(char):
	if char == '+':
		return '-'
	if char == '-':
		return '+'
		
def flipstart(pancakes,k):
	temppancakes = pancakes[:]
	for i in range(k):
		temppancakes[i] = opp(temppancakes[i])
	return temppancakes

def f(pancakes,k):
	count = 0
	while True:
		if '-' not in pancakes:
			return count
		if len(pancakes) < k:
			return 'IMPOSSIBLE'
		if pancakes[0] == '+':
			pancakes = pancakes[1:]
		else:
			count += 1
			pancakes = flipstart(pancakes,k)

import sys
with open(sys.argv[1], "r") as fileIN:
	inputLines = fileIN.readlines()
		
with open(sys.argv[2], "w") as fileOUT:
	numberOfCases = int(inputLines.pop(0))
	for num in range(numberOfCases):
		line = inputLines.pop(0).rstrip().split()
		pancakes = list(line[0])
		k = int(line[1])
		fileOUT.write('Case #' + str(num+1) + ': ' + str(f(pancakes,k)) + '\n')