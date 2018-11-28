import sys
import operator

def line_winner(z):
	for l in range(0, 4):
		if (reduce(operator.and_, z[l], True)):
			return True
			
	return False

out_file = open('output.out', 'w+')
in_file = open('A-large.in.txt', 'r+')
num_cases = int(in_file.readline())

for c in range(1, num_cases+1):
	x = []
	o = []
	notcompleted = False

	for l in range(0, 4):
		line = in_file.readline().strip('\n')
		xcol = []
		ocol = []
	
		for co in range(0, 4):
			if line[co] == 'X':
				xcol.append(True)
				ocol.append(False)
			elif line[co] == 'O':
				ocol.append(True)
				xcol.append(False)
			elif line[co] == 'T':
				ocol.append(True)
				xcol.append(True)
			else:
				ocol.append(False)
				xcol.append(False)
				notcompleted = True
		
		x.append(xcol)
		o.append(ocol)
	
	xdiagonal1 = True
	odiagonal1 = True
	
	xdiagonal2 = True
	odiagonal2 = True
	
	lindex = 3
	cindex = 0
	
	for f in range(0, 4):
		xdiagonal1 = x[lindex][cindex] and xdiagonal1
		odiagonal1 = o[lindex][cindex] and odiagonal1
		
		lindex -= 1
		cindex += 1
	
	for t in range(0, 4):
		xdiagonal2 = x[t][t] and xdiagonal2
		odiagonal2 = o[t][t] and odiagonal2
	
	if (xdiagonal1 or xdiagonal2 or line_winner(x) or line_winner(zip(*x))):
		case = 'Case #'+str(c)+': X won'
		out_file.write(case+'\n')		
	elif (odiagonal1 or odiagonal2 or line_winner(o) or line_winner(zip(*o))):
		case = 'Case #'+str(c)+': O won'
		out_file.write(case+'\n')
	elif (notcompleted):
		case = 'Case #'+str(c)+': Game has not completed'
		out_file.write(case+'\n')
	else:
		case = 'Case #'+str(c)+': Draw'
		out_file.write(case+'\n')
	
	line = in_file.readline().strip('\n')
    
    
    