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

state = []

def solveProblem(lines, index, count):
	global state
	args = lines[index].split(' ')
	R = int(args[0])
	C = int(args[1])

	state = []
	block = []
	for i in range(R):
		state.append([' '] * C)
	for i in range(R):
		args = lines[index + 1 + i]
		for j in range(len(args)):
			state[i][j] = args[j]
	for i in range(R):
		line = state[i]
		pos = None
		m = None
		for j in range(len(line)):
			if line[j] != '?':
				if m is None and pos is not None:
					for k in range(pos, j):
						line[k] = line[j]
				m = line[j]
			elif m is not None:
				line[j] = m
			elif m is None and pos is None:
				pos = j

	for i in range(R):
		line = state[i]
		if line[0] == '?':
			pos = None
			for k in range(i, R):
				if state[k][0] != '?':
					pos = k
					break
			if pos is None:
				pos = i - 1
			for k in range(C):
				state[i][k] = state[pos][k]

	results = []
	results.append('Case #{0}:'.format(count))
	for i in range(R):
		results.append(''.join(state[i]))
	return results, index + R + 1

lines = readLines('input.txt')
total = int(lines[0])
output = []
cur_index = 1
count = 1
while count <= total:
	outputs, next_index = solveProblem(lines, cur_index, count)
	output.extend(outputs)
	cur_index = next_index
	count += 1
writeLines(output)
