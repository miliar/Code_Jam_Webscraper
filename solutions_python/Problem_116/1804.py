import math

result = ''
processfurther = True
oppplayer = {'X':'O','O':'X'}
outfile = open("OutputSmall.txt", "w")

def checkwin(lst, player):
	global processfurther
	global oppplayer
	global result
	if processfurther:
		if not('.' in lst) and not( oppplayer[player] in lst):
			result = player + ' won'
			processfurther = False


def checkpattern(arrlst, cnt):
	lst  = arrlst[cnt*4:cnt*4 + 4]
	checkwin(lst, 'X')   #X win check
	checkwin(lst, 'O')   #O win check
	

with open("InputSmall.txt") as f:
	content = f.readlines()

totalcases = int(content[0])


for i in range(0,totalcases):
	result = ''
	processfurther = True
	if 0 == i:
		j = 0
	else:
		j = i*4 + i*1

	#rows construction
	rows = []
	for k in range(1,5):
		rows.extend(list(content[j + k][0:4]))

	#row check
	for l in range(0,4):
		if processfurther:
			checkpattern(rows, l)
	#column construction
	cols = []
	if processfurther:
		for m in range(0,16):
			cols.append(rows[m + (m%4  - (m/4))*3])

	#column check
	for n in range(0,4):
		if processfurther:
			checkpattern(cols, n)
	#diagonal check
	diagonals = []
	if processfurther:
		for o in range(0,4):
			diagonals.append(rows[o*5])
		for o in range(1,5):
			diagonals.append(rows[o*3])
	
	for p in range(0,2):
		if processfurther:
			checkpattern(diagonals, p)
	
	if processfurther:
		if '.' in rows:
			result  = 'Game has not completed'
		else:
			result  = 'Draw'

	
	outfile.write('Case #' + str(i + 1) + ': ' + result + '\n')
		

