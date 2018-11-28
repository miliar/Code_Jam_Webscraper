def solve(case):
	for i in range(len(case)):
		case[i] = case[i].split(' ')
	
	irows = []
	icols = []
	
	rows = case
	cols = [[case[i][j] for i in range(len(case))] for j in range(len(case[0]))]
	
	for i in range(len(case)):
		for j in range(len(case[i])):
			if case[i][j] != max(cols[j]) and case[i][j] != max(rows[i]):
				return 'NO'
	return 'YES'
	
file = open('B-small-attempt2.in','r')
lines = file.readlines()
for i in range(len(lines)):
	lines[i] = lines[i].strip()
file.close()

linesout = []
toout = ''
line = 1
while line < len(lines):
	rows = int(lines[line].split(' ')[0])
	toout = solve(lines[line+1:line+1+rows])
	linesout.append('Case #' + str(len(linesout) + 1) + ': ' + toout + '\n')
	toout = ''
	line = line+1+rows

linesout[-1] = linesout[-1][:-1]
file = open('out','w')
file.writelines(linesout)