import re

f = open('input.txt','r')
w = open('output.txt', 'w')
testcase = int(f.readline())

for a in range(0, testcase):
	msg = ""
	x = [0,0,0,0]
	o = [0,0,0,0]
	xd = 0
	od = 0
	xdd = 0
	odd = 0
	dotcount = 0
	for i in range(0,4):
		line = f.readline()
		if (("XXXX" in line) or ("TXXX" in line) or ("XXXT" in line) or ("XTXX" in line) or ("XXTX" in line)):
			msg = "X won"
			break
		elif (("OOOO" in line) or ("TOOO" in line) or ("OOOT" in line) or ("OTOO" in line) or ("OOTO" in line)):
			msg = "O won"
			break
		else:
			for j in range(0,4):
				if (line[j] == 'X'):
					x[j] += 1
					if ((i == 0 and j == 0) or (i == 1 and j == 1) or (i == 2 and j == 2) or (i == 3 and j == 3) ):
						xd += 1
					if ((i == 3 and j == 0) or (i == 2 and j == 1) or (i == 1 and j == 2) or (i == 0 and j == 3) ):
						xdd += 1
				elif (line[j] == 'O'):
					o[j] += 1
					if ((i == 0 and j == 0) or (i == 1 and j == 1) or (i == 2 and j == 2) or (i == 3 and j == 3)):
						od += 1
					if ((i == 3 and j == 0) or (i == 2 and j == 1) or (i == 1 and j == 2) or (i == 0 and j == 3) ):
						odd += 1
				elif (line[j] == 'T'):
					x[j] += 1
					o[j] += 1
					if ((i == 0 and j == 0) or (i == 1 and j == 1) or (i == 2 and j == 2) or (i == 3 and j == 3) ):
						xd += 1
					if ((i == 3 and j == 0) or (i == 2 and j == 1) or (i == 1 and j == 2) or (i == 0 and j == 3) ):
						xdd += 1
					if ((i == 0 and j == 0) or (i == 1 and j == 1) or (i == 2 and j == 2) or (i == 3 and j == 3) ):
						od += 1
					if ((i == 3 and j == 0) or (i == 2 and j == 1) or (i == 1 and j == 2) or (i == 0 and j == 3) ):
						odd += 1
				else:
					x[j] = 0
					o[j] = 0
					dotcount += 1

				if x[j] == 4 or xd == 4 or xdd == 4:
					msg = "X won"
					break
				if o[j] == 4 or od == 4 or odd == 4:
					msg = "O won"
					break

	if msg == "":
		if dotcount == 0:
			msg = "Draw"
		else:
			msg = "Game has not completed"

	for k in range(i+1,4):
		line = f.readline()

	ans = 'Case #{0}: {1}'.format(a+1,msg)
	print(ans)
	w.write(ans)

	if a != testcase-1:
		line = f.readline()
		w.write("\n")