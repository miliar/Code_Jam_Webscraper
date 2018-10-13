x_win = {
		"XXXX":"",
		"TXXX":"",
		"XTXX":"",
		"XXTX":"",
		"XXXT":""}
o_win = {
		"OOOO":"",
		"TOOO":"",
		"OTOO":"",
		"OOTO":"",
		"OOOT":""
		}

status = ["Draw","Game has not completed","X won","O won"]

infile = open("A-large.in",'r')
outfile = open("tictac.out",'w')
case_num = int(infile.readline().strip())

for i in range(0,case_num):
	lines = [infile.readline().strip() for j in range(0,4)]
	rows = ["".join([lines[j][k] for j in range(0,4)]) for k in range(0,4)]
	diag1 = "".join([lines[j][j] for j in range(0,4)])
	diag2 = "".join([lines[j][3-j] for j in range(0,4)])

	candidates = lines + rows + [diag1,diag2]
	flag = 0
	for cand in candidates:
		if cand in x_win:
			flag = 2
			break
		if cand in o_win:
			flag = 3
			break
		if (not flag) and "." in cand:
			flag = 1

	outfile.write("Case #" + str(i+1) + ": " + status[flag])
	outfile.write("\n")
	infile.readline() #skip the empty line