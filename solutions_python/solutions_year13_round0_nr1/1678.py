from sys import argv

#0 = O win, 1 = X win, 2 = no win
def check(x):
	if '.' in x: return 2
	if 'XXXT' in x: return 1
	if 'XXTX' in x: return 1
	if 'XTXX' in x: return 1
	if 'TXXX' in x: return 1
	if 'XXXX' in x: return 1
	if 'OOOT' in x: return 0
	if 'OOTO' in x: return 0
	if 'OTOO' in x: return 0
	if 'TOOO' in x: return 0
	if 'OOOO' in x: return 0

script, rname, wname = argv

infile = open(rname)
outfile = open(wname, 'w')

tc = int(infile.readline())

for i in range(1,tc+1):
	lines = infile.readline().strip()
	lines += infile.readline().strip()
	lines += infile.readline().strip()
	lines += infile.readline().strip()

	#blank line
	infile.readline()

	gameCompleted = False
	winnerFound = False
	winner = "N"

	#check if game completed
	if not '.' in lines:
		gameCompleted = True

	#check horizontal
	for h in [0, 4, 8, 12]:
		status = check(lines[h:h+4])
		if status == 0: 
			winner = "O"
			winnerFound = True
			break
		elif status == 1:
			winner = "X"
			winnerFound = True
			break

	#check diagonals
	if not winnerFound:
		diag1 = lines[0] + lines[5] + lines[10] + lines[15]
		diagcheck1 = check(diag1)
		diag2 = lines[3] + lines[6] + lines[9] + lines[12]
		diagcheck2 = check(diag2)
		if diagcheck1 == 0 or diagcheck2 == 0:
			winner = "O"
			winnerFound = True
		if diagcheck1 == 1 or diagcheck2 == 1:
			winner = "X"
			winnerFound = True

	#check vertical
	if not winnerFound:
		for v in range(0,4):
			checkline = lines[v] + lines[v+4] + lines[v+8] + lines[v+12]
			status = check(checkline)
			if status == 0: 
				winner = "O"
				winnerFound = True
				break
			elif status == 1:
				winner = "X"
				winnerFound = True
				break
	
	if winnerFound:
		if winner == "X":
			print("Case #%d: X won" % i)
			outfile.write("Case #%d: X won\n" % i)
		if winner == "O":
			print("Case #%d: O won" % i)
			outfile.write("Case #%d: O won\n" % i)
	elif gameCompleted:
		print("Case #%d: Draw" % i)
		outfile.write("Case #%d: Draw\n" % i)
	else:
		print("Case #%d: Game has not completed" % i)
		outfile.write("Case #%d: Game has not completed\n" % i)

infile.close()
outfile.close()