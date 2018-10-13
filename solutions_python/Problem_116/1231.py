
def testStr(x, t):
	if((x[0] == t or x[0] == 'T') and (x[1] == t or x[1] == 'T') and (x[2] == t or x[2] == 'T') and (x[3] == t or x[3] == 'T')):
		return 1
	if((x[4] == t or x[4] == 'T') and (x[5] == t or x[5] == 'T') and (x[6] == t or x[6] == 'T') and (x[7] == t or x[7] == 'T')):
		return 1
	if((x[8] == t or x[8] == 'T') and (x[9] == t or x[9] == 'T') and (x[10] == t or x[10] == 'T') and (x[11] == t or x[11] == 'T')):
		return 1
	if((x[12] == t or x[12] == 'T') and (x[13] == t or x[13] == 'T') and (x[14] == t or x[14] == 'T') and (x[15] == t or x[15] == 'T')):
		return 1
	if((x[0] == t or x[0] == 'T') and (x[5] == t or x[5] == 'T') and (x[10] == t or x[10] == 'T') and (x[15] == t or x[15] == 'T')):
		return 1
	if((x[3] == t or x[3] == 'T') and (x[6] == t or x[6] == 'T') and (x[9] == t or x[9] == 'T') and (x[12] == t or x[12] == 'T')):
		return 1
	for i in range(0, 4):
		if((x[i] == t or x[i] == 'T') and (x[i+4] == t or x[i+4] == 'T') and (x[i+8] == t or x[i+8] == 'T') and (x[i+12] == t or x[i+12] == 'T')):
			return 1

f = open('test.txt', 'r')
fout = open("output.txt", "w")
case = 0
i = 0
x=""
for line in f:
	if case == 0:
		case+=1
		continue
	x = x + line
	i += 1
	if i == 5:
		x = x.replace("\n", "")
		if testStr(x, "X") == 1:
			fout.write("Case #" + str(case) + ": X won\n")
		elif testStr(x, "O") == 1:
			fout.write("Case #" + str(case) + ": O won\n")
		elif x.find(".") == -1:
			fout.write("Case #" + str(case) + ": Draw\n")
		else:
			fout.write("Case #" + str(case) + ": Game has not completed\n")
		x=""
		i = 0
		case += 1
