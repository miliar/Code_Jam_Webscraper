import os


def readLines(filename):
	input = open(filename, 'rb')
	lines = []
	for line in input:
		line = line.replace('\n','')
		lines.append(line)	
	input.close()
	return lines

def writeLines(output):
	outputFile = open('output.txt', 'w')
	for line in output:
		outputFile.write(line + '\n')
	outputFile.close()

def solveProblem(line):
	numbers = []
	for ch in line:
		numbers.append(int(ch))
	nsize = len(numbers)
	for i in range(nsize):
		if i + 1 < nsize and numbers[i] > numbers[i + 1]:
			index = i
			while index >= 1 and numbers[index - 1] >= numbers[index]:
				index -= 1
			numbers[index] -= 1
			for k in range(index + 1, nsize):
				numbers[k] = 9
			break
	result = ''
	index = 0
	while index < nsize and numbers[index] == 0:
		index += 1
	for i in range(index, nsize):
		result += str(numbers[i])
	return result


lines = readLines('input.txt')
total = int(lines[0])
output = []
for i in range(1, total+1):
	value = solveProblem(lines[i])
	line = 'Case #{0}: {1}'.format(i, value)
	output.append(line)
writeLines(output)
