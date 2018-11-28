def anyone_won(line):
	if (line[0] == 'X' and line[1] == 'X' and line[2] == 'X' and line[3] == 'X') or \
		(line[0] == 'T' and line[1] == 'X' and line[2] == 'X' and line[3] == 'X') or \
		(line[0] == 'X' and line[1] == 'T' and line[2] == 'X' and line[3] == 'X') or \
		(line[0] == 'X' and line[1] == 'X' and line[2] == 'T' and line[3] == 'X') or \
		(line[0] == 'X' and line[1] == 'X' and line[2] == 'X' and line[3] == 'T'):
		return 'X'
	if (line[0] == 'O' and line[1] == 'O' and line[2] == 'O' and line[3] == 'O') or \
		(line[0] == 'T' and line[1] == 'O' and line[2] == 'O' and line[3] == 'O') or \
		(line[0] == 'O' and line[1] == 'T' and line[2] == 'O' and line[3] == 'O') or \
		(line[0] == 'O' and line[1] == 'O' and line[2] == 'T' and line[3] == 'O') or \
		(line[0] == 'O' and line[1] == 'O' and line[2] == 'O' and line[3] == 'T'):
		return 'O'
	return None

f = open('/Users/lhespanha/Documents/projects/personal/gcj2013/problemA.in','r')

cases = int(f.readline())
n = 0
while (n < cases):
	tab = []
	contains_dot = False
	won = False
	for i in range(4):
		line = f.readline()
		if "." in line:
			contains_dot = True			
		tab.append(line)
	for i in range(4):
		line_result = anyone_won(tab[i])
		if line_result:
			print "Case #%s: %s won" % (str(n+1), line_result)
			won = True
			break
		else:
			col_result = anyone_won(''.join([tab[0][i], tab[1][i], tab[2][i], tab[3][i]]))
			if col_result:
				print "Case #%s: %s won" % (str(n+1), col_result)
				won = True
				break
	if not won:
		diag1_result = anyone_won(''.join([tab[0][0], tab[1][1], tab[2][2], tab[3][3]]))
		if diag1_result:
			print "Case #%s: %s won" % (str(n+1), diag1_result)
			won = True
	if not won:
		diag2_result = anyone_won(''.join([tab[0][3], tab[1][2], tab[2][1], tab[3][0]]))
		if diag2_result:
			print "Case #%s: %s won" % (str(n+1), diag2_result)
			won = True
	if not won:
		if contains_dot:
			print "Case #%s: Game has not completed" % (str(n+1))
		else:
			print "Case #%s: Draw" % (str(n+1))
	f.readline()
	n = n + 1



