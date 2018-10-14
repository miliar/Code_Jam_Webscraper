
T = int(raw_input())
a = []
for i in range(T):
	a = [raw_input() for x in range(4)]
	#print a
	empty = False
	won = False
	print "Case #" + str(i+1) + ": ",
	for j in range(4):
		if a[j].replace('T','X') == 'XXXX':
			print "X won"
			won = True
			break
		elif a[j].replace('T','O') == 'OOOO':
			print "O won"
			won = True
			break
		else : 
			col = a[0][j] + a[1][j] + a [2][j] + a[3][j]
			if col.replace('T','X') == 'XXXX':
				print "X won"
				won = True
				break
			elif col.replace('T','O') == 'OOOO':
				print "O won"
				won = True
				break
		col = a[0][0] + a[1][1] + a[2][2] + a[3][3]
		if col.replace('T','X') == 'XXXX':
			print "X won"
			won = True
			break
		elif col.replace('T','O') == 'OOOO':
			print "O won"
			won = True
			break		
		col = a[0][3] + a[1][2] + a[2][1] + a[3][0]
		if col.replace('T','X') == 'XXXX':
			print "X won"
			won = True
			break
		elif col.replace('T','O') == 'OOOO':
			print "O won"
			won = True
			break		
				
		if a[j].find('.') != -1:
			empty = True
	
	#print "W " + str(won) + " " + str(empty)
	if not won:
		if not empty:
			print "Draw"
		else:
			print "Game has not completed"
	a = raw_input()
