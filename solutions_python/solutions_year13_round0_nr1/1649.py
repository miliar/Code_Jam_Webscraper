
winnings = ['1111000000000000','0000111100000000','0000000011110000','0000000000001111','1000100010001000','0100010001000100','0010001000100010','0001000100010001','1000010000100001','0001001001001000']

wins = []

for item in winnings:
	wins.append(int(item, 2))


fr = open("A-large.in", 'r')
fw = open("output.txt", 'w')

lines = fr.readlines()

numTests = lines[0].strip()

i = 1
curTest = 0

while (int(curTest) < int(numTests)):
	XVal = 0
	OVal = 0
	curPos = 0
	unfilled = False
	for gameLine in range(4):
		curLine = lines[i].strip()
		for c in curLine:
			if c == 'X':
				XVal |= (1<<curPos)
			elif c == 'O':
				OVal |= (1<<curPos)
			elif c == 'T':
				XVal |= (1<<curPos)
				OVal |= (1<<curPos)
			else:
				unfilled = True
				
			curPos += 1
		i += 1
	i += 1
	curTest += 1
	
	if True in [XVal&w == w for w in wins]:
		fw.write("Case #%d: %s\n" % (curTest, "X won"))
	elif True in[OVal&w == w for w in wins]:
		fw.write("Case #%d: %s\n" % (curTest, "O won"))
	elif unfilled is False:
		fw.write("Case #%d: %s\n" % (curTest, "Draw"))
	else:
		fw.write("Case #%d: %s\n" % (curTest, "Game has not completed"))

	
fr.close()
fw.close()