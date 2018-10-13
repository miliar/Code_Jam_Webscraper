def solve(case):
	for i in range(len(case)):
		case[i] = case[i].strip()
	
	case = ''.join(case)
	
	X = []
	O = []
	
	for i in range(len(case)):
		if case[i] == 'X':
			X.append(i)
		elif case[i] == 'O':
			O.append(i)
		elif case[i] == 'T':
			X.append(i)
			O.append(i)
			
	winners = [[0,1,2,3],[4,5,6,7],[8,9,10,11],[12,13,14,15],[0,4,8,12],[1,5,9,13],[2,6,10,14],[3,7,11,15],[0,5,10,15],[3,6,9,12]]
	
	winx,wino = False,False
	
	for i in winners:
		if winx == False:
			winx = set(i).issubset(set(X))
		if wino == False:
			wino = set(i).issubset(set(O))
		
	if (winx and wino) or ('.' not in case and not (winx or wino)):
		return 'Draw'
		
	if winx:
		return 'X won'
		
	if wino:
		return 'O won'
		
	return 'Game has not completed'
	
file = open('A-large.in','r')
lines = file.readlines()
file.close()

linesout = []
toout = ''
for i in range(1,len(lines),5):
	toout = solve(lines[i:i+5])
	linesout.append('Case #' + str(len(linesout) + 1) + ': ' + toout + '\n')
	toout = ''

linesout[-1] = linesout[-1][:-1]
file = open('out','w')
file.writelines(linesout)