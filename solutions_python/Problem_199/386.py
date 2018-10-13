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
	args = line.split(' ')
	state = args[0]
	psize = int(args[1])
	loop_size = len(state) - psize + 1
	count = 0
	for i in range(loop_size):
		if state[i] == '+':
			continue
		count += 1
		new_sub = ''
		for k in range(psize):
			new_sub += '-' if state[i + k] == '+' else '+'
		state = state[:i] + new_sub + state[i + psize:]
	for i in range(len(state)):
		if state[i] == '-':
			return 'IMPOSSIBLE'
	return count

lines = readLines('input.txt')
total = int(lines[0])
output = []
for i in range(1, total+1):
	value = solveProblem(lines[i])
	line = 'Case #{0}: {1}'.format(i, value)
	output.append(line)
writeLines(output)
