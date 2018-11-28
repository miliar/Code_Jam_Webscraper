def check(line):
	line = set(line)
	if(line == set(['X','T']) or line == set(['X'])):
		return 'X'
	elif(line == set(['O','T']) or line == set(['O'])):
		return 'O'
	
n = int(raw_input())
for t in range(n):
	table = []
	for i in range(4):
		table.append(raw_input())
	if t != n-1:
		temp = raw_input()
	for i in range(4):
		table.append(table[0][i]+table[1][i] +table[2][i]+table[3][i])
	table.append(table[0][0]+table[1][1] +table[2][2]+table[3][3])
	table.append(table[0][3]+table[1][2] +table[2][1]+table[3][0])
	check_final = 'D'
	check_empty = False
	for i in table:
		turn = check(i)
		if(turn):
			check_final = turn
		if('.' in i):
			check_empty = True
	print 'Case #' + str(t+1) + ':',
	if(check_final == 'X'):
		print 'X won'
	elif(check_final == 'O'):
		print 'O won'
	elif(check_empty):
		print 'Game has not completed'
	elif(check_final == 'D'):
		print 'Draw'
		
	#print table
	
	

		
