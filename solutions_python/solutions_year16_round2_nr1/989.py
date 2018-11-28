
def foo(ss):
	charDict = {}
	for ch in "ZERONTWHFUIVSXG":
		charDict[ch] = 0
	for ch in ss:
		charDict[ch] += 1

	digitList = [0 for i in range(10)]

	if charDict['X'] != 0:
		t = charDict['X']
		charDict['S'] -= t
		charDict['I'] -= t
		digitList[6] += t
	if charDict['G'] != 0:
		t = charDict['G']
		charDict['E'] -= t
		charDict['I'] -= t
		charDict['H'] -= t
		charDict['T'] -= t
		digitList[8] += t
	if charDict['U'] != 0:
		t = charDict['U']
		charDict['F'] -= t
		charDict['O'] -= t
		charDict['R'] -= t
		digitList[4] += t
	if charDict['Z'] != 0:
		t = charDict['Z']
		charDict['E'] -= t
		charDict['R'] -= t
		charDict['O'] -= t
		digitList[0] += t
	if charDict['W'] != 0:
		t = charDict['W']
		charDict['T'] -= t
		charDict['O'] -= t
		digitList[2] += t
	if charDict['O'] != 0:
		t = charDict['O']
		charDict['N'] -= t
		charDict['E'] -= t
		digitList[1] += t
	if charDict['H'] != 0:
		t = charDict['H']
		charDict['T'] -= t
		charDict['R'] -= t
		charDict['E'] -= t*2
		digitList[3] += t
	if charDict['S'] != 0:
		t = charDict['S']
		charDict['V'] -= t
		charDict['N'] -= t
		charDict['E'] -= 2*t
		digitList[7] += t
	if charDict['N'] != 0:
		t = charDict['N']/2
		charDict['I'] -= t
		charDict['E'] -= t
		digitList[9] += t
	if charDict['F'] != 0:
		t = charDict['F']
		charDict['I'] -= t
		charDict['V'] -= t
		charDict['E'] -= t
		digitList[5] += t

	resStr = ""
	for index in range(len(digitList)):
		for y in range(digitList[index]):
			resStr += str(index)

	return resStr

with open("A-large.in") as readfile:
	with open ("output.txt", "w") as writefile:
		N  = int(readfile.readline())
		for x in range(N):
			string = readfile.readline().strip()
			resStr = foo(string)
			writefile.write("Case #" + str(x+1) + ": " + resStr + "\n")
